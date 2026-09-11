---
description: enable your customers to chat with data & visualize insights
---

# Embed



<div align="left"><figure><img src="../../.gitbook/assets/embedd_dot.png" alt=""><figcaption></figcaption></figure></div>

You can embed Dot directly in your web app via an Iframe and configure parts of the UI with the following parameters. They are all optional.

* **hideProfile=true**
  * hides the Profile navigation item (default false)
* **hideAllFeatures=true**
  * hides all configurable navigation and optional chat controls by default; the core chat remains available (default false)
  * set an individual hide flag to `false` to expose that control, for example `hideFileUpload=false`
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
* **hideFileUpload=true**
  * hides the file upload button in the chat input (default false)
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
* **suggestedPrompt1=How+is+the+weather**
  * changes the first suggested prompt text to the url-encoded value
* **suggestedPrompt\[2-8]=How+is+the+weather**
  * changes the nth suggested prompt text to the url-encoded value. You can specify up to 8 suggested questions on the chat window.
* **scope=MYDB%2EMYSCHEMA%2EMYTABLE**
  * specify the id of the data source that should be used as a scope for Dot to answer questions
  * the value is url encoded, e.g. MYDB.MYSCHEMA.MYTABLE
  * if this is not specified Dot will search for the right data source to answer the question
* **extra=anything**
  * here you can store anything that should get returned by the conversation history (e.g. an embedded user id)
* **active\_groups=finance%2Csales**
  * restricts a users data access to the specified user groups
  * Use `%2C` to url-encode a `,` to specify multiple groups
  * Active groups are validated against the assigned groups of the user



### Start with optional controls hidden

Use `hideAllFeatures=true` to default all supported visibility flags to hidden. An explicit `false` enables a particular control; omitted or unrecognized values keep it hidden. Without this mode, existing defaults remain unchanged.

To show only New chat and the conversation list in the sidebar:

```text
https://eu.getdot.ai/?hideAllFeatures=true&hideSideNavigation=false&hideNewChat=false&hideChatHistory=false
```

Navigation flags: `hideSideNavigation`, `hideNewChat`, `hideApps`, `hideHistory`, `hideSchedules`, `hideModel`, `hideSettings`, `hideProfile`, and `hideChatHistory` (the conversation list and chat search). Showing a navigation item also requires `hideSideNavigation=false`.

Chat control flags: `hideHelp`, `hideTitle`, `hideShareButton`, `hideSuggestedQuestions`, `hideExplanation`, and `hideFileUpload`. These flags persist when navigating within the iframe. Presentation options such as colors, `uiMode`, `hideNativeLinks`, and `minimizeProgress` retain their independent behavior.

{% hint style="info" %}
Visibility flags customize the UI; they do not restrict API or direct URL access or grant permissions. Existing user permissions and workspace feature settings still apply. New optional controls must use the same visibility policy to remain hidden in this mode.
{% endhint %}

**Full example url**

```
https://eu.getdot.ai?hideSideNavigation=true&hideHelp=true&hideShareButton=true&hideExplanation=true&minimizeProgess=True&primaryColor=%23c700c7&chatPlaceHolderText=Ask%20AI
```



### Automatically login users

If you want to automatically login your users, you can pass the access\_token parameter into the url

* **access\_token=eyJhABCDE123456789IsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrb2xhFGHIJ67890bGVkLnNvIiwib3JnX2secret2xlZC5zbyIsImV4cCI6MdotKL09876H0.spR-XrXTtDOTP54321ZWWchwR0x\_S8W\_juPVh8k**

The token can be obtained per user using the [api/auth/embedded\_user\_login ](api/commonly-used-endpoints.md#automatically-authenticate-embedded-users)endpoint.



Questions? Get [support.md](../support.md "mention")!
