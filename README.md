# Job Connect

## Description

Job Connect is a web application designed to connect job seekers with potential employers. The platform facilitates job searches, applications, and employer listings.

## Features

- **User Authentication:** Allows users to create accounts, log in, and manage their profiles.
- **Job Listings:** Displays available job openings with detailed descriptions.
- **Application Submission:** Enables job seekers to apply for listed jobs.
- **Employer Dashboard:** Provides employers with a platform to post job openings and manage applications.

## Tech Stack

### Backend Microservices:

#### Auth Service:

- Flask (Python)
- SQLAlchemy (for database ORM)
- JWT (for authentication)

#### Job Service:

- Flask (Python)
- SQLAlchemy (for database ORM)
- Redis (for caching)

#### Application Service:

- Flask (Python)
- SQLAlchemy (for database ORM)
- Redis (for caching)

#### Employer Service:

- Flask (Python)
- SQLAlchemy (for database ORM)
- Redis (for caching)

### Frontend:

- React
- Redux (for state management)
- Axios (for API interactions)
- React Router (for routing)

## Project Structure
```
job-connect/
|-- backend/
| |-- auth_service/
| | |-- app.py
| | |-- config.py
| | +-- ...
| |
| |-- job_service/
| | |-- app.py
| | |-- config.py
| | +-- ...
| |
| |-- application_service/
| | |-- app.py
| | |-- config.py
| | +-- ...
| |
| |-- employer_service/
| | |-- app.py
| | |-- config.py
| | +-- ...
| |
| +-- redis/
| | |-- redis.conf
| | +-- ...
| |
| +-- mysql/
| | |-- job_db.sql
| | +-- ...
|
+-- frontend/
| |-- public/
| |-- src/
| | +-- ...
|
+-- README.md

```

## Setup Instructions

### Backend Microservices

1. Clone the repository.
2. Navigate to each microservice directory (auth_service, job_service, application_service, employer_service).
3. Create and activate a virtual environment for each microservice.
4. Install dependencies from their respective requirements.txt.
5. Configure environment variables in their respective .env files.
6. Run each service individually (`python app.py` within each microservice directory).

### Frontend (React)

1. Navigate to the frontend directory.
2. Install dependencies (`npm install`).
3. Start the development server (`npm start`).

## Usage

### Backend Microservices

- Access the API endpoints of each microservice as needed.
- Utilize tools like Postman for interaction with each microservice's API.

### Frontend

- Access the React application at [http://localhost:3000](http://localhost:3000).
- Register/login as a user or explore available job listings.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

## Authour: Kamau Macharia