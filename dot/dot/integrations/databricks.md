# Databricks

## Connect Dot to Databricks

### 1. Generate a Databricks Access Token

Dot requires an access token to connect to Databricks. It's recommended to use a service principal for this purpose.

#### Option A: Using a Service Principal

1. **Create a Service Principal**\
   Follow the [Databricks documentation](https://docs.databricks.com/api/workspace/serviceprincipals/create) to create a service principal.
2. **Grant Token Usage to the Service Principal**\
   Ensure the service principal has permissions to use access tokens.
3.  **Generate an Access Token**\
    Use the Databricks CLI to generate an access token:

    ```bash
    databricks tokens create --comment "Dot Integration" --lifetime-seconds 0
    ```



Save the generated token securely.

#### Option B: Using a Personal Access Token

Alternatively, you can generate a personal access token for your user account.

### 2. Grant Data Permissions to Dot's Service Principal

To allow Dot to access the necessary data, grant the appropriate permissions.

#### Unity Catalog

**Access to All Tables in a Catalog**

```sql
GRANT USE CATALOG ON CATALOG <catalog_name> TO `<application_id>`;
GRANT USE SCHEMA ON CATALOG <catalog_name> TO `<application_id>`;
GRANT SELECT ON CATALOG <catalog_name> TO `<application_id>`;
```



**Access to Specific Tables**

```sql
GRANT USE CATALOG ON CATALOG <catalog_name> TO `<application_id>`;
GRANT USE SCHEMA ON SCHEMA <catalog_name>.<schema_name> TO `<application_id>`;
GRANT SELECT ON TABLE <catalog_name>.<schema_name>.<table_name> TO `<application_id>`;
```



**Access to System Tables for Data Insights**

1.  **Enable System Schemas**\
    Use the Databricks API to enable system schemas:

    ```bash
    curl -X PUT -H "Authorization: Bearer <token>" \
    "https://<workspace_url>/api/2.0/unity-catalog/metastores/<metastore_id>/systemschemas/query"
    ```



2.  **Grant Access to System Tables**

    ```sql
    GRANT USE SCHEMA ON SCHEMA system.query TO `<application_id>`;
    GRANT SELECT ON TABLE system.query.history TO `<application_id>`;
    GRANT USE SCHEMA ON SCHEMA system.access TO `<application_id>`;
    GRANT SELECT ON TABLE system.access.column_lineage TO `<application_id>`;
    ```



#### Hive Metastore

```sql
GRANT READ_METADATA, USAGE, SELECT ON CATALOG <catalog_name> TO `<application_id>`;
```



### 3. Create a Databricks SQL Warehouse for Dot

1. **Create a SQL Warehouse**\
   Follow the [Databricks documentation](https://docs.databricks.com/compute/sql-warehouse/create.html) to create a SQL Warehouse.
2. **Assign Permissions**\
   In the SQL Warehouse settings, click 'Permissions' and grant the Dot service principal 'Can Use' permissions.

### 4. Add Databricks as a Connection in Dot

1. **Navigate to Connections**\
   In Dot, go to the Settings / Connections page.
2. **Add a New Connection**\
   Click '+ Database Connection' and select Databricks
3. **Enter Connection Details**\
   Provide the following information:
   * **Host**: From the SQL Warehouse created in Step 3
   * **Port**: Typically 443
   * **HTTP Path**: From the SQL Warehouse
   * **Access Token**: Generated in Step 1

***

This guide should help you set up a connection between Dot and Databricks.
