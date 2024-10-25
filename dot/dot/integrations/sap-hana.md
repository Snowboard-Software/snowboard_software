---
description: Easily talk to your "Systems, Applications, and Products" In-Memory database
---

# SAP HANA

### Create a role and a user for Dot <a href="#create-a-role-and-a-user-for-dot" id="create-a-role-and-a-user-for-dot"></a>

Create a dedicated user and role for Dot to access SAP HANA Cloud tables. Replace `<schema_name>`, `<table_name>` with the name of your schema and tables.

```sql
SET SCHEMA <schema_name>
CREATE USER DOT_USER
CREATE ROLE DOT_ROLE
GRANT SELECT ON SCHEMA <schema_name> TO DOT_ROLE
GRANT DOT_ROLE TO DOT_USER
```

It is recommended to grant permissions only to tables your end-users should have access to. These typically include core business tables and reporting tables.

If you need to grant access to a particular table, run the following command:

```sql
GRANT SELECT ON <schema_name>.<table_name> TO <user_or_role>
```

### How to connect to the free SAP HANA Cloud instance <a href="#how-to-connect-to-the-free-sap-hana-cloud-instance" id="how-to-connect-to-the-free-sap-hana-cloud-instance"></a>

1. Sign-in to the SAP BTP Cockpit with your credentials
2. Select your subaccount under the account explorer
3. Select your space under Cloud Foundry -> Spaces
4. Select **SAP HANA Cloud** on the left panel
5. Open **SAP HANA Cloud Central**, check the current status of the SAP HANA instance.&#x20;

For more info on how to start with the SAP HANA free instance check out: [Provision an Instance of SAP HANA Cloud, SAP HANA Database](https://developers.sap.com/tutorials/hana-cloud-mission-trial-3.html).



### Allow Dot IPs: <a href="#allow-dot-ips" id="allow-dot-ips"></a>

To connect your SAP HANA Cloud instance with Dot, configure it to allow Dot to access it through the following IPs.

* 3.229.110.216
* 3.122.135.165
