# MCP

### What is MCP?

MCP (Model Context Protocol) lets AI assistants like Claude, Codex, Cursor, and ChatGPT connect directly to your data sources through secure connections. With Dot's MCP integration, your assistant can query your business data while respecting all of your existing Dot permissions and setup.

### Your Dot MCP URL

You'll paste this URL into the clients below (ChatGPT uses its own, see [ChatGPT](#chatgpt)). It depends on which region you sign into Dot from:

* **US**: `https://app.getdot.ai/ai/mcp`
* **EU**: `https://eu.getdot.ai/ai/mcp`

Use the same host you use to sign into Dot in the browser. You can also copy the exact URL from your **Profile** in Dot. Open the user menu, choose **Connect Dot**, then **AI tools**, or scroll to **Use Dot elsewhere**. It has one tab per client: Claude, Codex, Cursor, ChatGPT, MCP and CLI.

{% hint style="success" %}
**OAuth is the default.** For supported clients (Claude, Codex, ChatGPT, Cursor, Windsurf), OAuth means no tokens to copy or manage. Just sign into Dot in your browser and click **Allow**. Sessions last up to a year.

If your client can't do OAuth or something goes wrong, see [Using an API token](#using-an-api-token).
{% endhint %}

### Signing in

When Claude, Codex or Cursor asks you to connect, Dot opens in your browser. If you are signed out of Dot, its sign-in page opens in that same window. Sign in with your password, a sign-in email or SSO, or create an account. Dot then brings you back to the **Allow** page, which names the app you return to. Click **Allow**.

The connection request lasts 30 minutes. If it runs out, start connecting again from your app.

### Claude (Web, Desktop, Cowork, Mobile)

**Requirements**: any Claude plan. Free allows one custom connector. On Team and Enterprise, only an Owner adds a custom connector, then each member connects.

{% hint style="info" %}
**You only need to set this up once.** Dot is a remote connector, so once it is on your Claude account it also works in Claude Desktop, Cowork and the Claude mobile apps.
{% endhint %}

{% tabs %}
{% tab title="Add to Claude" %}
{% stepper %}
{% step %}
### Click Add to Claude

In Dot, open your **Profile** and scroll to **Use Dot elsewhere**. On the **Claude** tab, click **Add to Claude**.
{% endstep %}

{% step %}
### Add the connector

Claude opens **Add custom connector** with the name **Dot** and your Dot MCP URL already filled in. Click **Add**. If you are signed out of Claude, sign in first and the dialog opens after.
{% endstep %}

{% step %}
### Connect

Click **Connect** on the new **Dot** entry.

<figure><img src="../../.gitbook/assets/claude-web-connect-button.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Allow access in Dot

Dot's **Allow** page opens. Check the account and permissions, then click **Allow**. If you are signed out of Dot, sign in first (see [Signing in](#signing-in)).

<figure><img src="../../.gitbook/assets/claude-web-oauth-authorize.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Done

Back in Claude, **Dot** shows as **Connected** with its tools. Turn it on in any chat with the **+** button → **Connectors**.

<figure><img src="../../.gitbook/assets/claude-web-connected-tools.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Add it by hand" %}
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

Name it **Dot**, paste your Dot MCP URL, then click **Add**.

<figure><img src="../../.gitbook/assets/claude-web-add-custom-dialog.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Connect and allow

Click **Connect** on the new **Dot** entry. On Dot's **Allow** page, click **Allow**.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Team / Enterprise" %}
On Team and Enterprise, only an Owner can add a custom connector. The Owner adds Dot once for the organization. Then each member connects their own Dot account.

**Owner (once):**

{% stepper %}
{% step %}
### Click Add for your team

In Dot, open your **Profile** and scroll to **Use Dot elsewhere**. On the **Claude** tab, click **Add for your team**.
{% endstep %}

{% step %}
### Add the connector

Claude's admin settings open on **Add custom connector**, with the name **Dot** and your Dot MCP URL filled in. Click **Add**.
{% endstep %}
{% endstepper %}

To add it by hand instead, go to **Organization settings → Connectors** in Claude, click **Add** → **Custom** → **Web**, name it **Dot**, paste your Dot MCP URL, then click **Add**.

**Each member (once):**

{% stepper %}
{% step %}
### Open Customize → Connectors

Find **Dot** in the list. It is marked **Custom**.
{% endstep %}

{% step %}
### Connect

Click **Connect**.

<figure><img src="../../.gitbook/assets/claude-web-connect-button.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Allow access in Dot

Dot's **Allow** page opens. Check the permissions and click **Allow**.

