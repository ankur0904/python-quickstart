from novu.config import NovuConfig
from novu.api import EventApi
from novu.api.subscriber import SubscriberApi
from novu.dto.subscriber import SubscriberDto
NovuConfig().configure("https://api.novu.co", "b23c55928da9e76702b74921a7fffee2")

# Create a subscriber
# This will create a subscriber with the given subscriber_id, email, first_name and last_name
# check here: https://web.novu.co/subscribers

your_subscriber_id = "123" # Replace this with a unique user ID

subscriber = SubscriberApi("https://api.novu.co", "b23c55928da9e76702b74921a7fffee2")
subscriber.create(SubscriberDto(
        subscriber_id=your_subscriber_id,
        email="abc@gmail.com",
        first_name="John",
        last_name="Doe"
    )
)

# Update subscriber detail
# This will update the subscriber detail in this case we are changing the email, first_name and last_name
# Link: https://web.novu.co/subscribers

subscriber = SubscriberApi("https://api.novu.co", "b23c55928da9e76702b74921a7fffee2")
subscriber.put(subscriber=SubscriberDto(
        subscriber_id="123",   # you want update on this id
        email="abcde@gmail.com",
        first_name="New",
        last_name="Name"
))


# Trigger the notification
EventApi().trigger(
    name="test",  # The trigger ID of workflow name. It can be found on the workflow page.
    recipients="123",
    payload={},  # Your Novu payload goes here
)


print("Done")