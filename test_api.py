import requests

# Base URL of the API
BASE_URL = 'http://127.0.0.1:5000'

# Function to handle API requests and print responses
def make_request(method, url, data=None):
    response = method(url, json=data)
    if response.ok:
        try:
            return response.json()
        except ValueError:
            return 'Response is not in JSON format'
    else:
        return f'{response.status_code} {response.reason}'

# Function to retrieve a list of drones
def get_drones():
    url = f'{BASE_URL}/api/drones/'
    return make_request(requests.get, url)

# Function to create a new task
def create_task(name, description, drone_id):
    url = f'{BASE_URL}/api/tasks/'
    data = {'name': name, 'description': description, 'drone_id': drone_id}
    return make_request(requests.post, url, data)

# Function to retrieve details of a specific task
def get_task(task_id):
    url = f'{BASE_URL}/api/tasks/{task_id}/'
    return make_request(requests.get, url)

# Function to execute a task
def execute_task(task_id):
    url = f'{BASE_URL}/api/tasks/{task_id}/execute/'
    return make_request(requests.post, url)

# Main function to test all endpoints
def main():
    print('\nGET /api/drones:\n', get_drones())
    print('\nPOST /api/tasks:\n', create_task('Task 1', 'Description of Task 1', 1))
    print('\nGET /api/tasks/1:\n', get_task(1))
    print('\nPOST /api/tasks/1/execute:\n', execute_task(1))

if __name__ == "__main__":
    main()
