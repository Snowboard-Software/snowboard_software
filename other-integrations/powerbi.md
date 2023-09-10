# PowerBI



## PowerBI App Registration, Permission

Go to Azure AD App registration, add “New registration”

![](../.gitbook/assets/Untitled.png)

Default selection is fine, add a name

![](<../.gitbook/assets/Untitled 1.png>)

Write down Application (Client ID)

![](<../.gitbook/assets/Untitled 2.png>)

Add a client secret, change the duration to an appropriate amount. Client secret has to be recreated each time it runs out and must also be changed in Snowboard afterwards

![](<../.gitbook/assets/Untitled 3.png>)

Write down Value, this is the Client secret for Snowboard

![](<../.gitbook/assets/Untitled 4.png>)

Go to API permissions

![](<../.gitbook/assets/Untitled 5.png>)

```
Add “Application Permissions” → “Tenant.Read.All” 
Add “Application Permissions” → “Report.Read.All” 
Add “Application Permissions” → “Report.ReadWrite.All”
```

![](<../.gitbook/assets/Untitled 6.png>)

Grant admin consent

![](<../.gitbook/assets/Untitled 7.png>)

Get AzureAD Tenant ID ([https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant))

![](<../.gitbook/assets/Untitled 8.png>)

**Shouldn’t be necessary, but for completeness sake:** Go to [https://login.microsoftonline.com/{tenant-id}/adminconsent?client\_id={client-id](https://login.microsoftonline.com/%7Btenant-id%7D/adminconsent?client\_id={client-id)} and grant permissions

![](<../.gitbook/assets/Untitled 9.png>)

Today Admin endpoints needed

`https://api.powerbi.com/v1.0/myorg/admin/groups`

[https://learn.microsoft.com/en-us/rest/api/power-bi/admin/reports-get-reports-in-group-as-admin](https://learn.microsoft.com/en-us/rest/api/power-bi/admin/reports-get-reports-in-group-as-admin)
