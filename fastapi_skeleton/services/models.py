

from typing import List

import joblib
import numpy as np
from loguru import logger

from fastapi_skeleton.core.messages import NO_VALID_PAYLOAD
from fastapi_skeleton.models.payload import (HousePredictionPayload,
                                             payload_to_list)
from fastapi_skeleton.models.prediction import HousePredictionResult


class HousePriceModel(object):

    RESULT_UNIT_FACTOR = 100000

    def __init__(self, path):
        self.path = path
        self._load_local_model()

    def _load_local_model(self):
        self.model = joblib.load(self.path)

    def _pre_process(self, payload: HousePredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result

    def _post_process(self, prediction: np.ndarray) -> HousePredictionResult:
        logger.debug("Post-processing prediction.")
        result = prediction.tolist()
        human_readable_unit = result[0] * self.RESULT_UNIT_FACTOR
        hpp = HousePredictionResult(median_house_value=human_readable_unit)
        return hpp

    def _predict(self, features: List) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result

    def predict(self, payload: HousePredictionPayload):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result
