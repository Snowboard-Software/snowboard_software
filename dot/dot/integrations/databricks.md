# Databricks

## Create Databricks SQL Warehouse <a href="#id-3-create-databricks-sql-warehouse" id="id-3-create-databricks-sql-warehouse"></a>

> _**TIP:**_ you can also use an existing one and skip this step

*   Open the workspace tab and click on created workspace console:

    ![](https://docs.airbyte.com/assets/images/databricks\_open\_worspace-54fcb71a96d4c89ad57d2f9b452c7cc8.png)
* Create SQL warehouse:

![](https://docs.airbyte.com/assets/images/databricks\_new\_warehouse-1da87ce787e707aafbdfb143a64f98b6.png)

* Switch to SQL tab
* Click New button
* Choose SQL Warehouse
* After the SQL warehouse was created we can copy its connection details

## Databricks SQL Warehouse connection details <a href="#id-4-databricks-sql-warehouse-connection-details" id="id-4-databricks-sql-warehouse-connection-details"></a>

* Open workspace console.
*   Go to SQL Warehouse section and open it

    ![](https://docs.airbyte.com/assets/images/databricks\_open\_sql\_warehouse-45c92346a31613a0a1398f4cd9c3aafe.png)
*   Open Connection Details tab:

    ![](https://docs.airbyte.com/assets/images/databricks\_sql\_warehouse\_connection\_details-91f70fd5a196d5fd21ade7c83c906fa4.png)

> _**IMPORTANT:**_ `Server hostname`, `Port`, `HTTP path` are used for Dot connection



## Create Databricks Token <a href="#id-7-create-databricks-token" id="id-7-create-databricks-token"></a>

* Open workspace console.
*   Open User Settings, go to Access tokens tab and click Generate new token:

    ![](https://docs.airbyte.com/assets/images/dtabricks\_token\_user\_new-01e5f8918dcc0d95610a75a17ddc63fb.png)
*   In the new window put a comment (Optional) and lifetime:

    ![](https://docs.airbyte.com/assets/images/databricks\_generate\_token-a6eaed2a1d9acfca77414655bd689145.png)

> _**TIP:**_ `Lifetime` can be set to `0`

## Allow Dot IPs

If your organization uses a firewall to manage access to Databricks, Dot will only access your Databricks warehouse through the following IPs:

* `3.229.110.216`
* `3.122.135.165`
