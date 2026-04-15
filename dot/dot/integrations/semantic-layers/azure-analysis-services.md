---
description: Connect Dot to Azure Analysis Services semantic models
---

# Azure Analysis Services

Connect Dot to your Azure Analysis Services (AAS) server to query your semantic models using natural language. Dot syncs your tables, columns, measures, and relationships so you can ask questions about your data without writing DAX.

{% hint style="info" %}
**Requirements**

* An Azure Analysis Services server with at least one deployed model
* Read access to the models you want to query
* One of the two authentication methods described below
{% endhint %}

## Authentication Methods

### Option 1: Interactive SSO (OAuth)

Sign in with your Microsoft account. Dot uses delegated access on your behalf — no service principal setup required.

1. Go to **Settings → Semantic Layers → Azure Analysis Services**
2. Enter your **Server URL** (e.g., `asazure://westeurope.asazure.windows.net/myserver`)
3. Optionally enter a **Database Name** to sync only that model, or leave empty to sync all models on the server
4. Click **Connect with Microsoft**
5. Sign in with your Microsoft account and grant access
6. Dot will start syncing your semantic models

{% hint style="success" %}
**Finding your Server URL**

Open your AAS resource in the Azure Portal. The server name is shown on the Overview page, formatted as:
`asazure://{region}.asazure.windows.net/{servername}`
{% endhint %}

### Option 2: Service Principal

Use an Azure AD app registration for automated, unattended access — ideal for production deployments where you don't want auth tied to a user account.

**1. Create an Entra ID Application**

1. Go to **Azure Portal → Azure Active Directory → App registrations → New registration**
2. Name: `Dot-AAS-Access` (or similar)
3. Account types: Accounts in this organizational directory only
4. Click **Register**
5. Go to **Certificates & secrets → New client secret** and copy the value
6. Note the **Application (client) ID** and **Directory (tenant) ID** from the Overview page

**2. Grant AAS Access**

Add the service principal as a member of a server role:

1. Open SQL Server Management Studio (SSMS) and connect to your AAS server
2. Right-click the server → **Properties → Security**
3. Click **Add** and enter: `app:{client_id}@{tenant_id}`
4. Assign the appropriate role (Reader is sufficient for Dot)

**3. Connect in Dot**

1. Go to **Settings → Semantic Layers → Azure Analysis Services**
2. Enter your **Server URL**, **Database Name**, **Client ID**, **Client Secret**, and **Tenant ID**
3. Click **Connect**

## What Gets Synced

When you connect Azure Analysis Services, Dot imports:

* **Databases / Models** — appear as schemas in Dot
* **Tables and columns** — with their descriptions and data types
* **Measures** — including DAX expressions
* **Relationships** — connections between tables

Dot periodically re-syncs to pick up changes. You can also trigger a manual sync from the connection settings.

## Troubleshooting

### AADSTS650052: Missing Service Principal

If you see an error like:

> AADSTS650052: The app is trying to access a service that your organization lacks a service principal for.

This means the Azure Analysis Services first-party application is not registered in your Azure AD tenant. This typically happens if your organization has never provisioned an AAS resource directly, or if AAS was removed.

**Fix:** An Azure AD administrator needs to create the service principal. Run one of the following:

**Azure CLI:**

```bash
az login --tenant YOUR_TENANT_ID
az ad sp create --id 4ac7d521-0382-477b-b0f8-7e1d95f85ca2
```

**PowerShell:**

```powershell
Connect-AzureAD -TenantId "YOUR_TENANT_ID"
New-AzureADServicePrincipal -AppId "4ac7d521-0382-477b-b0f8-7e1d95f85ca2"
```

Or go to **Azure Portal → Enterprise Applications → New Application**, search for "Azure Analysis Services", and add it.

This is a one-time operation. Once completed, the OAuth flow will work.

{% hint style="info" %}
**Power BI users:** If your data lives in AAS but you access it through Power BI, you can use the [Power BI connector](powerbi-semantic-layer.md) instead — it does not require the AAS service principal.
{% endhint %}

### Token Expired / Please Reconnect

If you see "No access token available" or similar errors, your OAuth refresh token may have expired (tokens last 90 days). Go to **Settings → Semantic Layers → Azure Analysis Services** and click **Connect with Microsoft** again to re-authenticate.

## Limitations

{% hint style="warning" %}
**Known limitations**

* **Cross-tenant access** — querying AAS servers in a different Azure AD tenant requires B2B guest access
* **Row-Level Security (RLS)** — supported for Service Principal auth, but the SP must be added to an RLS role in SSMS
* **Maximum 100,000 rows per query** — larger result sets are truncated
{% endhint %}
