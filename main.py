from novu.config import NovuConfig
from novu.api import EventApi
from novu.api.subscriber import SubscriberApi
from novu.dto.subscriber import SubscriberDto
NovuConfig().configure("https://api.novu.co", "<YOUR_NOVU_API_KEY>")

# Create a subscriber
# This will create a subscriber with the given subscriber_id, email, first_name and last_name

your_subscriber_id = "<ID>" # Replace <ID> with a unique userID

subscriber = SubscriberApi("https://api.novu.co", "<YOUR_NOVU_API_KEY>")
subscriber.create(SubscriberDto(
        subscriber_id=your_subscriber_id,
        email="<Email>",
        first_name="John",
        last_name="Doe"
    )
)

# Update subscriber detail
# This will update the subscriber detail. In this case we are changing the email, first_name and last_name

subscriber = SubscriberApi("https://api.novu.co", "<YOUR_NOVU_API_KEY>")
subscriber.put(subscriber=SubscriberDto(
        subscriber_id="<ID>",   # you want update on this id
        email="<New_Updated_Email>",
        first_name="New",
        last_name="Name"
))


# Trigger the notification
EventApi().trigger(
    name="<trigger_ID>",  # The trigger ID of workflow name. It can be found on the workflow page.
    recipients="<ID>",
    payload={},  # Your Novu payload goes here
)


print("Done")