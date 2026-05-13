# Simple FastAPI App

## Setup instructions

Clone the repo. Navigate to the root of this project. lab_1
```bash
# Create/Activate virutal enviroment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

```bash
# Running the FastAPI server
uvicorn main:app --reload
```

- This will start a server at http://127.0.0.1:8000. If you navigate to this url you will see "Hello World"
- To see the /docs just add /docs to the end of the url. http://127.0.0.1:8000/docs

## Sample Curl Commands

```bash
# POST method
curl -i -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/users -d '{"name":"henry jones", "email":"henry@example.com"}'

# GET method
curl -i -X GET http://127.0.0.1:8000/users
```

## Sample JSON output
```bash
# POST method output
HTTP/1.1 201 Created
date: Wed, 13 May 2026 00:34:53 GMT
server: uvicorn
content-length: 57
content-type: application/json

{"id":3,"name":"henry jones","email":"henry@example.com"}

# GET method output
HTTP/1.1 200 OK
date: Wed, 13 May 2026 00:33:44 GMT
server: uvicorn
content-length: 59
content-type: application/json

[{"id":1,"name":"henry jones","email":"henry@example.com"}]
```

## Explaination:
- POST /users works by having the browser send a POST request with the correct formatted
JSON using pydantic to verify and cast the input. This user object is then assigned an auto-incrementing id and added to the mock database.
- The data is stored in memory on the device that is currently running the FastAPI server.
- This is not production ready because it stores data in memory. Which means if the server was to ever restart because you made changes, it was delete all data that was stored in memory. A database is better due to persistence and SQL queries. 