# Welcome to the Mandrill Listener repository!
This is a simple listener that will listen for Mandrill events and then store them in a database.

## Tools used
<!-- django, vue cdn, axios, tailwind -->
* **Django** - Python web framework, used Django REST Framework for the API
* **Vue CDN** - Javascript framework, did not need to use the full Vue CLI
* **Axios** - Javascript library for making HTTP requests
* **Tailwind CDN** - For quick and easy styling
* **Django Channels** - For sending notifications through the websockets

## Features
* Listens for Mandrill events
* Stores the events in a database
* Displays the events in a list on the frontend home page
* Can simulate responses from Mandrill using the API Endpoint `/webhook/`
* Sends a notification to all connected users when a new event is received
* Used Django Channels to send the notifications through websockets
* It is possible to send notifications to other users as well through the same websocket connection
  * Currently simulated through the "test" button on the home page

## What I would add
* User authentication before they can view the events.
* Mandrill's validation system to ensure that the events are coming from Mandrill.
* An error handling and logging system to store failed events and messages in a separate table.
* Database storage for the notifications that are sent to users, implemented asynchrnously.
* Automatically fetching new events from the database and displaying them on the frontend on notification.

## Response Format:
```json
{
    mandrill_events: [ // Array of events
        {
            "event": "send", // Event type
            "msg": {
                    "_id": "5f7b1c0f0c5d4c0c8c1c1c1c", // Unique ID for this event
        }
    ],
}
```

## How to run
1. Clone the repository
2. Create a virtual environment, on Windows: `py -m venv venv`
3. Install the requirements: `pip install -r requirements.txt`
4. Navigate to the Listener folder: `cd listener`
5. Run the migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

