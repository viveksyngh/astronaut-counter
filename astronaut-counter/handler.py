import requests
import random
import logging
import time

logging.basicConfig(level=logging.DEBUG)


def handle(req):
    logging.debug("Making request to open notify API")
    start = time.time()
    r = requests.get("http://api.open-notify.org/astros.json")
    logging.debug("Request completed. Total time taken %s", time.time() - start)
    result = r.json()
    return result["number"]

