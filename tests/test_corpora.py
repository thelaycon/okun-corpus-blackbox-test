import pytest
import json
import requests

ENDPOINT_URL = "https://corpus.okunresearch.com.ng/okun-corpus"

def test_fetch_api():
    # Check if api works
    response = requests.get(ENDPOINT_URL)
    
    #Confirm success
    assert response.status_code == 200

