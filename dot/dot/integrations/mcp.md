# MCP

### What is MCP?

MCP (Model Context Protocol) enables AI assistants like Claude, Cursor, and ChatGPT to connect directly to your data sources through secure connections. With Dot's MCP integration, AI assistants can query your business data while maintaining all your existing permissions and setup.

### Authentication Methods

Dot supports two ways to authenticate MCP connections:

#### OAuth (Recommended)

OAuth lets your AI client authenticate directly with Dot — no tokens to copy or manage. When you add Dot as a connector, your client opens a browser window where you sign into Dot and approve access. Your session stays active for up to a year.

**Supported clients**: Claude Web, Claude Desktop, Claude Code, Cursor, Windsurf

#### API Token

Token-based auth works with all MCP clients. You generate a token in Dot and paste it into your client's configuration. This method is required for clients that don't support OAuth (ChatGPT, Raycast, and generic MCP clients).

### Quick Start

**With OAuth** (Claude, Cursor, Windsurf):

1. Go to **Settings → Integrations** in Dot
2. Select your client under the MCP section
3. Copy the URL or run the provided command
4. Your client will open a browser to authenticate — sign in and click **Allow**

**With API Token** (all clients):

1. Go to **Settings → Integrations** in Dot
2. Select your client and switch to the **API Token** tab
3. Click **Generate MCP Token** and copy it immediately — you won't see it again
4. Follow the client-specific instructions to add the URL and token

### Client Setup

#### Claude Web (claude.ai)

**Requirements**: Free, Pro, Max, Team, or Enterprise plan. Free users can connect one custom connector at a time.

**Your Dot MCP URL** depends on which region you sign into Dot from:

* **US**: `https://app.getdot.ai/ai/mcp`
* **EU**: `https://eu.getdot.ai/ai/mcp`

Use the same host you use to sign into Dot in the browser. You can also copy the exact URL from **Settings → Integrations** inside Dot.

{% tabs %}
{% tab title="Pro / Max" %}
{% stepper %}
{% step %}
### Open Customize → Connectors

In Claude, click your profile → **Customize** → **Connectors**.

<figure><img src="../../.gitbook/assets/claude-web-customize.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/claude-web-connectors-tab.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Add a custom connector

Click the **+** next to the Connectors header and choose **Add custom connector**.

<figure><img src="../../.gitbook/assets/claude-web-add-custom-menu.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Name it and paste the URL

Name it **Ask Dot**, paste your Dot MCP URL, then click **Add**.

<figure><img src="../../.gitbook/assets/claude-web-add-custom-dialog.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Connect

Click **Connect** on the new **Ask Dot** entry.

<figure><img src="../../.gitbook/assets/claude-web-connect-button.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Authorize in Dot

A Dot tab opens. Review the requested permissions and click **Allow**.

<figure><img src="../../.gitbook/assets/claude-web-oauth-authorize.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Done

Back in Claude, **Ask Dot** now shows as **Connected** with its available tools. Enable it in any chat via the **+** button → **Connectors**.

<figure><img src="../../.gitbook/assets/claude-web-connected-tools.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Team / Enterprise" %}
Team and Enterprise workspaces use a two-step flow: an owner adds the connector once for the organization, then each member connects their own Dot account.

**Owner (one-time setup):**

{% stepper %}
{% step %}
### Open Organization settings → Connectors

In Claude, go to **Organization settings → Connectors**.
{% endstep %}

{% step %}
### Add a custom web connector

Click **Add** → **Custom** → **Web**.
{% endstep %}

{% step %}
### Paste the Dot MCP URL

Name it **Ask Dot**, paste your Dot MCP URL (`app.getdot.ai/ai/mcp` or `eu.getdot.ai/ai/mcp`), then click **Add**.
{% endstep %}
{% endstepper %}

**Each member (once):**

{% stepper %}
{% step %}
### Open Customize → Connectors

Find **Ask Dot** in the list — it'll be marked **Custom**.
{% endstep %}

{% step %}
### Connect

Click **Connect**.

<figure><img src="../../.gitbook/assets/claude-web-connect-button.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Authorize in Dot

A Dot tab opens. Review the permissions and click **Allow**.

<figure><img src="../../.gitbook/assets/claude-web-oauth-authorize.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**API Token fallback:** If OAuth isn't working, follow the same steps but paste the token-appended URL from the **API Token** tab on Dot's Integrations page instead of the plain MCP URL.
{% endhint %}

#### Claude Desktop

**Your Dot MCP URL** is `https://app.getdot.ai/ai/mcp` (US) or `https://eu.getdot.ai/ai/mcp` (EU) — same rule as Claude Web.

{% tabs %}
{% tab title="OAuth (recommended)" %}
1. Open **Settings → Connectors → Add custom connector**.
2. Name it **Ask Dot** and paste your Dot MCP URL.
3. Click **Add**, then **Connect** — Claude opens your browser to authorize. Click **Allow** in Dot.

