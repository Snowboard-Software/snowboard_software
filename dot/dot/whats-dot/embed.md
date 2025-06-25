---
description: enable your customers to chat with data & visualize insights
---

# Embed



<div align="left"><figure><img src="../../.gitbook/assets/embedd_dot.png" alt=""><figcaption></figcaption></figure></div>

You can embed Dot directly in your web app via an Iframe and configure parts of the UI with the following parameters. They are all optional.

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
* **minimizeProgress=true**
  * only show 'thinking' as progess when waiting for an answer
* **hideNativeLinks=true**
  * will convert html links to javascript links, so users can't open a new tab accidentally
* **primaryColor=%23c700c7**
  * styles important action elements (e.g. chat input + button) according the specified color
  * the color is a hex code with the url encoded #c700c7
* **sideNavigationBackgroundColor=%23ffdbff**
  * styles the background color of the side navigation
* **chatInputBackgroundColor=%23ffdbff**
  * styles the background color of the chat input field
* **chatBackgroundColor=%23ffe6ff**
  * sets the background of the chat window
* **chatPlaceHolderText=Ask%20AI**
  * changes the placeholder text in the chat input field
  * default value is "Ask Dot about your data..."
* **scope=MYDB%2EMYSCHEMA%2EMYTABLE**
  * specify the id of the data source that should be used as a scope for Dot to answer questions
  * the value is url encoded, e.g. MYDB.MYSCHEMA.MYTABLE
  * if this is not specified Dot will search for the right data source to answer the question



**Full example url**

```
https://eu.getdot.ai?hideSideNavigation=true&hideHelp=true&hideShareButton=true&hideExplanation=true&minimizeProgess=True&primaryColor=%23c700c7&chatPlaceHolderText=Ask%20AI
```



### Automatically login users

If you want to automatically login your users, you can pass the access\_token parameter into the url

* **access\_token=eyJhABCDE123456789IsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrb2xhFGHIJ67890bGVkLnNvIiwib3JnX2secret2xlZC5zbyIsImV4cCI6MdotKL09876H0.spR-XrXTtDOTP54321ZWWchwR0x\_S8W\_juPVh8k**

The token can be obtained per user using the [api/auth/embedded\_user\_login ](api.md#api-auth-embedded_user_login)endpoint or via the [api/auth/token](api.md#api-auth-token) endpoint if you store the users password in your application.





Questions? Get [support.md](../support.md "mention")!
