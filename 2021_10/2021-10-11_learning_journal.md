# Daily Learning Journal - 2021-10-11 - Monday

## Google Project Management: Professional Certificate

[PM Capstone](https://www.coursera.org/learn/applying-project-management/home/welcome)

## Typing Academy

Daily [typing lessons](https://www.typing.academy/typing-tutor/lessons)

## Greek Language

[DuoLingo greek](https://www.duolingo.com/learn)

## Flask Webpage

[Flask for web apss](https://www.youtube.com/playlist?list=PL-v3vdeWVEsUDDWYgZ8ImfSORIHyrsBJy)
[Flask Qucik start](https://flask.palletsprojects.com/en/2.0.x/quickstart/#static-files)

## Dev Web Api

HTTP Verb | URL Path | Purpose | Possible Parameter
------------ | ------------- | ------------- | -------------
GET | /excuses | List all possible Excuses | Class (NSFW/SFW)
GET | /excuses/generator | Get one random Excuse | Class (NSFW/SFW), Name (String, blank)
GET | /excuses/intros | List all Intros in Excuses | Class (NSFW/SFW)
GET | /excuses/intros/:id | Show a specific Intro in Excuses | -
PUT/PATCH | /excuses/intros/:id | Update a specific Intro in Excuses | JSON Payload with contecnt (String) and CLass (NSFW/SFW)
DELETE | /excuses/intros/:id | Delete a specific Intro in Excuses | -
POST | /excuses/intros/new | Create a new Intro in Excuses | JSON Payload with contecnt (String) and CLass (NSFW/SFW)
GET | /excuses/scapegoats | List all Scapegoats in Excuses | Class (NSFW/SFW)
GET | /excuses/scapegoats/:id | Show a specific Scapegoat in Excuses | -
PUT/PATCH | /excuses/scapegoats/:id | Update a specific Scapegoat in Excuses | -
DELETE | /excuses/scapegoats/:id | Delete a specific Scapegoat in Excuses | -
POST | /excuses/scapegoats/new | Create a new Intro in Excuses | JSON Payload with contecnt (String) and CLass (NSFW/SFW)
GET | /excuses/delays | List all Delays in Excuses | Class (NSFW/SFW)
GET | /excuses/delays/:id | Show a specific Delay in Excuses | -
PUT/PATCH | /excuses/delays/:id | Update a specific Delay in Excuses | -
DELETE | /excuses/delays/:id | Delete a specific Delay in Excuses | -
POST | /excuses/delays/new | Create a new Intro in Excuses | JSON Payload with contecnt (String) and CLass (NSFW/SFW)

### Parameters for an API concept

- Data format:
  - Support of JSON format
- Method structure (CRUD)
  - Read - GET:
    - List Endpoint:
      - List all Entries
      - List Entries of one category
      - List Entries of one class
    - Get Endpoint:
      - Get an Excuse
      - Get a personalized Excuse
      - Get an Excuse of a class
      - Get a personalized Excuse of a class
  - Update - PUT/POST/PATCH:
    - Change an Entry
  - Create - POST/PUT:
    - Create an Entry
  - Delete - DELETE:
    - Delete an Entry
- Data model
  - class (SFW, NSFW, etc.)
  - content (The data)
  - order (Intros, Scapegoat, Delay)
  - Input id
  - Active <-> Not Active
- Authentication
  - Bearer token: append the token value to the text "Bearer " to the request Authorization header
  - Basic Auth: the Authorization header is going to pass the API a Base64 encoded string representing username and password values, appended to the text "Basic "
- Usage policies
  - Rights and quotas for developers should be easy to understand and work with.
