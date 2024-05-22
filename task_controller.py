from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = TaskService.list_tasks()
    return jsonify(tasks)

@task_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = TaskService.get_task(id)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')
    assigned_to = data.get('assigned_to')
    created_at = data.get('created_at')
    task = TaskService.create_task(title, description, status, assigned_to, created_at)
    return jsonify(task), 201

@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    status = data.get('status')
    task = TaskService.update_task(id, status)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    deleted = TaskService.delete_task(id)
    if deleted:
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404
