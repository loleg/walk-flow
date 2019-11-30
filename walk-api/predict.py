import json
import falcon
import random
from .model_prediction import computePrediction

class PredictResource(object):

    def on_get(self, req, resp):
        example_query = {
          "usage": "work",
          "measures": [
            {
              "date": "2019-11-20",
              "counted": "1",
              "temperature": "25",
              "rain": "11"
            },
            {
              "date": "2019-11-14",
              "counted": "12",
              "temperature": "2",
              "rain": "22"
            }
          ]
        }

        query = example_query
        # query = json.parse(req)

        perfect_calculation_per_day, perfect_calculation_per_weekday = computePrediction(query)

        example_response = {
          "day": perfect_calculation_per_day,
          "weekday": perfect_calculation_per_weekday
        }

        resp.body = json.dumps(example_response, ensure_ascii=False)
        resp.status = falcon.HTTP_200
