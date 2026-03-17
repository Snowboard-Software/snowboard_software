---
description: Single Sign-On with Microsoft Entra ID (Azure AD)
---

# Azure Active Directory

## Integrating Single Sign-On (SSO) with Azure AD for Sled

Sled integrates with Azure Active Directory (Microsoft Entra ID) using OAuth 2.0 / OpenID Connect. This guide walks through the setup process for both the Azure AD and Sled sides of the configuration.

### Technical Overview

| Property | Value |
|----------|-------|
| Protocol | OAuth 2.0 / OpenID Connect |
| Scopes | `openid`, `profile`, `email`, `User.Read`, `GroupMember.Read.All` |
| Redirect URI | `https://{your-sled-domain}/api/auth/azure/callback` |
| Tenant type | Single tenant |

---

## Part 1: Azure AD Configuration

### Step 1: Register a New Application

1. Go to the **Azure Portal** and navigate to **Azure Active Directory** > **App registrations**
2. Click **New registration**

### Step 2: Application Registration

1. Enter the name of the application, e.g. `Sled`
2. Under **Supported account types**, select **"Accounts in this organizational directory only"** (Single tenant)
3. For the **Redirect URI**, select **Web** and enter: `https://{your-sled-domain}/api/auth/azure/callback`

<figure><img src="../.gitbook/assets/Screenshot_from_2024-01-16_13-53-20.png" alt=""><figcaption></figcaption></figure>

4. Click **Register**

### Step 3: Copy Application IDs

Once registered, you will be redirected to the application overview page. Copy and save these two values:

* **Application (client) ID**
* **Directory (tenant) ID**

<figure><img src="../.gitbook/assets/Screenshot_from_2024-01-16_13-53-41.png" alt=""><figcaption></figcaption></figure>

### Step 4: Create a Client Secret

1. In the application menu, click **Certificates & secrets**
2. Click **New client secret**
3. Set a description (e.g. `Sled SSO`) and an expiration (12 or 24 months recommended)

<figure><img src="../.gitbook/assets/Screenshot_from_2024-01-16_13-54-20.png" alt=""><figcaption></figcaption></figure>

4. Click **Add**
5. **Immediately copy the secret Value** (not the Secret ID) - this is only shown once

<figure><img src="../.gitbook/assets/Screenshot_from_2024-01-16_13-54-30.png" alt=""><figcaption></figcaption></figure>

### Step 5: Configure API Permissions

1. In the application menu, go to **API permissions**
2. Click **Add a permission** > **Microsoft Graph** > **Delegated permissions**
3. Add the following permissions:

| Permission | Purpose | Admin Consent |
|------------|---------|---------------|
| `User.Read` | Read the signed-in user's profile (email, name) | No |
| `GroupMember.Read.All` | Read the signed-in user's group memberships | Yes |

4. Click **Add permissions**
5. Click **Grant admin consent for \[Your Organization]** and confirm

{% hint style="info" %}
Granting admin consent for `GroupMember.Read.All` requires Global Administrator or Privileged Role Administrator rights.
{% endhint %}

---

## Part 2: Azure AD Groups and Role Mapping

Sled uses Azure AD Security Groups to control access levels. This section explains how the mapping between Azure AD groups and Sled roles works.

### How It Works

1. When a user logs in via Azure SSO, Sled queries the Microsoft Graph API for the user's group memberships
2. Sled checks the user's groups against the configured group mappings
3. The **highest-privilege matching group** determines the user's role
4. If none of the user's groups match, the user gets **Viewer** access (read-only)
5. Group memberships are checked fresh on every login - changes in Azure AD take effect on the next login

### Sled Roles

| Role | Permissions |
|------|------------|
| **Admin** | Full access: settings, user management, edit data, read data, search |
| **Editor** | Edit data, read data, search |
| **Viewer** | Read-only: browse data and search (default for all SSO users) |

### Step 6: Create Security Groups (Optional)

{% hint style="info" %}
This step is **optional**. Without any group configuration, all authenticated Azure AD users automatically receive Viewer (read-only) access in Sled. Only create groups if you need to grant Editor or Admin permissions.
{% endhint %}

1. Navigate to **Azure Active Directory** > **Groups**
2. Click **New group**
3. Create groups as needed:

| Group Name | Group Type | Membership Type | Description |
|------------|-----------|-----------------|-------------|
| `Sled Admins` | Security | Assigned | Full administrative access to Sled |
| `Sled Editors` | Security | Assigned | Can edit and review data in Sled |

4. For each group, open the group and copy the **Object ID** from the Overview page

### Step 7: Assign Users to Groups

1. Open each group in **Azure Active Directory** > **Groups**
2. Go to **Members** > **Add members**
3. Search for and select the users who need the respective access level
4. Click **Select**

Users not assigned to any Sled group can still log in and will receive Viewer access by default.

### Step 8: Restrict Application Access (Optional)

