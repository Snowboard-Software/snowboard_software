# Metabase

Both Metabase Cloud or self-hosted Metabase are supported.

To connect Dot to Metabase, follow these steps:

## **1. Generate an API Key in Metabase**

Metabase allows the creation of API keys to authenticate programmatic requests. To generate an API key:

1. Click on the gear icon in the upper right corner of Metabase.
2. Select **Admin settings**.
   1. ![](<../../../.gitbook/assets/image (11).png>)
3. Navigate to the **Settings** tab.
4. Click on the **Authentication** tab in the left-hand menu.
5. Scroll to the **API Keys** section and click **Manage**.
6. Click the **Create API Key** button.
   1.

       <figure><img src="../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
7. Enter a descriptive **Key name** to identify its purpose.
8. Select a **Group** to assign the key, determining its permissions.
9. Click **Create**.
10. Copy the generated API key and store it securely, as Metabase will not display it again.

## **2. Obtain the Metabase Server URL**

Identify the base URL of your Metabase instance. This is typically in the format `http://your-metabase-domain.com` or `https://your-metabase-domain.com`.

## **3. Connect Metabase to Dot**

In Dot, provide the Metabase Server URL and the API key you generated:

1. Open Dot and navigate to **Settings** / **Connections**.
2. Select the option to connect to Metabase.
3. Enter the **Server URL** (your Metabase base URL).
4. Input the **API Key** obtained from Metabase.
5. Click **Connect** to establish the integration.



<figure><img src="../../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

Once connected, Dot will synchronize with Metabase. As soon as it's done, you can head over to **Model** / **External assets** to further curate what Dot should know about.

**Note:** Ensure that the API key has appropriate permissions assigned through its associated group in Metabase to allow Dot to access the necessary data.
