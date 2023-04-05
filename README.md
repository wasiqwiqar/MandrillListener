# Welcome to the Mandrill Listener repository!
This is a simple listener that will listen for Mandrill events and then store them in a database.

* No authentication is required to view the events, permission classes were not used but can be added if required.

## How to run
1. Clone the repository
2. Create a virtual environment, on Windows: `py -m venv venv`
3. Activate the virtual environment, on Windows: `venv\Scripts\activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Navigate to the Listener folder: `cd listener`
6. Run the migrations: `py manage.py migrate`
7. Start the server: `py manage.py runserver`

## Tools used
<!-- django, vue cdn, axios, tailwind -->
* **Django** - Python web framework, used Django REST Framework for the API
* **Axios** - Javascript library for making HTTP requests
* **Vue CDN** - Javascript framework, did not need to use the full Vue CLI
* **Tailwind CDN** - For quick and easy styling
* **Django Channels** - For sending notifications through the websockets
* **SQLite 3** - To keep it simple, we can use `PostgreSQL` or `MySQL` in production.

### JSONField
This project makes use of `JSONField` which is only supported in `PostgreSQL` and newer versions of `SQLite` & `MySQL`. 

* We can switch to a generic `TextField` if the existing infrastructure does not support `JSONField`.

### Redis
Currently using an in-memory cache for the notifications, `redis` can be used too but that would require `Docker` and would overcomplicate the task at hand. Would use `redis` in production.

## Features
* Listens for Mandrill events
* Stores the events in a database
* Displays the events in a list on the frontend home page
* Can simulate responses from Mandrill using the API Endpoint `/webhook/`
* Sends a notification to all connected users when a new event with type `open` is received
* Used Django Channels to send the notifications through websockets
* It is possible to send notifications to other users as well through the same websocket connection
  * Currently simulated through the "Test" button on the home page

## What I would add
* User authentication before they can view the events.
* Pagination for the events
* Mandrill's validation system to ensure that the events are coming from Mandrill.
* An error handling and logging system to store failed events and messages in a separate table.
* Database storage for the notifications that are sent to users, implemented asynchrnously.
* Automatically fetching new events from the database and displaying them on the frontend on notification.

## Expected Mandrill Event Format:
```json
{
   "mandrill_events":[
      {
         "event":"send",
         "msg":{
            "_id":"d1dasd12"
         }
      }
   ]
}
```

## Current paths
By default the server will on `127.0.0.1:8000`

* `/` - Home page - Displays the events & notifications
* `/webhook/` - API Endpoint - GET - Provides a list of events
* `/webhook/` - API Endpoint - POST - Receives events from Mandrill

If you want to test the API Endpoint, you can visit `/webhook/` and scroll to the bottom for the ability to send `Raw JSON` data to the endpoint.
