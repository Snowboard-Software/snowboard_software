---
description: Authenticate with your existing identity provider
---

# Single Sign-On

Sled supports Single Sign-On (SSO), allowing your users to authenticate using their existing identity provider credentials instead of managing separate passwords.

## Supported Providers

* [Azure Active Directory](azure-active-directory.md) - Microsoft Entra ID (OAuth 2.0 / OpenID Connect)

## How SSO Works in Sled

When SSO is enabled, users see a **"Sign in with Microsoft"** button on the login page. Clicking it redirects them to your identity provider for authentication. After successful login, users are automatically created in Sled and assigned a role based on their group memberships.

### Key Features

* **Automatic user provisioning** - Users are created in Sled on first login, no manual setup needed
* **Group-based access control** - Map identity provider groups to Sled roles (Admin, Editor, Viewer)
* **Default viewer access** - All authenticated users get read-only access without any extra configuration
* **MFA support** - Works with your identity provider's Multi-Factor Authentication policies
* **Optional password fallback** - Keep password login enabled alongside SSO during transition
