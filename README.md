# PrepGenius

PrepGenius is a web application designed to help students prepare for their JAMB (Joint Admissions and Matriculation Board) exams by providing a comprehensive collection of past questions. The portal aims to assist students in familiarizing themselves with the exam format, testing their knowledge, and improving their performance.It provides access questions, choose subjects, and track their scores. This repository contains the backend code and database structure for the PrepGenius application.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Structure](#database-structure)
- [Table Creation](#table-creation)
- [Installation](#installation)
- [Usage](#usage)
- [API Routes](#API-Routes)
- [Contributing](#contributing)
- [Migrations](#migrations)
- [Work in progress](#Work-in-Progress)

## Features

- User authentication: Users can register, login, and manage their accounts.
- Question management: Questions can be added, edited, and deleted from the database.
- Subject selection: Users can select subjects they want to practice and track their progress.
- Score tracking: Users' scores are recorded for each subject and overall.
- Options management: Options for each question can be added and marked as correct.

## Technologies Used

- Python
- Flask framework
- Flask-SQLAlchemy
- MySQL database

## Database Structure

The database structure consists of the following tables:

- **users**: Stores user information such as username, email, and password.
- **subjects**: Stores subject details, including subject name and description.
- **questions**: Contains question details, including the question text, subject ID, topic ID, explanation, and correct option ID.
- **options**: Stores options for each question, including the option text and question ID.
- **selected_subs**: Tracks the subjects selected by each user.

For a more detailed explanation of the tables and their relationships, please refer to the [database model section](#database-structure) in this repository.

## Table Creation

To create the necessary tables in the database, follow these steps:

1. Set up your MySQL database and configure the connection details in the Flask configuration file.
2. Open a terminal and navigate to the project directory.
3. Open the python interpreter and Run the following command to create the tables:

```bash
from models.base_model import BaseModel, app, db
with app.app_context():
    db.create_all()
```

## Installation

1. Clone the repository: `git clone https://github.com/NUCCASJNR/PrepGenius.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your MySQL database and configure the connection details in the Flask configuration file.
5. `cd PrepGenius`
4. Run the Flask application: `python3 -m api.app`

## Usage

1. Access the PrepGenius web application using a web browser.
2. Register a new account or log in with existing credentials.
3. Explore the available subjects and select the subjects you want to practice.
4. Access the questions and attempt them.
5. View your scores and progress for each subject and overall.

## API Routes
The following API routes are available in the PrepGenius application:

- Subjects
1. GET /api/subjects - Retrieve all subjects.

```bash
http http://127.0.0.1:5000/api/subjects
HTTP/1.1 200 OK
Connection: close
Content-Length: 375
Content-Type: application/json
Date: Mon, 10 Jul 2023 11:41:42 GMT
Server: Werkzeug/2.3.4 Python/3.10.6

[
    {
        "created_at": "Sun, 09 Jul 2023 23:39:41 GMT",
        "id": "3a07fd25-1b15-4c49-9540-3ed07f38389a",
        "name": "maths",
        "updated_at": "Sun, 09 Jul 2023 23:39:41 GMT"
    },
    {
        "created_at": "Sun, 09 Jul 2023 23:36:42 GMT",
        "id": "c96ad9ac-be26-4710-a0cf-7602b1833d33",
        "name": "english studies",
        "updated_at": "Mon, 10 Jul 2023 12:09:28 GMT"
    }
]
```

2. GET /api/subjects/{subject_id} - Retrieve a specific subject by ID.
```bash
 http http://127.0.0.1:5000/api/subjects/3a07fd25-1b15-4c49-9540-3ed07f38389a
HTTP/1.1 200 OK
Connection: close
Content-Length: 168
Content-Type: application/json
Date: Mon, 10 Jul 2023 11:44:51 GMT
Server: Werkzeug/2.3.4 Python/3.10.6

{
    "created_at": "Sun, 09 Jul 2023 23:39:41 GMT",
    "id": "3a07fd25-1b15-4c49-9540-3ed07f38389a",
    "name": "maths",
    "updated_at": "Sun, 09 Jul 2023 23:39:41 GMT"
}
```

3. POST /api/subjects - Create a new subject.

```bash
alareef@codewithalareef:~/PrepGenius$ http POST http://127.0.0.1:5000/api/subjects name=physics -vvv
POST /api/subjects HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 19
Content-Type: application/json
Host: 127.0.0.1:5000
User-Agent: HTTPie/2.6.0

{
    "name": "physics"
}


HTTP/1.1 201 CREATED
Connection: close
Content-Length: 170
Content-Type: application/json
Date: Mon, 10 Jul 2023 11:47:34 GMT
Server: Werkzeug/2.3.4 Python/3.10.6

{
    "created_at": "Mon, 10 Jul 2023 12:47:34 GMT",
    "id": "0ef32d79-5e92-4bdb-aea7-d61817028eb7",
    "name": "physics",
    "updated_at": "Mon, 10 Jul 2023 12:47:34 GMT"
}
```

4. PUT /api/subjects/{subject_id} - Update a subject by ID.
```bash
http PUT http://127.0.0.1:5000/api/subjects/0ef32d79-5e92-4bdb-aea7-d61817028eb7 name=chemistry -vvv
PUT /api/subjects/0ef32d79-5e92-4bdb-aea7-d61817028eb7 HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 21
Content-Type: application/json
Host: 127.0.0.1:5000
User-Agent: HTTPie/2.6.0

{
    "name": "chemistry"
}


HTTP/1.1 200 OK
Connection: close
Content-Length: 172
Content-Type: application/json
Date: Mon, 10 Jul 2023 11:49:35 GMT
Server: Werkzeug/2.3.4 Python/3.10.6

{
    "created_at": "Mon, 10 Jul 2023 12:47:34 GMT",
    "id": "0ef32d79-5e92-4bdb-aea7-d61817028eb7",
    "name": "chemistry",
    "updated_at": "Mon, 10 Jul 2023 12:49:35 GMT"
}
```

5. DELETE /api/subjects/{subject_id} - Delete a subject by ID.

```bash
 http DELETE http://127.0.0.1:5000/api/subjects/0ef32d79-5e92-4bdb-aea7-d61817028eb7 
HTTP/1.1 200 OK
Connection: close
Content-Length: 3
Content-Type: application/json
Date: Mon, 10 Jul 2023 11:50:28 GMT
Server: Werkzeug/2.3.4 Python/3.10.6

{}
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. For major changes, please discuss them in advance to ensure they align with the project's goals.

## Migrations

To set up the database structure, follow these steps:

1. Make sure you have the necessary database connection details configured in the Flask configuration file.
2. Open a terminal and navigate to the `api` directory in the project directory where we have the `app.py`.
```bash
cd PrepGenius/api
```
3. Run the following commands to apply the database migrations:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Work in Progress

This project is actively being developed, and the following features are currently in progress:

- Integration with external API for data retrieval
- Implementing user authentication and authorization
- Enhancing the user interface and adding interactive elements
- Adding support for additional languages

Please note that these features are subject to change and may be updated as the project progresses. Contributions and suggestions are welcome!
