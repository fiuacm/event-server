# FIU ACM event-server

This is the FIU ACM's event-server
This program as of right now is an event-server that is an API that
accepts a .csv file and converts it into JSON and stores it in
a MongoDB instance and returns JSON in the following format.

Primary Maintainer: @ndneighbor (Angelo Saraceno)

As of right now, it is only a command line application- but in the
future we hope to extend it with a front end interface.

The program is written in Python 2.7 with the Flask framework, this will serve as the event backend
to show the capabilities of the Flask

# routes

## GET /events

Whenever this route is hit it will return JSON containing three events
in the following schema

```
{
  "event": id
	{
	  "title": "name"
	  "time": "time"
	  "day": month day
	  "month": "month"
	  "year": "year"
	  "description": string
	  "rsvp": func()
	}
}
```


## POST /events

When this route is hit, a new .csv file will be uploaded where the events will be pulled from- really useful if you don't want to drag and drop

The route needs a .csv as it's payload to send back a 200

Planned features
-Login Token
-Using the flask templating engine  
