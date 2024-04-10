import pytest
from flask import Flask

from app.create_dag import create_dag_bp, dags
from app.get_dag import get_dag_bp

@pytest.fixture
def app():
    # Create a Flask application
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(create_dag_bp)
    app.register_blueprint(get_dag_bp)

    return app

@pytest.fixture
def client(app):
    # Create a test client using the Flask application context
    with app.test_client() as client:
        yield client

def test_create_dag(client):
    # Test case for successful creation of a DAG
    response = client.post('/api/create_dag', json={"dag_id": "test_dag", "tasks": ["task1", "task2"]})
    assert response.status_code == 200
    assert response.json == {"message": "DAG created successfully", "dag_id": "test_dag"}
    assert "test_dag" in dags

    # Test case for creating a DAG with missing ID
    response = client.post('/api/create_dag', json={"tasks": ["task1", "task2"]})
    assert response.status_code == 400
    assert response.json == {"error": "DAG ID is required"}

    # Test case for creating a DAG with existing ID
    response = client.post('/api/create_dag', json={"dag_id": "test_dag", "tasks": ["task1", "task2"]})
    assert response.status_code == 400
    assert response.json == {"error": "DAG ID already exists"}
