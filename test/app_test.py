import json

import requests
from nose.tools import assert_true

"""The tests to run in this project.
To run the tests
$ nosetests --verbose
"""

BASE_URL = "http://127.0.0.1:5000/"


# BASE_URL = "https://jkchang.herokuapp.com/swagger/"



def test_baseURL_redirection():
    "Test baseURL redirection"
    response = requests.get('%s/' % (BASE_URL))
    assert_true(response.ok)

def test_positive():
    "Test output contents"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=BRC&limit=10' % (BASE_URL))
    assert_true(response.json()['data'] == ['BRCA1', 'BRCA2', 'BRCC3', 'BRCC3P1'])

def test_case_sensitivity():
    "Test gene_suggest query case_sensitivity"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=BrC&limit=10' % (BASE_URL))
    assert_true(response.ok)


def test_case_sensitivity2():
    "Test gene_suggest species case_sensitivity"
    response = requests.get('%s/gene_suggest?species=hOMo_sapiens&query=BRC&limit=10' % (BASE_URL))
    assert_true(response.ok)

def test_miss_required_parameters():
    "Test missing required parameters"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&limit=10' % (BASE_URL))
    assert_true(response.status_code == 400)


def test_unmatched_species():
    "Test unmatched species input - NOT FOUND"
    response = requests.get('%s/gene_suggest?species=homo&query=BRC&limit=10' % (BASE_URL))
    assert_true(response.status_code == 404)


def test_unmatched_query():
    "Test unmatched query input - NOT FOUND"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=BRC123&limit=10' % (BASE_URL))
    assert_true(response.status_code == 404)


def test_invalid_parameter():
    "Test invalid limit input - BAD REQUEST"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=BRC&limit=a' % (BASE_URL))
    assert_true(response.status_code == 400)


def test_output_json_format():
    "Test Response is a well-formed JSON object"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=BRC' % (BASE_URL))
    try:
        json_object = json.loads(response.content)
    except ValueError as e:
        assert False
    assert True

def test_limitaion():
    "Test output limitation"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=BRC&limit=1' % (BASE_URL))
    assert_true(response.json()['data'] == ['BRCA1'])

def test_no_limitaion():
    "Test no output limitation"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=AC0' % (BASE_URL))
    assert_true(len(response.json()['data']) == 11203)

def test_dot_in_query():
    "Test '.' in the query"
    response = requests.get('%s/gene_suggest?species=homo_sapiens&query=ABBA01000933.' % (BASE_URL))
    assert_true(response.json()['data'] == ['ABBA01000933.1'])

# def validate_headers():
#     "validate headers"
#     response = requests.get('%s/gene_suggest?species=homo_sapiens&query=BrC&limit=10' % (BASE_URL))

test_dot_in_query()