from http import HTTPStatus
from fast_zero.app import app
from fastapi.testclient import TestClient


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    
    assert response.json() == {'message': 'Olá Mundo!'} # Assert
