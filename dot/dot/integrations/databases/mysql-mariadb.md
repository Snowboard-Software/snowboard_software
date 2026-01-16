# MySQL / MariaDB

### Create a User and Assign Privileges

As a superuser, execute the following SQL commands to create a user and assign necessary privileges.

```sql
CREATE USER 'dot_user'@'%' IDENTIFIED BY '<something secret>';

CREATE ROLE 'dot_role';

GRANT 'dot_role' TO 'dot_user'@'%';
```

### Grant Read Access to Data

For each database (`database`), execute the following commands to grant read-only access.

```sql
GRANT USAGE ON `database`.* TO 'dot_role';
GRANT SELECT ON `database`.* TO 'dot_role';
```

**Note**: To programmatically generate these grant statements for all databases, you can use the following command. These commands still need to be executed.

```sql
SELECT 
    CONCAT(
        'GRANT USAGE ON `', schema_name, '`.* TO \'dot_role\';',
        '\nGRANT SELECT ON `', schema_name, '`.* TO \'dot_role\';'
    ) AS grant_statements
FROM information_schema.schemata
WHERE schema_name NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys');
```

### Allow Dot IPs

If your organization uses a firewall to manage MySQL access, Dot will only access your MySQL through the following IPs:

* `3.229.110.216`
* `3.122.135.165`
