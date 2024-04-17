# UAV Monitoring Platform

This project is a Python application for monitoring UAV (Unmanned Aerial Vehicle) activities using a Flask API.

## Installation

1. Install dependencies if they are not already installed (e.g., Flask, etc.).
  
2. Run the Flask application:

    ```bash
    python app.py
    ```

The application will start running at `http://127.0.0.1:5000`.

## Usage

1. **API Endpoints:**

    - `/api/drones/`: Retrieve a list of drones.
    - `/api/tasks/`: Create a new task.
    - `/api/tasks/<task_id>/`: Retrieve details of a specific task.
    - `/api/tasks/<task_id>/execute/`: Execute a task.

2. **Testing Endpoints:**

    The `test_api.py` file contains functions to test the API endpoints. Run the tests using:

    ```bash
    python test_api.py
    ```