<figure><img src="../../.gitbook/assets/claude-web-oauth-authorize.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}

### Claude Code

Claude Code uses the connectors on your Claude account. If you added Dot in Claude and sign in to Claude Code with that account, Dot is already there. Run `/mcp` to see it.

If you sign in to Claude Code with an API key, it doesn't load those connectors. Add Dot directly:

```bash
claude mcp add --transport http --scope user dot https://app.getdot.ai/ai/mcp
```

`--scope user` adds Dot to every project. For the EU region, use `https://eu.getdot.ai/ai/mcp`. Then run `/mcp` in Claude Code to sign in to Dot.

**Plugin:** you can also install Dot as a plugin from Dot's GitHub marketplace, then run `/mcp` to sign in:

```bash
claude plugin install dot --marketplace Snowboard-Software/getdot
```

The plugin connects to the US region. On EU, use the `claude mcp add` command above with the EU URL.

### Codex

Run this in your terminal (for the EU region, use `https://eu.getdot.ai/ai/mcp`):

```bash
codex mcp add dot --url https://app.getdot.ai/ai/mcp
```

Codex opens your browser to sign in to Dot. Click **Allow**, and Dot is ready in Codex.

The Codex app in the ChatGPT desktop app and the Codex IDE extension share this setup, so Dot shows up there too.

{% hint style="info" %}
**No browser on this machine?** After adding Dot, run `codex mcp login dot --no-browser`. Codex prints a sign-in link. Open it in any browser, sign in and click **Allow**. Then paste the full address the browser ends up on back into the terminal, even if that page doesn't load.
{% endhint %}

**Plugin:** you can also install Dot as a plugin from Dot's GitHub marketplace, then run `codex mcp login dot` to sign in:

```bash
codex plugin marketplace add Snowboard-Software/getdot
codex plugin add dot@getdot
```

The plugin connects to the US region. On EU, use the `codex mcp add` command above with the EU URL.

### Cursor IDE

Cursor connects to Dot directly as a remote MCP server.

**One-click install:** Open the **Cursor** tab in Dot and click **Add to Cursor**. Cursor will open your browser to authorize.

**Manual install:** Add this to `~/.cursor/mcp.json` (use `https://eu.getdot.ai/ai/mcp` for the EU instance):

```json
{
  "mcpServers": {
    "dot": {
      "url": "https://app.getdot.ai/ai/mcp"
    }
  }
}
```

Save the file, then restart Cursor (or toggle the server in **Settings → Tools & Integrations → MCP Tools**). On first connect, Cursor opens your browser to authorize and keeps the session for up to a year.

If you set Dot up earlier with the `npx mcp-remote` proxy, replace that entry with the config above. The proxy could ask you to sign in again and again when more than one Cursor window was open.

{% hint style="info" %}
If you'd rather use a static API token instead of OAuth, see [Using an API token → JSON config](#using-an-api-token) below for the Cursor-specific shape.
{% endhint %}

### Windsurf

Copy the URL from the **MCP** tab in Dot and add it as an MCP server in Windsurf settings. Windsurf will open your browser to authenticate.

### ChatGPT

**Requirements**: ChatGPT Pro, Business, Enterprise or Edu, on the web. On Business and Enterprise, an admin adds Dot.

ChatGPT has its own URL, so copy it from the **ChatGPT** tab in Dot:

* **US**: `https://app.getdot.ai/chatgpt/mcp`
* **EU**: `https://eu.getdot.ai/chatgpt/mcp`

1. In ChatGPT, open **Plugins**, select **+**, then **Add custom MCP server**.
2. Name it **Dot**, then paste the ChatGPT URL as the server URL.
3. Choose **OAuth** for authentication. ChatGPT signs you in to Dot.

It is built for ChatGPT's Deep Research. Ask it to research your company data and it queries Dot.

### Raycast AI

Raycast works with the plain MCP URL. If it can't sign in through your browser, generate a token (see [Using an API token](#using-an-api-token)).

1. Run **"Manage MCP Servers"** command in Raycast
2. Press `Cmd + N` to add a new server
3. Paste the URL, or the token configuration, from the **MCP** tab in Dot
4. Submit and use by @-mentioning "dot" in Raycast AI

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### Other MCP clients

Most MCP clients support URL-based configuration. If your client supports OAuth / MCP authorization, use the plain Dot MCP URL — that's it. Otherwise, follow [Using an API token](#using-an-api-token) and send the token in a header.

### Using an API token

Use a token when your client doesn't support OAuth or as a fallback if OAuth isn't working.

#### Generate a token

