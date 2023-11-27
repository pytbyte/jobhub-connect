# Job Connect

## Description

Job Connect is a web application designed to connect job seekers with potential employers. The platform facilitates job searches, applications, and employer listings.

## Features

- **User Authentication:** Allows users to create accounts, log in, and manage their profiles.
- **Job Listings:** Displays available job openings with detailed descriptions.
- **Application Submission:** Enables job seekers to apply for listed jobs.
- **Employer Dashboard:** Provides employers with a platform to post job openings and manage applications.

## Tech Stack

### Frontend:

- React
- Redux (for state management)
- Axios (for API interactions)
- React Router (for routing)

### Backend:

- Flask (Python)
- SQLAlchemy (for database ORM)
- Redis (for caching)
- JWT (for authentication)
- RESTful API architecture

## Project Structure

job-connect/
* backend/
 * app.py
 * models.py
 * controllers/
 * utils/
 * tests/
 * requirements.txt
 +-- .env.example

+-- frontend/
* public/
* src/
 * components/
 * containers/
 * actions/
 * reducers/
 * services/
 * App.js
 * index.js
 +-- ...
* package.json
* package-lock.json
+-- README.md



## Setup Instructions

### Backend (Flask API)

1. Clone the repository.
2. Navigate to the backend directory.
3. Create and activate a virtual environment.
4. Install dependencies from requirements.txt.
5. Configure environment variables in .env file.
6. Run the Flask server (`python app.py`).

### Frontend (React)

1. Navigate to the frontend directory.
2. Install dependencies (`npm install`).
3. Start the development server (`npm start`).

## Usage

### Backend API

- Access the API endpoints at [http://localhost:5000](http://localhost:5000).
- Use tools like Postman to interact with the API.

### Frontend

- Access the React application at [http://localhost:3000](http://localhost:3000).
- Register/login as a user or explore available job listings.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
