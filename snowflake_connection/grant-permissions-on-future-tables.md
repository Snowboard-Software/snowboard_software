# Grant permissions on future tables

The following code block grants future permission to the role `snowboard_role` on all future tables and views in a database. This is needed for older Snowflake installations that only support future grants on the schema level.&#x20;

```sql
EXECUTE IMMEDIATE $$
-- TODO CHANGE database_name
DECLARE
  database_name TEXT := 'EXAMPLE_DB';
  log_text TEXT;
  grant_statement TEXT;
  schema_name TEXT;
  res_schemas RESULTSET;
  res resultset;
BEGIN
  log_text := 'START - ';
  grant_statement := 'show schemas in database ' || :database_name;
  res_schemas := (EXECUTE IMMEDIATE :grant_statement);
  FOR record IN res_schemas DO
    IF (record."name" != 'INFORMATION_SCHEMA') THEN
      schema_name := :database_name || '.' || record."name";
      grant_statement := 'grant select, references on future tables in schema ' || schema_name || ' to role snowboard_role; ';
      res := (EXECUTE IMMEDIATE :grant_statement);
      grant_statement := 'grant select, references on future views in schema ' || schema_name || ' to role snowboard_role; ';
      res := (EXECUTE IMMEDIATE :grant_statement);
      log_text := log_text || record."name" || ' GRANTED - ';
    END IF;
  END FOR;
  RETURN log_text;
END;
$$;

```
