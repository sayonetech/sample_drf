---
title: ARRIVE REST API
---
You can use the ARRIVE REST API with the [ARRIVE SDK](https://developer.curbside.com/docs/) to manage the lifecycle of trips.
This documentation describes common use cases such as:
 * [Cancelling or completing a trip](#cancelling-or-completing-a-trip)
 * [Confirming that a user arrived](#confirming-that-a-user-arrived)
 * [Retrieving sites near a location](#retrieving-sites-near-a-location)
## Sign up for the Curbside Platform
To access the ARRIVE REST API, you must [sign up](https://dashboard.curbside.com/signup) for the Curbside Platform.
It is also recommended that you read the [Quick Start for iOS App](/docs/getting-started/quickstart-ios-app/) or the [Quick Start for Android App](/docs/getting-started/quickstart-android-app/) before integrating the ARRIVE REST API.
## Create a Usage Token
Once you are logged in, you can [create a usage token](https://dashboard.curbside.com/account?accessTab=tokens&accountTab=access).
When you are ready to move your app into production, create a separate usage token for production by checking the `Production` checkbox when creating it.
## Requests
The ARRIVE REST API accepts JSON in the HTTP request body.
All requests are handled over HTTPS.
Some requests require an `app-id`. If you are sending requests to the ARRIVE REST API from arrive.example.com, you can create an App ID such as arrive.example.com
Requests must be sent to the `https://api.curbside.com/plt/ad/2017-05-31/notify` endpoint.

### <a name="cancelling-or-completing-a-trip"></a>Cancelling or Completing a Trips
Cancelling trips through the ARRIVE REST API is necessary when the trip cannot
be fulfilled. For example, in a retail scenario, a trip might need to be
cancelled when an order is cancelled due to an out-of-stock event.
Note that if a notify request contains instructions to both cancel and complete
a trip, the completion will have precedence.