To limit which users can use Sled SSO (rather than allowing all users in your tenant):

1. In Azure, go to **Enterprise applications** and find your Sled application
2. Go to **Manage** > **Users and Groups**
3. Click **Add user/group** and assign the users or groups that should have access

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

4. Go to **Manage** > **Properties**

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

5. Set **Assignment required?** to **Yes** - now only explicitly assigned users can authenticate

---

## Part 3: Sled Configuration

### Step 9: Configure Azure SSO in Sled

1. Log into Sled as an **admin user**
2. Navigate to **Settings** (gear icon)
3. Scroll to the **Azure SSO Configuration** section
4. Fill in the fields:

| Field | Value |
|-------|-------|
| **Tenant ID** | Directory (tenant) ID from Step 3 |
| **Client ID** | Application (client) ID from Step 3 |
| **Client Secret** | Secret value from Step 4 |
| **Redirect URI** | `https://{your-sled-domain}/api/auth/azure/callback` |
| **Enable Azure SSO** | Enabled |
| **Enable Password Login** | Enabled (recommended during initial setup) |

5. Click **Save Configuration**

### Step 10: Configure Group Mappings in Sled

After enabling Azure SSO, the **Azure AD Group Mappings** section appears below the SSO configuration.

1. Click **Add Mapping**
2. Fill in:
   * **Azure AD Group ID**: The Object ID of the Azure AD Security Group (UUID format)
   * **Azure AD Group Name**: A friendly label for your reference (e.g. "Data Engineering")
   * **Sled Role**: Select Admin, Editor, or Viewer
3. Click **Save**
4. Repeat for each group you want to map

#### Example Configuration

| Azure AD Group | Group Object ID | Sled Role |
|----------------|-----------------|-----------|
| Sled Admins | `a1b2c3d4-e5f6-...` | Admin |
| Data Engineers | `e5f6a7b8-c9d0-...` | Editor |
| BI Analysts | `1a2b3c4d-5e6f-...` | Editor |

With this setup:
* Members of "Sled Admins" get **Admin** access
* Members of "Data Engineers" or "BI Analysts" get **Editor** access
* All other authenticated Azure AD users get **Viewer** access
* A user in both an Admin and an Editor group gets **Admin** (highest privilege wins)

---

## Testing

### Test SSO Login

1. Log out of Sled
2. On the login page, click **"Sign in with Microsoft"**
3. Authenticate with your Azure AD credentials (MFA if enabled)
4. After authentication, you should be redirected back to Sled and logged in
5. Check your assigned role in your user profile (top right)

### Verify Group-Based Roles

1. Log in with a user in a mapped Admin group - verify they have Admin access
2. Log in with a user in a mapped Editor group - verify they have Editor access
3. Log in with a user not in any mapped group - verify they have Viewer access

---

## Troubleshooting

### "Failed to exchange code for token"

Client secret is incorrect or expired. Verify the secret in Sled matches Azure Portal. If expired, create a new one and update the Sled configuration.

### "Failed to get user information from Microsoft Graph"

Missing API permissions or admin consent not granted. Go to App registration > API permissions and verify `User.Read` and `GroupMember.Read.All` are present and granted.

### "Redirect URI mismatch"

The redirect URI in Azure does not match the one configured in Sled. Verify both match exactly, including protocol (https) and path (`/api/auth/azure/callback`).

### User has the wrong role

1. Verify the user's group membership in Azure AD
2. Check that the group's Object ID matches the mapping in Sled Settings
3. Have the user log out and log in again (roles are refreshed on each login)

### Group changes not taking effect

Azure AD group changes can take a few minutes to propagate. Have the user wait a few minutes, then log out and log in again. Sled fetches group memberships fresh on every login.

---

## Optional: Disable Password Login

Once SSO is working reliably:

1. Go to **Settings** > **Azure SSO Configuration**
2. Set **Enable Password Login** to **Disabled**
3. Click **Save**

{% hint style="warning" %}
Keep at least one admin account with password access as backup before disabling password login.
{% endhint %}

---

## FAQ

**Can users still use passwords after enabling SSO?**\
Yes, by default both methods work simultaneously. Disable password login in Settings once SSO is stable.

**What happens if a user is in multiple mapped groups?**\
The highest-privilege role wins (Admin > Editor > Viewer).

**What if no group mappings are configured?**\
All authenticated Azure AD users get Viewer (read-only) access automatically.

**Does it work with MFA and Conditional Access?**\
Yes. Any MFA or Conditional Access policies in your Azure AD tenant are enforced during the Microsoft login step. No special configuration needed in Sled.

**How do I find a group's Object ID?**\
Azure Portal > Azure Active Directory > Groups > click the group > Object ID is in the Overview tab.

**How quickly do group changes take effect?**\
Users need to log out and log in again. Sled fetches group memberships fresh on each login. Azure AD may take a few minutes to propagate group changes.
