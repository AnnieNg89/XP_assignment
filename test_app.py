import pytest
from app import create_app, db
from models import Task

@pytest.fixture
def client():
    app = create_app()
    app.config.update({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI':'sqlite:///:memory:'
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_task(client):
    response = client.post('/tasks',json={'title': 'test task'})
    assert response.status_code == 200
    assert b'test task' in response.task_data
    assert Task.query.count() == 1
