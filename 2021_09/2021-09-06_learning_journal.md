# Daily Learning Journal - 2021-09-06 - Monday

## Setting up Virtual Servers

[The Command Line](https://missing.csail.mit.edu/2020/course-shell/)

## Google Project Management: Professional Certificate

[Project Planing](https://www.coursera.org/learn/project-planning-google/home/)

## Typing Academy

Daily [typing lessons](https://www.typing.academy/typing-tutor/lessons)

## Dev Web Api

### Parameters for an API concept

- Data format. Support of JSON format
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
- Authentication
  - Bearer token: append the token value to the text "Bearer " to the request Authorization header
  - Basic Auth: the Authorization header is going to pass the API a Base64 encoded string representing username and password values, appended to the text "Basic "
- Usage policies
  - Rights and quotas for developers should be easy to understand and work with.

### Work on the Web Api

- [The Excuse Mongoose as Project](https://github.com/users/universalamateur/projects/2)
- Creating a more soffisticated Flask app: [Tutorial](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#what-is-an-api)
- [Flaks Api with Auth0](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
- [Postman Info page about api call authentification](https://learning.postman.com/docs/sending-requests/authorization/#bearer-token)
