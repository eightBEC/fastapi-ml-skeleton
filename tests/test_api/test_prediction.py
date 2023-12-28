from fastapi_skeleton.core import config


def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={
            "median_income_in_block": 8.3252,
            "median_house_age_in_block": 41,
            "average_rooms": 6,
            "average_bedrooms": 1,
            "population_per_block": 322,
            "average_house_occupancy": 2,
            "block_latitude": 37.88,
            "block_longitude": -122.23,
        },
        headers={"token": str(config.API_KEY)},
    )
    assert response.status_code == 200
    assert "median_house_value" in response.json()
    assert "currency" in response.json()


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/model/predict", json={}, headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 422
