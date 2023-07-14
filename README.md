## Quickstart Code

```python
from novu.config import NovuConfig
from novu.api import EventApi
from novu.api.subscriber import SubscriberApi
from novu.dto.subscriber import SubscriberDto
NovuConfig().configure("https://api.novu.co", "b23c55928da9e76702b74921a7fffee2")



your_subscriber_id = "123"

subscriber = SubscriberApi("https://api.novu.co", "b23c55928da9e76702b74921a7fffee2")
subscriber.create(SubscriberDto(
        subscriber_id=your_subscriber_id,
        email="abc@gmail.com",
        first_name="John",
        last_name="Doe"
    )
)

subscriber = SubscriberApi("https://api.novu.co", "b23c55928da9e76702b74921a7fffee2")
subscriber.put(subscriber=SubscriberDto(
        subscriber_id="123",   # you want update on this id
        email="abcde@gmail.com",
        first_name="New",
        last_name="Name"
))



EventApi().trigger(
    name="test",
    recipients="123",
    payload={},
)
```