1. In Dot, open your **Profile** and scroll to **Use Dot elsewhere**
2. On the **MCP** tab, open **Client can't do OAuth? Use an API token**
3. Click **Generate token** and copy it immediately. You won't see it again

#### Apply the token

Depending on how your client accepts credentials, use one of these:

{% tabs %}
{% tab title="Header" %}
Send the token in an `X-API-KEY` header. That's how token auth works now, so use it anywhere your client lets you set request headers.

For Claude Code, pass the header on the add command:

```bash
claude mcp add --transport http dot https://app.getdot.ai/ai/mcp --header "X-API-KEY: YOUR_TOKEN"
```

If your client only takes a plain URL and can't set headers, use OAuth instead (see the top of this page). Putting the token in the URL is no longer supported.
{% endtab %}

{% tab title="JSON config (Cursor, etc.)" %}
For clients that accept an MCP server block:

1. In Cursor, go to **Settings → Tools & Integration → Add new MCP Server** to open `mcp.json`
2. Generate a token on the **MCP** tab in Dot (see above), which shows the URL and header to use
3. Add to `mcpServers`:

```json
{
  "mcpServers": {
    "dot": {
      "url": "https://app.getdot.ai/ai/mcp",
      "headers": {
        "X-API-KEY": "<your-dot-mcp-api-key>"
      }
    }
  }
}
```
{% endtab %}

{% endtabs %}

#### Token management

* **Special MCP token with limited scope** — separate from regular API tokens
* **One active token per user** — generating a new token revokes the previous one
* **365-day expiry** — tokens expire after one year
* **Immediate revocation** — admins can delete tokens anytime via the UI

### Charts and apps inside your assistant

Hosts that support MCP Apps, such as Claude, show Dot's answers as a card in the conversation: the charts and tables, drawn the way Dot draws them. When you ask to see a Dot app (a dashboard or report), the assistant opens it live in the conversation. Ask "what apps do I have?" and the assistant lists the ones you can open. Text-only clients such as Claude Code and Codex get the text answer, data preview and links.

### Asking questions

Once configured, you can ask your AI assistant questions about your data:

* "What were total sales last quarter?"
* "Show me top 10 customers by revenue"
* "Compare this month's performance to last month"
* "What data sources are available?"

### Security

#### OAuth sessions

* OAuth uses industry-standard **OAuth 2.1 with PKCE** for secure authorization
* Access tokens expire after **1 hour** and are automatically refreshed
* Refresh tokens are valid for **1 year** — after that, re-authentication is required
* To end MCP access, disconnect or remove Dot in your client, which revokes that session, or delete your MCP token in Settings. Note that changing your Dot password does not revoke existing MCP connections on its own
* The consent page shows exactly which permissions the client is requesting before you approve

#### Data access

* MCP respects all your Dot permissions and has the same data permissions as the user
* Queries run within your organization's scope and user scope
* All data filtering rules are enforced
* All queries are logged for compliance

### Troubleshooting

#### OAuth issues

**Browser doesn't open for authentication**

* Ensure your AI client is up to date
* Try the token-based method as a fallback
* Check that your browser isn't blocking pop-ups from Dot

**"Authorization session expired" error**

* The connection request lasts 30 minutes. Start connecting again from your app
* If your Dot account is in the other region, connect that region's URL instead (see [Your Dot MCP URL](#your-dot-mcp-url))

#### Token issues

**"Invalid API token" error**

* Verify you copied the complete token
* Check if token was revoked or replaced
* Ensure you're using the correct Dot URL

**"Token does not have required MCP access" error**

* Generate a new MCP token from your Profile, under Use Dot elsewhere
* Ensure you're not using a regular API token

#### Connection issues

**Connection timeout**

* Check network connection to Dot
* Verify the Dot instance URL is correct
* Some clients have a tool timeout setting — adjust it accordingly

### Connect other MCP servers to Dot

This is the other direction: you give Dot tools from a remote MCP server so it can use them while answering. Admins set this up under **Settings → Connections**, in **Context Connectors**, on the **MCP server** card. It is in beta, and servers that only sign in with OAuth aren't supported yet.

1. Enter a **Name**, a **Slug** (lowercase letters, digits and underscores), the server's **URL** (it must start with `https://`) and a **Description**. The description tells Dot when to use the server.
2. If the server needs a key, add the **Auth header** name and its **Value**.
3. Click **Save**. Dot loads the server's tools. A server it can't reach isn't saved.

Tools the server declares read-only start switched on. Dot can't enable a tool that can change data. If you know a tool only reads, choose **Mark read-only** next to it first. Use **Refresh tools** to pick up changes. A tool whose definition changed turns off until you review it and switch it back on.
