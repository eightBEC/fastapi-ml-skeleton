

from fastapi_skeleton.core import messages


def test_auth_using_prediction_api_no_apikey_header(test_client) -> None:
    response = test_client.post('/api/model/predict')
    assert response.status_code == 400
    assert response.json() == {"detail": messages.NO_API_KEY}


def test_auth_using_prediction_api_wrong_apikey_header(test_client) -> None:
    response = test_client.post(
        '/api/model/predict',
        json={"image": "test"},
        headers={"token": "WRONG_TOKEN"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": messages.AUTH_REQ}
