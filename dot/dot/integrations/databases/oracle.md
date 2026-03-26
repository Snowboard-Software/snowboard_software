# Oracle Database

### Create a User

As a DBA or SYSDBA, create a dedicated read-only user for Dot.

```sql
CREATE USER dot_reader IDENTIFIED BY '<something secret>';
GRANT CREATE SESSION TO dot_reader;
```

### Grant Read Access to Data

For each schema you want Dot to access, grant SELECT on all tables.

```sql
BEGIN
  FOR t IN (SELECT table_name FROM all_tables WHERE owner = '<SCHEMA>') LOOP
    EXECUTE IMMEDIATE 'GRANT SELECT ON <SCHEMA>.' || t.table_name || ' TO dot_reader';
  END LOOP;
END;
/
```

**Note**: Replace `<SCHEMA>` with the schema/owner name (e.g. `HR`, `SALES`). Repeat for each schema you want to expose to Dot.

To also grant access to views:

```sql
BEGIN
  FOR v IN (SELECT view_name FROM all_views WHERE owner = '<SCHEMA>') LOOP
    EXECUTE IMMEDIATE 'GRANT SELECT ON <SCHEMA>.' || v.view_name || ' TO dot_reader';
  END LOOP;
END;
/
```

### Connection Details

In Dot, use these fields:

* **Host**: Your Oracle server hostname or IP address
* **Port**: `1521` (default Oracle listener port)
* **Service Name**: Your Oracle service name (e.g. `ORCL`, `XEPDB1`, `FREEPDB1`)
* **Username**: `dot_reader`
* **Password**: The password you set above

Dot connects directly using Oracle's TNS protocol (Thin mode) — no Oracle Client installation is required on the Dot side.

### Allow Dot IPs

If your organization uses a firewall to manage Oracle access, Dot will only access your database through the following IPs:

* `3.229.110.216`
* `3.122.135.165`
