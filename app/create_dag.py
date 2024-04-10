from flask import Blueprint, request, jsonify

# Create a Blueprint for create_dag module
create_dag_bp = Blueprint('create_dag', __name__)

# Dictionary to store created DAGs
dags = {}


@create_dag_bp.route('/api/create_dag', methods=['POST'])
def create_dag():
    data = request.get_json()
    dag_id = data.get('dag_id')
    tasks = data.get('tasks', [])
    # Validate input
    if not dag_id:
        return jsonify({"error": "DAG ID is required"}), 400
    if dag_id in dags:
        return jsonify({"error": "DAG ID already exists"}), 400
    if not tasks:
        return jsonify({"error": "At least one task is required"}), 400

    # Store the DAG
    dags[dag_id] = tasks

    return jsonify({"message": "DAG created successfully", "dag_id": dag_id}), 200
