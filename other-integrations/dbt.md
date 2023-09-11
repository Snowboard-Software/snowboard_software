# dbt



## dbt cloud

## Enabling API access

1. Navigate to dbt Cloud: [https://cloud.getdbt.com](https://cloud.getdbt.com)
2. Go to **Account Settings**

![](<../.gitbook/assets/grafik (4) (1).png>)

3. Click the button **Enable Metadata Access**

<figure><img src="../.gitbook/assets/grafik (4).png" alt=""><figcaption></figcaption></figure>

**Retrieving Service Account Token**

4. Click on your profile icon **> Account Settings**

![](<../.gitbook/assets/grafik (1) (1).png>)

5. Click **Service Tokens**. Then click **New Token**

<figure><img src="../.gitbook/assets/grafik (6).png" alt=""><figcaption></figcaption></figure>

6. Enter a token name, like Metaplane. Then click **+ Add** and select the **Job Admin** permission set for **All Projects**. Lastly, click **Save** in the bottom right hand corner to create the service token.
7. Once you click **Save**, you will be provided a service token. This is what Sled will use to start monitoring your dbt projects.



## dbt core

Connecting Sled with DBT Core involves the following steps:

**Step 1: Verify Data Objects Availability in Sled Data Catalog**

Before connecting Sled with DBT Core, make sure that the data objects you want to work with are available in Sled's Data Catalog. If they are unavailable, follow these steps:

1. **Allow Permissions:** If the objects are unavailable, you may need to allow the necessary permissions in your Snowflake accounts. The guide for this step is available [here](https://docs.sled.so/snowflake\_connection#grants-read-access-to-data).
2. **Sync Data Objects:** Once the permissions are granted, sync the data objects from the Settings page in Sled. To do this, go to the Settings page by clicking on your username initials at the top right corner of the page, select "Integrations" from the right navigation, find your connected Snowflake account, and open the Schedule Background Tasks tab. Then, click the "Start Now" button next to the "Discover Tables" option.
3. **Wait for Discovery:** Once the background discovery task is completed, you should be able to find your data objects in Sled's Data Catalog.

**Step 2: Deploy dbt Artifacts Package**

To deploy the DBT artifacts package, follow these steps:

1. **Download Package**: Download the DBT artifacts package from the official GitHub repository at [Sled DBT Artifacts](https://github.com/Snowboard-Software/dbt\_artifacts).
2. **Deploy Package:** Deploy the package to your DBT environment.

**Step 3: Connect db Core to Sled**

To connect DBT Core to Sled, follow these steps:

1. **Access Settings:** Go to the Settings page by clicking on your username initials at the top right corner of the page.
2. **Select Integrations:** From the right navigation, select "Integrations."
3. **Add Integration:** Click the "Add Integration" button, and select "DBT Core" from the list of available integrations.
4. **Enter Details:** Enter your details, such as your snowflake hostname, database, and schema name which contains your DBT models
5. **Test Connection:** Click the "Test Connection" button to ensure that the connection is successful.

💡 **The sync process will occur automatically as defined in the settings, which can also be updated.**



**Step 4: Find Data Objects Tagged Under the dbt\_core tag**

Once the process is completed, you can find your data objects tagged under the dbt\_core tag in Sled's Data Catalog.

💡 **All the dbt tests and their status will be reflected on the data objects tagged under dbt\_core in Sled's Data Catalog.**

