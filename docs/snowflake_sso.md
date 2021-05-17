Enabling SSO on Snowflake 
===========

## Automatic deployment

***~ 5 min to complete***

### Grant correct rights
You need to grant `CREATE INTEGRATION` to the Snowflake role of your configured Snowboard technical user.
If you have followed the setup procedure in this documentation you can add these rights with:
```sql
GRANT CREATE INTEGRATION ON ACCOUNT TO ROLE snowboard_role;
```

### Enable SSO
Logged into Snowboard as admin user, click the `Enable SSO Button` on the corresponding account on the Snowboard settings page.


## Manual deployment

***~ 15 min to complete***

You need an `ACCOUNTADMIN` user to follow this guide. 

### Create security integration
Create a custom security integration by running the following query. Replace {{origin}} with the domain and protocol your Snowboard installation is running and {{host_name}} with the Snowflake account name.
```sql
CREATE SECURITY INTEGRATION SNOWBOARD
                type = oauth
                enabled = true
                oauth_client = custom
                oauth_client_type='CONFIDENTIAL'
                OAUTH_ALLOW_NON_TLS_REDIRECT_URI = true
                oauth_redirect_uri='{{origin}}/api/auth/snowflake/callback/{{host_name}}';
```

### Add data to Snowboard
Logged into Snowboard as admin user, click the `Enable SSO Button` on the corresponding account on the Snowboard settings page.
You will get a warning that your user doesn't have correct rights to automatically enable SSO.

Enter the correct information from Snowflake by extracting the data from the following queries:
```sql
DESCRIBE SECURITY INTEGRATION SNOWBOARD;
```
This query conveys the data for:
- Authorization Endpoint
- Token Endpoint
- Redirect URI

```sql
SELECT  d:OAUTH_CLIENT_ID::text as OAUTH_CLIENT_ID, 
            d:OAUTH_CLIENT_SECRET::text as OAUTH_CLIENT_SECRET 
      FROM (SELECT parse_json(SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('SNOWBOARD')) as d);
```
This query conveys the data for:
- Client-ID
- Client Secret

After entering the correct information save the configuration by pressing the `Save Button`
