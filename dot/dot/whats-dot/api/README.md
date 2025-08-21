---
description: automate as much as you like
---

# API

## Everything starts with a token of trust

All API endpoints can be accessed via an API token that is tied to the permissions of a user account. You can also let them expire after some time.

### How to get a token?

1. Go to **Settings / Users**
2. Click **Create New Token**

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

3. **Enter a name**, description, and expiration period
4. **Copy the token** (it's only shown once)



### How to use the token?

You have two ways. You either pass the token as a header with `API-KEY` or you pass it as a url parameter  in `api_token` . As a header is usually more secure because automated loggers don't store them, but in some places you can't set headers (e.g. dbt webhooks) and then you can use the URL parameter.

#### Via Headers

Call the user endpoint via command line interface.

```bash
# Basic API request with token
curl -H "API-KEY: dot-your_token_here" <https://[app or eu].getdot.ai/api/auth/me>
```

Call the user endpoint via Python.

```python
import requests
headers = {"API-KEY": "dot-your_token_here"}
response = requests.get("https://[app or eu].getdot.ai/api/auth/me", headers=headers)
```

#### Via URL - Parameters

For the following endpoints you can also use a URL based authentication:

* Sync connection
* Import external asserts
* Export conversation history

Call the endpoint only via url:

```bash
curl "https://{region}.getdot.ai/api/sync/{connection_type}/{connection_type}" \
     "?user_id={user}&api_token={api_token}"
```

## Learn More

{% content-ref url="commonly-used-endpoints.md" %}
[commonly-used-endpoints.md](commonly-used-endpoints.md)
{% endcontent-ref %}

{% content-ref url="use-cases-and-scripts.md" %}
[use-cases-and-scripts.md](use-cases-and-scripts.md)
{% endcontent-ref %}

{% content-ref url="all-api-endpoints.md" %}
[all-api-endpoints.md](all-api-endpoints.md)
{% endcontent-ref %}



