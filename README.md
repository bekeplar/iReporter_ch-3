# iReporter

 iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

[![Build Status](https://travis-ci.org/bekeplar/iReporter.svg?branch=develop)](https://travis-ci.org/bekeplar/iReporter)
[![Coverage Status](https://coveralls.io/repos/github/bekeplar/iReporter_ch-3/badge.svg?branch=develop)](https://coveralls.io/github/bekeplar/iReporter_ch-3?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/6042069fde009728cd76/maintainability)](https://codeclimate.com/github/bekeplar/iReporter_ch-3/maintainability)

## Required features

- Users can create an account and log in.
- Users can create a ​red-flag ​​record (An incident linked to corruption).
- Users can create ​intervention​​ record​ ​​(a call for a government agency to intervene e.g  repair bad road sections, collapsed bridges, flooding e.t.c).
- Users can edit their ​red-flag ​​or ​intervention ​​records.
- Users can delete their ​red-flag ​​or ​intervention ​​records.  
- Users can add geolocation (Lat Long Coordinates) to their ​red-flag ​​or ​intervention  records​.  Users can change the geolocation (Lat Long Coordinates) attached to their ​red-flag ​​or  intervention ​​records​.
- Admin can change the ​status​​ of a record to either ​under investigation, rejected ​​(in the  event of a false claim)​ ​​or​ resolved ​​(in the event that the claim has been investigated and  resolved)​.

## Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|api/v1/auth/signup|create a new user
POST|api/vi/auth/login|Login a user
POST|api/v1/redflags|Create a redflag resource
GET|api/v1/redflags|Fetch all redflags reported
GET|api/v1/redflags/<redflag_id>|Fetch a specific redflag record
DELETE|api/v1/redflags/<int:redflag_id>|Delete a specific redflag
PATCH|api/v1/redflags/<int:redflag_id>/location|Edit location of a specific redflag
PATCH|api/v1/redflags/<int:redflag_id>/comment|Edit a comment of a specific redflag
PATCH|api/v1/redflags/<int:redflag_id>/status|Edit status of a specific redflag
POST|api/v1/interventions|Create an intervention resource
GET|api/v1/interventions|Fetch all interventions reported
GET|api/v1/interventions/<intervention_id>|Fetch a specific intervention record
DELETE|api/v1/interventions/<int:intervention_id>|Delete a specific redflag
PATCH|api/v1/interventions/<int:intervention_id>/location|Edit location of a specific interventions
PATCH|api/v1/interventions/<int:redflag_id>/comment|Edit a comment of a specific redflag
PATCH|api/v1/redflags/<int:redflag_id>/status|Edit status of a specific redflag

## Requirements

- Python
- Flask
- Virtualenv
- Postman

## Getting started

- Clone the project to your local machine

```git clone https://github.com/bekeplar/iReporter.git
```

- Change to the cloned directory

```cd iReporter
pip install virtualenv
source venv/bin/activate
git checkout develop
pip install -r requirements.txt
python run.py
```

- For those on windows

```cd iReporter
python -m venv venv
or
pip install virtualenv
venv\Scripts\activate
```

- Run tests by

```- pytest
   - pytest --cov
   - pytest -v

```

- Testing Endpoints

```copy the url in the terminal
paste it in postman
Use the following sample data

redflag = [
    {
        "createdBy":1,
        "type":"redflag",
        "title":"corruption",
        "location":"1.33, 2.045",
        "comment":"corrupt trffic officers in mukono",
        "status":"draft",
        "images":"nn.jpg",
        "videos":"nn.mp4"
    }
]

intervention = [
    {
        "createdBy":1,
        "type":"intervention",
        "title":"Bribery",
        "location":"1.33, 2.045",
        "comment":"There is no medicine in Health centre IV",
        "status":"draft",
        "images":"nn.jpg"
    }
]

user = [
    {
        "firstname":"bekelaze",
        "lastname":"Joseph",
        "othernames":"beka",
        "email":"bekeplar@gmail.com",
        "phoneNumber":"0789057968",
        "username":"bekeplar",
        "isAdmin":"False",
        "password":"bekeplar1234"
    }
]
```

## Hosting link

```https://kepireporter.herokuapp.com/
```

## Authors

Bekalaze Joseph

### Courtesy of

Andela Uganda
