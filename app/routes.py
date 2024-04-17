from flask import jsonify, request, abort, Blueprint
from app.models import db, Drone, Task, Image
from app.utils import generate_random_image_url

routes_blueprint = Blueprint('routes', __name__)

# Endpoint to retrieve all drones
@routes_blueprint.route('/api/drones/', methods=['GET'])
def get_drones():
    drones = Drone.query.all()
    drones_data = [{'id': drone.id, 'name': drone.name} for drone in drones]
    return jsonify(drones_data)

# Endpoint to create a new drone
@routes_blueprint.route('/api/drones/', methods=['POST'])
def create_drone():
    data = request.json
    new_drone = Drone(name=data['name'])
    db.session.add(new_drone)
    db.session.commit()
    return jsonify({'message': 'Drone created successfully'}), 201

# Endpoint to retrieve details of a specific drone
@routes_blueprint.route('/api/drones/<int:id>/', methods=['GET'])
def get_drone(id):
    drone = Drone.query.get_or_404(id)
    drone_data = {'id': drone.id, 'name': drone.name}
    return jsonify(drone_data)

# Endpoint to create a new task
@routes_blueprint.route('/api/tasks/', methods=['POST'])
def create_task():
    data = request.json
    if 'name' not in data or 'description' not in data or 'drone_id' not in data:
        abort(400, 'Missing required fields')
    drone = Drone.query.get(data['drone_id'])
    if not drone:
        abort(404, 'Drone not found')
    new_task = Task(name=data['name'], description=data['description'], drone_id=data['drone_id'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

# Endpoint to retrieve details of a specific task
@routes_blueprint.route('/api/tasks/<int:id>/', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    task_data = {
        'id': task.id,
        'name': task.name,
        'description': task.description,
        'drone_id': task.drone_id,
        'drone_name': task.drone.name,
    }
    return jsonify(task_data)

# Endpoint to execute a task
@routes_blueprint.route('/api/tasks/<int:id>/execute/', methods=['POST'])
def execute_task(id):
    task = Task.query.get_or_404(id)
    noisy_images = []
    for _ in range(5):
        image_url = generate_random_image_url()
        noisy_images.append(image_url)
        new_image = Image(url=image_url, task_id=task.id)
        db.session.add(new_image)
    db.session.commit()
    return jsonify({'message': 'Task executed successfully', 'noisy_images': noisy_images}), 201

# Endpoint to retrieve images captured during the execution of a task
@routes_blueprint.route('/api/tasks/<int:id>/images/', methods=['GET'])
def get_task_images(id):
    task = Task.query.get_or_404(id)
    images_data = [{'id': image.id, 'url': image.url} for image in task.images]
    return jsonify(images_data)
