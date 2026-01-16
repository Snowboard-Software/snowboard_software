---
description: Separate environments for different teams
---

# Workspaces

Workspaces are isolated environments within your organization—separate users, data connections, and permissions, but shared billing.

**Use cases**: Team separation (Sales vs Finance), client isolation, regional data separation, testing environments.

### Creating a Workspace

*Org admins only*

1. **Settings → Workspaces → Create Workspace**
2. Enter a name, optionally copy data from another workspace
3. Done

Limits: 10 workspaces (free) / 200 (unlimited).

### Switching Workspaces

Click your **workspace name** (top-left) → select another workspace.

You can set a default workspace in your user settings.

### Adding Users

1. **Settings → Workspaces** → find workspace → **Manage Users**
2. Enter email, select role (User/Admin), click Add

New users invited to a workspace can only see that workspace. Admins can grant full org access later.

### Slack & Teams Routing

Route specific channels to workspaces. See [Channel Routing](../integrations/slack-and-teams/channel-routing.md).
