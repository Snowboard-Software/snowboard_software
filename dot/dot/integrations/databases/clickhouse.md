# Clickhouse

Connect Dot to your ClickHouse database to query your data using natural language.

## Create a User for Dot

#### 1. Create a Dedicated User

Create a dedicated user for Dot with read-only access to your data:

```sql
-- Create a user for Dot
CREATE USER dot_user IDENTIFIED BY 'your_secure_password_here';

-- Grant read access to specific databases
GRANT SELECT ON database_name.* TO dot_user;

-- Or grant read access to all databases (if needed)
-- GRANT SELECT ON *.* TO dot_user;
```

#### 2. Grant Access to System Tables (Optional)

For enhanced query analytics and usage insights, grant access to system tables:

```sql
-- Grant access to query history for usage analytics
GRANT SELECT ON system.query_log TO dot_user;
GRANT SELECT ON system.tables TO dot_user;
GRANT SELECT ON system.columns TO dot_user;
GRANT SELECT ON system.databases TO dot_user;
```

This enables Dot to:

* Analyze table usage patterns
* Identify popular queries
* Provide performance optimization suggestions
* Show data lineage insights

## Connection Methods

### Option 1: Direct HTTP/HTTPS Connection (Recommended)

For most ClickHouse deployments, use the HTTP interface with SSL encryption:

**Required Connection Details:**

* **Host**: Your ClickHouse server hostname (e.g., `clickhouse.company.com`)
* **Port**: `8443` (HTTPS) or `8123` (HTTP - not recommended for production)
* **Username**: The user you created (e.g., `dot_user`)
* **Password**: The secure password you set
* **Database**: Your target database name (optional - can access all granted databases)
* **SSL**: Enable for production (`secure=true`)
* **Certificate Verification**: Enable unless using self-signed certificates

**Connection Example:**

```
Host: clickhouse.company.com
Port: 8443
Username: dot_user
Password: your_secure_password
Database: analytics_db
```

### Option 2: SSH Tunnel Connection

For databases behind firewalls or in private networks, use SSH tunneling:

**Required SSH Details:**

* **SSH Host**: Your bastion/jump server
* **SSH Port**: `22` (default) or custom SSH port
* **SSH Username**: Your SSH username
* **SSH Authentication**: Password or private key

**SSH Configuration Example:**

```
SSH Host: bastion.company.com
SSH Port: 22
SSH Username: your_ssh_user
SSH Authentication: Private Key
ClickHouse Host: internal-clickhouse.local
ClickHouse Port: 8443
```



## Dot IP Allowlist

If your ClickHouse server uses IP restrictions, add these Dot service IP addresses to your allowlist:

* `3.229.110.216`
* `3.122.135.165`

#### Port Requirements

**Standard Ports:**

* **Port 8443** (TCP) - HTTP interface with SSL/TLS (recommended)
* **Port 8123** (TCP) - HTTP interface without encryption (not recommended)
* **Port 9440** (TCP) - Native protocol with SSL/TLS
* **Port 9000** (TCP) - Native protocol without encryption

**SSH Tunnel Ports:**

* **Port 22** (TCP) - SSH for tunneling (if using SSH option)

