---
description: enable your customers to chat with data & visualize insights
---

# Embed

<figure><img src="../../.gitbook/assets/dot_embedded.png" alt=""><figcaption></figcaption></figure>

You can embed Dot directly in your web app via an Iframe and configure parts of the UI with the following parameters.

* **hideSideNavigation=true**
  * hides the complete left side navigation (default false)
* **hideHelp=true**
  * hides the little help dongle at the bottom right (default false)
* **hideShareButton=true**
  * hides the ability to share a conversation (default false)
* **hideTitle=true**
  * hides the title of a conversation (default false)
* **uiMode=dark**
  * specify either `dark` or `light` mode of the UI (default system)
* **hideExplanation=true**
  * hides full logs button & explanation tab
* **minimizeProgess=True**
  * only show 'thinking' as progess when waiting for an answer
* **primaryColor=%23c700c7**
  * styles important action elements (e.g. chat input + button) according the specified color
  * the color is a hex code with the url encoded #c700c7



**Full example url**

```
https://eu.getdot.ai?hideSideNavigation=true&hideHelp=true&hideShareButton=true&hideExplanation=true&minimizeProgess=True&primaryColor=%23c700c7
```



### Automatically login users

If you want to automatically login your users, you can pass the access\_token parameter into the url

* **access\_token=eyJhABCDE123456789IsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrb2xhFGHIJ67890bGVkLnNvIiwib3JnX2secret2xlZC5zbyIsImV4cCI6MdotKL09876H0.spR-XrXTtDOTP54321ZWWchwR0x\_S8W\_juPVh8k**

The token can be obtained per user using the [api/auth/token ](api.md#api-auth-token)endpoint.





Questions? Get [support.md](../support.md "mention")!