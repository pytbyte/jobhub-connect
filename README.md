## Job Connect
Description

Job Connect is a web application designed to connect job seekers with potential employers. The platform facilitates job searches, applications, and employer listings.

# Features

* User Authentication:    Allows users to create accounts, log in, and manage their profiles.
* Job Listings:    Displays available job openings with detailed descriptions.
* Application Submission:   Enables job seekers to apply for listed jobs.
* Employer Dashboard:   Provides employers with a platform to post job openings and manage applications.

# Tech Stack
## Frontend:

* React
* Redux (for state management)
* Axios (for API interactions)
* React Router (for routing)

## Backend:

* Flask (Python)
* SQLAlchemy (for database ORM)
* Redis (for caching)
* JWT (for authentication)
* RESTful API architecture
+-- bin // Custom tasks
+-- dist // Source build
+-- public // Static Files
+-- src
|   +-- config // Environment Configuration
|   +-- entity // TypeORM Entities
|   +-- auth // Authentication
|   +-- common // Global Nest Module
|   |   +-- constants // Constant value and Enum
|   |   +-- controllers // Nest Controllers
|   |   +-- decorators // Nest Decorators
|   |   +-- dto // DTO (Data Transfer Object) Schema, Validation
|   |   +-- filters // Nest Filters
|   |   +-- guards // Nest Guards
|   |   +-- interceptors // Nest Interceptors
|   |   +-- interfaces // TypeScript Interfaces
|   |   +-- middleware // Nest Middleware
|   |   +-- pipes // Nest Pipes
|   |   +-- providers // Nest Providers
|   |   +-- * // models, repositories, services...
|   +-- shared // Shared Nest Modules
|   +-- gql // GraphQL Structure
|   +-- * // Other Nest Modules, non-global, same as common structure above
+-- test // Jest testing
+-- typings // Modules and global type definitions

// Module structure
// Add folders according to module scale. If it's small, you don't need to add folders.
+-- src/greeter
|   +-- * // folders
|   +-- greeter.constant.ts
|   +-- greeter.controller.ts
|   +-- greeter.service.ts
|   +-- greeter.module.ts
|   +-- greeter.*.ts
|   +-- index.ts

# Setup Instructions

## Backend (Flask API)

* Clone the repository.
* Navigate to the backend directory.
* Create and activate a virtual environment.
* Install dependencies from requirements.txt.
* Configure environment variables in .env file.
* Run the Flask server (python app.py).


## Frontend (React)

* Navigate to the frontend directory.
* Install dependencies (npm install).
* Start the development server (npm start).


## Usage

# Backend API
 
* Access the API endpoints at http://localhost:5000.
* Use tools like Postman to interact with the API.

# Frontend

* Access the React application at http://localhost:3000.
* Register/login as a user or explore available job listings.
* Contributing
* Contributions are welcome! Feel free to open issues or submit pull requests.

# License
This project is licensed under the MIT License.
