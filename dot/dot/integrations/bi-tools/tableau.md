# Tableau

Both Tableau Cloud (Online) or Tableau Server (2019.3 or later) are supported.

## Tableau Online <a href="#tableau-online" id="tableau-online"></a>

**Authentication**

Generate a Personal Access Token with a user who is either "Site Admin Explorer" or "Site Admin Creator".

1. Open “My Account Settings“

![](https://docs.sled.so/~gitbook/image?url=https%3A%2F%2F2457798860-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FEdkjXblQVFxdE5uvkTZt%252Fuploads%252Fbqm2rhWu90uUXeiDhJAW%252Fgrafik.png%3Falt%3Dmedia%26token%3D42f9c7de-8267-43c5-af2c-ec953084ad46\&width=300\&dpr=4\&quality=100\&sign=606aa2ae\&sv=2)

2\. Go to the section “Personal Access Tokens”

![](https://docs.sled.so/~gitbook/image?url=https%3A%2F%2F2457798860-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FEdkjXblQVFxdE5uvkTZt%252Fuploads%252FLlV9TCmQmJBK3a5OlfVM%252Fgrafik.png%3Falt%3Dmedia%26token%3Dca573f80-d452-418d-9ebb-bbf5bb8e4427\&width=768\&dpr=4\&quality=100\&sign=bd2ab74e\&sv=2)

3\. Create new token

![](https://docs.sled.so/~gitbook/image?url=https%3A%2F%2F2457798860-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FEdkjXblQVFxdE5uvkTZt%252Fuploads%252FeZwVf7mYcTPLPKUySC3S%252Fgrafik.png%3Falt%3Dmedia%26token%3Dab3c7dd0-e124-4aee-aa4d-936268c67121\&width=300\&dpr=4\&quality=100\&sign=3beb599f\&sv=2)

4\. Copy token secret to clipboard and save it. This token is valid for 1 year and will need to be refreshed.



## **Tableau Server** <a href="#tableau-server" id="tableau-server"></a>

The setup is identical to Tableau Cloud. If your server is not reachable from the internet, please coordinate with our customer success team [hi@getdot.ai](mailto:hi@getdot.ai) — a typical network setup uses OpenVPN.



## Connected App <a href="#connected-app" id="connected-app"></a>

A site administrator sets it up in Tableau:

1. Go to **Settings → Connected Apps** and create a new app of type **Direct Trust**. On Tableau Server this lives in the site settings and requires version 2022.1 or later (earlier versions expose connected apps only via the REST API).
2. Add the Dot host your workspace runs on to the app's domain allowlist — Tableau refuses the embed otherwise.
3. Generate a secret and copy three values: **Client ID**, **Secret ID** and **Secret Value**. Secret ID and Secret Value are easy to mix up.



## Connect in Dot

Enter your details, hit connect and watch it sync. As soon as it's done, you can head over to **Model /External assets** to further curate what Dot should know about.

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

Open the connection's **Connected App** tab, paste the three values from Tableau and enter the email of a Tableau admin user.

<figure><img src="../../../.gitbook/assets/tableau-connected-app-tab.png" alt=""><figcaption></figcaption></figure>

Use an existing licensed Tableau login, ideally an admin so it can see every workbook — Dot does not create a user and does not need an extra licence. When someone asks a question, Tableau applies that person's own permissions, so everyone sees exactly what they already see in Tableau.



## What Dot needs access to <a href="#what-dot-needs-access-to" id="what-dot-needs-access-to"></a>

The same three things apply to Tableau Cloud and Tableau Server:

1. The **Metadata API** is enabled. On Tableau Cloud it always is. On Tableau Server an administrator enables it once with `tsm maintenance metadata-services enable` — see [Tableau's guide](https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_start.html#enable-the-tableau-metadata-api-for-tableau-server). Without it Dot still lists workbooks and views, but loses the lineage to warehouse tables and can't see calculated-field definitions.

2. Dot's IPs are allowlisted: `5.78.211.110` and `178.105.217.177`.
3. The paths Dot needs are reachable: `/api/*` for catalog and metadata, and — for exact tile values — `/javascripts/*`, `/views/*`, `/vizql/*` and `/vizportal/*`. If only `/api/*` is reachable, the connection looks healthy and the catalog syncs, while exact values silently don't work.
