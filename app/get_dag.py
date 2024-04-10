from flask import Blueprint, jsonify
from app.create_dag import dags

get_dag_bp = Blueprint('get_dag', __name__)


@get_dag_bp.route('/api/get_dag/<dag_id>', methods=['GET'])
def get_dag(dag_id):
    if dag_id not in dags:
        return jsonify({"error": "DAG not found"}), 404

    return jsonify({"dag_id": dag_id, "tasks": dags[dag_id]}), 200
