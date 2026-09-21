---
description: No more forgotten passwords
---

# Single Sign On

Let your team sign in to Dot with the account they already use at work. Dot works with [Okta](okta.md), [Azure Active Directory](azure-active-directory.md), [Google](google.md), and any provider that speaks [OpenID Connect](oidc.md). Each page walks through the setup for that provider.

Setting up a provider adds a way to sign in. It does not take the old ones away, so your users can still sign in with a password or an email link until you turn that off.

## Enforce Single Sign-On

Once your provider works, you can make it the only way into your workspace.

1. Finish the setup for at least one provider and save it. The setting stays hidden until a provider is active.
2. Go to **Settings → Advanced Settings → Access & Authentication**.
3. Turn on **Enforce Single Sign-On**.

Dot then refuses four things for everyone in the workspace:

* signing in with an email address and password
* signing in with an email link
* signing up with an email address and password
* resetting a password

You set this once for the organization. The setting does not appear inside a workspace.

{% hint style="warning" %}
**Enforcing SSO covers new sign-ins only.** It does not sign out people who are already signed in, and a session lasts up to 30 days. Personal API tokens keep working as well.

So when somebody leaves, use **Delete User** under **Settings → Users**. Deleting a person ends their sessions and revokes their tokens at once, whether or not you enforce SSO. If they belong to a workspace, Dot restricts them to that workspace instead of deleting them, so take them out of every workspace first.
{% endhint %}
