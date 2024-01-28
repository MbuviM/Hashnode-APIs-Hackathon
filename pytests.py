import pytest
from Blog import *
import os

# Test for successful blog post
def test_successful_blog_post():
    response = make_graphql_request(url=hashnode_url, headers=auth_headers, json=request_payload)
    assert response.status_code == 200
    assert "Blog posted successfully!" in response.text

# Test for missing API key
def test_missing_api_key():
    original_key = os.environ.get('HASHNODE_API_KEY')
    os.environ['HASHNODE_API_KEY'] = ''  # Set API key to empty string for the test
    
    response = make_graphql_request(url=hashnode_url, headers=auth_headers, json=request_payload)
    assert response.status_code != 200
    assert "Error: HASHNODE_API_KEY is not set." in response.text

    os.environ['HASHNODE_API_KEY'] = original_key  # Restore the original API key

# Test for invalid API request
def test_invalid_graphql_request():
    # Modify the request payload to create an invalid GraphQL request
    invalid_payload = {"query": "invalid_mutation", "variables": {}}
    response = make_graphql_request(url=hashnode_url, headers=auth_headers, json=invalid_payload)
    assert response.status_code != 200
    assert "An error occurred." in response.text
# Test for different blog post data
def test_different_blog_post_data():
    different_data = {
        "user_id": 'another_id',
        "slug": 'another_slug',
        "title": 'Another Blog Title',
        "subtitle": 'Another Blog Subtitle',
        "author": "Another Author"
    }
    different_variables = {"input": different_data}
    different_payload = {"query": post_mutation, "variables": different_variables}

    response = make_graphql_request(url=hashnode_url, headers=auth_headers, json=different_payload)
    assert response.status_code == 200
    assert "Blog posted successfully!" in response.text
