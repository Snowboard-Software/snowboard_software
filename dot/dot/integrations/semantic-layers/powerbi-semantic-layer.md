---
description: Connect with PowerBIs Semantic Models
---

# PowerBI Semantic Layer

{% hint style="info" %}
Limitations

* Datasets with RLS or SSO enabled are not supported
* executeQueries must be enabled in tenant settings
* My workspace / personal workspaces are not supported with service principals; focus on “new” (v2) workspaces.
{% endhint %}



## 1. Create the Entra app (service principal)

Who: Entra / Azure AD admin (or anyone allowed to create app registrations)

1. In the Entra admin center → App registrations → New registration:
   1. Name: e.g. pbi-backend-service-principal
   2. Supported account types: Single tenant (typical).
   3. Register.
2. On the app page, capture:
   1. Application (client) ID
   2. Directory (tenant) ID
3. Certificates & secrets → New client secret:
   1. Add a secret (e.g. 2 year lifetime).
   2. Copy the secret value now (can’t be read later).
4. Add Security Group (optional)
   4. Create an Entra security group, e.g. pbi-spn-api-callers.
   5. Add the service principal to that group.

&#x20;

For this Power BI scenario you do not need to add Power BI API permissions under _API permissions_ when using service principal auth.



***

## 2. Tenant settings in Fabric / Power BI admin portal

Who: Fabric / Power BI admin

Open Fabric / Power BI Admin portal → Tenant settings. We’ll touch three areas.

&#x20;

### 2.1 Developer settings: allow SPs to use APIs

Under Developer settings:

1. Find “Service principals can use Fabric APIs” (or: “Allow service principals to use Power BI APIs”).
2. Set to:
   1. Enabled, scoped to:
      1. Entire organization, or
      2. Specific security groups → add pbi-spn-api-callers.
3. Save.



This unlocks public Power BI/Fabric APIs for service principals.

***

### 2.2 Integration settings: allow ExecuteQueries

Under Integration settings:

1. Enable “Dataset Execute Queries REST API”.
2. Recommended: restrict to the same group pbi-spn-api-callers.
3. Save.

This specifically allows POST /datasets/{id}/executeQueries (and the in-group variant) for those identities.

***

### 2.3 Admin API settings: allow SPs to list all datasets/semantic models

To let the service principal list everything across the org, enable admin APIs.

Under Admin API settings:

1. Turn on “Service principals can access read-only admin APIs”.
2. Scope to Specific security groups → pbi-spn-api-callers.
3. Save.

&#x20;

This allows the SP to call e.g. GET /v1.0/myorg/admin/datasets(list all datasets) and other admin endpoints, as long as it’s in the allowed group.



Note: when using service principal for admin APIs, the app must nothave admin-consent Power BI permissions configured in Entra; access is governed by these tenant settings instead.

***

## 3. Give the service principal access to workspaces / datasets

Who: Workspace owners (or central admin via script)



For each workspace whose semantic models the backend should query:

1. Go to Workspace → Access.
2. Add either:
   1. The service principal directly, or
   2. The security group pbi-spn-api-callers.
3. Give it a role that implies Read + Build on semantic models, e.g.:
   1. Contributor or Member, or
   2. Viewer + Build (Viewer with Build on the semantic model itself).

&#x20;

The minimum requirement from the API doc:

* Tenant setting “Dataset Execute Queries REST API” enabled, and
* Caller has dataset Read + Build permissions.

&#x20;

To truly “list all” datasets/semantic models:

* The admin APIs (see 2.3) give you org-level listing(/admin/datasets etc.) as long as SP is in the allowed group—no workspace membership needed.
* But to query a dataset with executeQueries, the SP still must have Build/Read on that semantic model’s workspace.

&#x20;

## 4. Connect Dot

Go to Settings / Semantic Layers

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

<br>
