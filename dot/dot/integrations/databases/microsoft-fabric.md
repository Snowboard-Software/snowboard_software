# Microsoft Fabric

Connect Dot to your Microsoft Fabric Data Warehouse or SQL Analytics Endpoint to query your data using natural language.

## Authentication Methods

Microsoft Fabric supports two authentication methods for external applications like Dot:

### Option 1: Service Principal Authentication (Recommended)

Service Principal authentication provides secure, automated access without requiring user credentials.

**1. Create an Entra ID Application and Service Principal**

1. **Register a new application** in Azure Portal:
   * Go to Azure Active Directory > App registrations > New registration
   * Name: `Dot-Fabric-Access` (or similar)
   * Account types: Accounts in this organizational directory only
   * Click "Register"
2. **Create a client secret**:
   * Go to Certificates & secrets > New client secret
   * Description: `Dot Integration`
   * Expires: Choose appropriate duration (12 months recommended)
   * Copy the **Value** (this is your `client_secret`)
3. **Note the following values** from the Overview page:
   * **Application (client) ID** (this is your `client_id`)
   * **Directory (tenant) ID** (this is your `tenant_id`)

**2. Configure Fabric Tenant Settings**

1. **Enable Service Principal API access**:
   * Go to Fabric Admin Portal > Tenant settings
   * Find "Developer settings" > "Service principals can use Fabric APIs"
   * Enable this setting for your organization or specific security groups

**3. Grant Workspace Access**

1. **Add Service Principal to Workspace**:
   * Go to your Fabric workspace
   * Settings > Manage access
   * Add people or groups > Enter your Service Principal name
   * Assign **Contributor** role (recommended) or **Member** role

### Option 2: Entra UPN Authentication

Use your Microsoft Entra ID username and password for direct authentication.

**Requirements:**

* Valid Entra ID user account with access to the Fabric workspace
* Username in UPN format (e.g., `user@company.com`)
* Account password

**Grant User Access:**

1. **Add user to Workspace**:
   * Go to your Fabric workspace
   * Settings > Manage access
   * Add the user account
   * Assign **Contributor** role (recommended)

## Connection Information

### Required Connection Details

**For Service Principal Authentication:**

* **Server**: Your Fabric SQL Analytics Endpoint (e.g., `abc123def456.datawarehouse.fabric.microsoft.com`)
* **Database**: Your warehouse database name
* **Tenant ID**: Directory (tenant) ID from Azure AD
* **Client ID**: Application (client) ID from Azure AD
* **Client Secret**: Secret value created in Azure AD

**For Entra UPN Authentication:**

* **Server**: Your Fabric SQL Analytics Endpoint
* **Database**: Your warehouse database name
* **Username**: Your Entra UPN (e.g., `user@company.com`)
* **Password**: Your account password

#### Finding Your Connection String

1. **Get your SQL Analytics Endpoint**:
   * Open your Fabric workspace
   * Go to your Data Warehouse or Lakehouse
   * Settings > SQL endpoint
   * Copy the server name from the connection string

### Network Requirements

#### Dot IP Allowlist

If your organization uses network firewalls or IP restrictions, add these Dot service IP addresses to your allowlist:

* `3.229.110.216`
* `3.122.135.165`

#### Port Requirements

* **Port 1433** (TCP) - Standard SQL Server port for TDS connections
* **Port 443** (TCP) - HTTPS for Fabric API access



