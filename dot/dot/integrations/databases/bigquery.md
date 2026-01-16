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

     

## Allow Dot IPs

If your organization uses a network policy to manage BigQuery access, Dot will only access your BigQuery through the following IPs:

* `3.229.110.216`
* `3.122.135.165`
