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

def test_get_dag(client):
    # Test case for retrieving an existing DAG
    dags["test_dag"] = ["task1", "task2"]
    response = client.get('/api/get_dag/test_dag')
    assert response.status_code == 200
    assert response.json == {"dag_id": "test_dag", "tasks": ["task1", "task2"]}

    # Test case for retrieving a non-existing DAG
    response = client.get('/api/get_dag/non_existing_dag')
    assert response.status_code == 404
    assert response.json == {"error": "DAG not found"}

if __name__ == "__main__":
    pytest.main()