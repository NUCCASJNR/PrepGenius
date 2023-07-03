# PrepGenius

PrepGenius is a web application for practice tests and exam preparation. It provides a platform for users to access questions, choose subjects, and track their scores. This repository contains the backend code and database structure for the PrepGenius application.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Structure](#database-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication: Users can register, login, and manage their accounts.
- Question management: Questions can be added, edited, and deleted from the database.
- Subject selection: Users can select subjects they want to practice and track their progress.
- Score tracking: Users' scores are recorded for each subject and overall.
- Options management: Options for each question can be added and marked as correct.

## Technologies Used

- Python
- Flask framework
- SQLAlchemy
- MySQL database

## Database Structure

The database structure consists of the following tables:

- **users**: Stores user information such as username, email, and password.
- **subjects**: Stores subject details, including subject name and description.
- **questions**: Contains question details, including the question text, subject ID, topic ID, explanation, and correct option ID.
- **options**: Stores options for each question, including the option text and question ID.
- **selected_subs**: Tracks the subjects selected by each user.

For a more detailed explanation of the tables and their relationships, please refer to the [database model section](#database-structure) in this repository.

## Installation

1. Clone the repository: `git clone https://github.com/NUCCASJNR/PrepGenius.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your MySQL database and configure the connection details in the Flask configuration file.
4. Run the Flask application: `flask run`

## Usage

1. Access the PrepGenius web application using a web browser.
2. Register a new account or log in with existing credentials.
3. Explore the available subjects and select the subjects you want to practice.
4. Access the questions and attempt them.
5. View your scores and progress for each subject and overall.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. For major changes, please discuss them in advance to ensure they align with the project's goals.

## License

This project is licensed under the [MIT License](LICENSE).