Once connected, the MCP indicator (hammer icon) appears in the chat input.
{% endtab %}

{% tab title="API Token (manual config)" %}
Edit Claude Desktop's config file:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Paste the Dot server block from the **API Token** tab on Dot's Integrations page, save, and restart Claude Desktop. Look for the MCP indicator (hammer icon) in the chat input.
{% endtab %}
{% endtabs %}

#### Claude Code

{% hint style="success" %}
**OAuth (recommended):** Run the command from Dot's Integrations page:

```bash
claude mcp add --transport http ask_dot https://app.getdot.ai/ai/mcp
```

OAuth will open your browser to authenticate on first use.
{% endhint %}

**Token-based:** Use the token-appended URL instead:

```bash
claude mcp add --transport http ask_dot https://app.getdot.ai/ai/mcp?token=YOUR_TOKEN
```

#### Cursor IDE

{% hint style="success" %}
**OAuth (recommended):** Click the install button on Dot's Integrations page. Cursor will open your browser to authorize.
{% endhint %}

**Token-based (manual setup):**

1. Go to mcp.json via Cursor Settings > Tools & Integration > Add new MCP Server
2. Get the URL and API key from the JSON config section in "Others" on Dot's Integrations page
3. Add to mcpServers in mcp.json:

```json
{
  "mcpServers": {
    "ask_dot": {
      "url": "https://app.getdot.ai/ai/mcp",
      "headers": {
        "API-KEY": "<your-dot-mcp-api-key>"
      }
    }
  }
}
```

#### Windsurf

{% hint style="success" %}
**OAuth (recommended):** Copy the URL from Dot's Integrations page and add it as an MCP server in Windsurf settings. Windsurf will open your browser to authenticate.
{% endhint %}

**Token-based:** Use the token-appended URL from the API Token tab.

#### ChatGPT

**Requirements**: ChatGPT Enterprise, Education, or Team subscription

{% hint style="info" %}
ChatGPT uses token-based authentication only.
{% endhint %}

1. Go to ChatGPT settings for connectors
2. Add a new connector:
   * **Name**: Ask\_dot
   * **Description**: Dot AI-powered data analysis platform. \<Add additional info about the data you have connected and when to use it>
   * **MCP Server URL**: Use the ChatGPT-specific URL from Dot's Integrations page
   * **Authentication**: No Auth (handled via token in URL)

#### Raycast AI

1. Run **"Manage MCP Servers"** command in Raycast
2. Press `Cmd + N` to add a new server
3. Paste the configuration from Dot's Integrations page
4. Submit and use by @-mentioning "dot" in Raycast AI

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### Other MCP Clients

Most MCP clients support URL-based configuration. Use the token-appended URL from Dot's Integrations page. If your client supports OAuth / MCP authorization, use the base URL without a token: `https://app.getdot.ai/ai/mcp`

### Using MCP with Dot

#### Asking Questions

Once configured, you can ask your AI assistant questions about your data:

* "What were total sales last quarter?"
* "Show me top 10 customers by revenue"
* "Compare this month's performance to last month"
* "What data sources are available?"

### Security

#### OAuth Sessions

* OAuth uses industry-standard **OAuth 2.1 with PKCE** for secure authorization
* Access tokens expire after **1 hour** and are automatically refreshed
* Refresh tokens are valid for **1 year** — after that, re-authentication is required
* You can revoke OAuth access anytime by changing your Dot password, which invalidates all sessions
* The consent page shows exactly which permissions the client is requesting before you approve

#### API Token Management

* Special MCP token with limited scope
* **One active token**: Only one MCP token per user
* **Auto-revocation**: New tokens revoke previous ones
* **365-day expiry**: Tokens expire after one year
* **Immediate revocation**: Delete tokens anytime via the UI (by admins)

#### Data Access

* MCP respects all your Dot permissions and has the same data permissions as the user
* Queries run within your organization's scope and user scope
* All data filtering rules are enforced
* All queries are logged for compliance

### Troubleshooting

#### OAuth Issues

**Browser doesn't open for authentication**

* Ensure your AI client is up to date
* Try the token-based method as a fallback
* Check that your browser isn't blocking pop-ups from Dot

**"Authorization session expired" error**

* The consent page expires after 10 minutes — restart the connection from your AI client

**"Sign in to continue" on consent page**

* You need to be signed into Dot in your browser first
* Click "Open Dot Login", sign in (password or SSO), then click "Continue"

#### Token Issues

**"Invalid API token" error**

* Verify you copied the complete token
* Check if token was revoked or replaced
* Ensure you're using the correct Dot URL

**"Token does not have required MCP access" error**

* Generate a new MCP token from Settings → Integrations
* Ensure you're not using a regular API token

#### Connection Issues

**Connection timeout**

* Check network connection to Dot
* Verify the Dot instance URL is correct
* Some clients have a tool timeout setting — adjust it accordingly
