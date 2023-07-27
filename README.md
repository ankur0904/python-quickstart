## Quickstart Code
### Replace `<YOUR_NOVU_API_KEY>` with your **API Key**, `<ID>` with **Subscriber ID**
```python
from novu.config import NovuConfig
from novu.api import EventApi
from novu.api.subscriber import SubscriberApi
from novu.dto.subscriber import SubscriberDto
NovuConfig().configure("https://api.novu.co", "<YOUR_NOVU_API_KEY>")


your_subscriber_id = "<ID>" 

subscriber = SubscriberApi("https://api.novu.co", "<YOUR_NOVU_API_KEY>")
subscriber.create(SubscriberDto(
        subscriber_id=your_subscriber_id,
        email="<Email>",
        first_name="John",
        last_name="Doe"
    )
)


subscriber = SubscriberApi("https://api.novu.co", "<YOUR_NOVU_API_KEY>")
subscriber.put(subscriber=SubscriberDto(
        subscriber_id="<ID>",   # you want update on this id
        email="<New_Updated_Email>",
        first_name="New",
        last_name="Name"
))


EventApi().trigger(
    name="<trigger_ID>",  # The trigger ID of workflow name. It can be found on the workflow page.
    recipients="<ID>",
    payload={},  # Your Novu payload goes here
)


print("Done")
```