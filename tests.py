from fastapi.testclient import TestClient

from main import app
import pytest

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    


# def test_hello_name(name):
#     name = 'Kamila'
#     response = client.get(f"/hello/{name}")
#     assert response.status_code == 200
#     assert response.text == f'"Hello {name}"'



def test_counter():
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "1"
    # 2nd Try
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "2"