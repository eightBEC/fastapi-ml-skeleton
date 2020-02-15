
from typing import List
from pydantic import BaseModel


class HousePredictionPayload(BaseModel):
    median_income_in_block: float
    median_house_age_in_block: int
    average_rooms: int
    average_bedrooms: int
    population_per_block: int
    average_house_occupancy: int
    block_latitude: float
    block_longitude: float


def payload_to_list(hpp: HousePredictionPayload) -> List:
    return [
        hpp.median_income_in_block,
        hpp.median_house_age_in_block,
        hpp.average_rooms,
        hpp.average_bedrooms,
        hpp.population_per_block,
        hpp.average_house_occupancy,
        hpp.block_latitude,
        hpp.block_longitude]
