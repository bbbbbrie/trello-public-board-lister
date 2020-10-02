import argparse
import loguru
import os
import requests


def test_get_trello_api_end_point_200():
    response = requests.get("http://api.trello.com")
    assert response.status_code == 200


