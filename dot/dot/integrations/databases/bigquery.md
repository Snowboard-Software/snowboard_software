# BigQuery

## Prerequisites

You’ll need to have a [Google Cloud Platform](https://cloud.google.com/) account with a [project](https://cloud.google.com/storage/docs/projects) you would like Dot to use. Consult the Google Cloud Platform documentation for how to [create and manage a project](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This project should have a BigQuery dataset for Dot to connect to.



## 1 Create a service account

**Create a service account that you manage in your Google Cloud account.** This account should be provisioned with the following read-only roles:

* `bigquery.dataViewer`
* `bigquery.jobUser`
* `bigquery.readSessionUser`

You'll need to provide the service account's email, a [JSON-formatted key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating), and the location of your BigQuery instance. 



<details>

<summary>Create a service account step by step.</summary>

1. **Navigate to Service Accounts**:
   * Go to the [Google Cloud Console](https://console.cloud.google.com/).
   * In the **Navigation menu**, select **IAM & Admin >** [**Service Accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts).
2. **Create a New Service Account**:
   * Click on **Create Service Account** at the top.
   * Assign a **Name** and optional **Description** (e.g., `dot-service-account` for identification).
   * Click **Create and Continue**.
3. **Assign Required Roles**:
   * In the **Grant this service account access to project** section, add the following roles:
     * **BigQuery Data Viewer** (`roles/bigquery.dataViewer`)
     * **BigQuery Job User** (`roles/bigquery.jobUser`)
     * **BigQuery Read Session User** (`roles/bigquery.readSessionUser`)
   * Click **Continue** to finalize the role assignments.
4. **Create a JSON Key**:
   * Under **Create key (optional)**, select **JSON** and click **Create**.
   * This downloads a JSON file with the service account credentials. Store this file securely; it contains sensitive information.
5. **Service Account Details Needed for Dot**:
   * **Service Account Email**: Visible in the **Email** column on the Service Accounts page.
   * **JSON Key**: The file downloaded in step 4.
   * **BigQuery Location**: The regional or multi-regional setting for your BigQuery instance (e.g., `us-central1`). Find this in the BigQuery console under **BigQuery > Settings**.

</details>



## 2 Granting permissions

The service account also needs the appropriate read-only roles.

The easiest way to grant these roles is through the [Google Cloud Shell](https://console.cloud.google.com/home/dashboard?cloudshell=true).

First, we'll create a custom role for Dot-related permissions and then bind it to the service account that you're using. We'll also bind read-only BigQuery roles to the service account.

**A) Create a Dot custom role**

```bash
gcloud iam roles create DotMonitor \
  --project={{PROJECT_ID}} \
  --title=DotMonitor \
  --description="Dot specific permissions" \
  --permissions=bigquery.jobs.listAll,bigquery.jobs.list
```

_Note that the_ `{{PROJECT_ID}}` _placeholder needs to be replaced with your project id._

**B) Bind the custom role to a service account and apply read-only BQ roles**

<pre class="language-bash"><code class="lang-bash"><strong>gcloud projects add-iam-policy-binding {{PROJECT_ID}} \
</strong>  --member="serviceAccount:{{SERVICE_ACCOUNT}}" \
  --role="projects/{{PROJECT_ID}}/roles/DotMonitor"

gcloud projects add-iam-policy-binding {{PROJECT_ID}} \
  --member="serviceAccount:{{SERVICE_ACCOUNT}}" \
  --role="roles/bigquery.dataViewer"

gcloud projects add-iam-policy-binding {{PROJECT_ID}} \
  --member="serviceAccount:{{SERVICE_ACCOUNT}}" \
  --role="roles/bigquery.jobUser"

gcloud projects add-iam-policy-binding {{PROJECT_ID}} \
  --member="serviceAccount:{{SERVICE_ACCOUNT}}" \
  --role="roles/bigquery.readSessionUser"
</code></pre>

_Note that the_ `{{SERVICE_ACCOUNT}}` _and_ `{{PROJECT_ID}}` _placeholders needs to be replaced with your service account and project id, respectively._

Example Values

* PROJECT\_ID: `super-position-123456`
*   SERVICE\_ACCOUNT: `dot-101@super-position-123456.iam.gserviceaccount.com`

     

## Per-User Access (Optional)

By default, all Dot users in your organization share the same service account when querying BigQuery. If you need each user to only see the data they have access to in BigQuery — based on their individual IAM roles, row-level security policies, or column-level policy tags — you can enable **per-user access** via service account impersonation.

When enabled, Dot runs each query as the logged-in user's Google identity instead of the shared service account. BigQuery enforces access controls natively, so you manage permissions in GCP — not in Dot.

### Prerequisites

* **Google SSO** must be configured in Dot (see [Google SSO setup](../sso/google.md)). Dot uses the SSO-verified email to identify the Google user.
* Users must sign in to Dot via Google SSO. Users who sign in with a password will fall back to the shared service account.

### Step 1: Grant impersonation permissions

The Dot service account needs permission to impersonate your users. Run this in the [Google Cloud Shell](https://console.cloud.google.com/home/dashboard?cloudshell=true):

```bash
gcloud iam service-accounts add-iam-policy-binding {{SERVICE_ACCOUNT}} \
  --project={{PROJECT_ID}} \
  --member="serviceAccount:{{SERVICE_ACCOUNT}}" \
  --role="roles/iam.serviceAccountTokenCreator"
```

Replace `{{SERVICE_ACCOUNT}}` with the Dot service account email (e.g., `dot-101@super-position-123456.iam.gserviceaccount.com`) and `{{PROJECT_ID}}` with your project ID.

### Step 2: Grant BigQuery access to your users

Each user who will use Dot needs BigQuery permissions on the relevant projects and datasets. At minimum:

```bash
gcloud projects add-iam-policy-binding {{PROJECT_ID}} \
  --member="user:alice@yourcompany.com" \
  --role="roles/bigquery.dataViewer"

gcloud projects add-iam-policy-binding {{PROJECT_ID}} \
  --member="user:alice@yourcompany.com" \
  --role="roles/bigquery.jobUser"
```

For managing permissions at scale, use [Google Groups](https://cloud.google.com/iam/docs/groups-in-cloud-console) — grant roles to a group and add users to it.

{% hint style="info" %}
You can also use BigQuery [row-level security policies](https://cloud.google.com/bigquery/docs/row-level-security-intro) and [column-level security (policy tags)](https://cloud.google.com/bigquery/docs/column-level-security-intro) for fine-grained access control. These are enforced automatically when per-user access is enabled.
{% endhint %}

### Step 3: Enable per-user access in Dot

1. Go to **Settings** > **Connections** > **BigQuery**.
2. Click **Edit**.
3. Enable the **Per-user BigQuery access** toggle.
4. Click **Connect** to save.

Once enabled, every query a user runs in Dot will execute as their Google identity. If a user doesn't have access to a table or column in BigQuery, they'll see a clear error message instead of the data.

### How it works

| Scenario | Who runs the query |
|---|---|
| User logged in via Google SSO | The user's Google identity |
| User logged in with password | The shared service account |
| Scheduled queries and alerts | The shared service account |
| Data sync and model operations | The shared service account |

Scheduled queries, alerts, and background operations always use the shared service account, so they are not affected by per-user access settings.

## Allow Dot IPs

If your organization uses a network policy to manage BigQuery access, Dot will only access your BigQuery through the following IPs:

* `3.229.110.216`
* `3.122.135.165`
