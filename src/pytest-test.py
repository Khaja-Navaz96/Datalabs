# # import logging
# # import os
# # import unittest
# # import pytest
# # import requests
# # from flask_testing import TestCase
# #
# # from app import DB
# #
# # @pytest.mark.parametrize('post_data', {'name': 'rutuja'})
# # def correct_data_posted(post_data):
# #         response = requests.post('http://localhost:5000/insert',data=post_data)
# #
# #         assert response.status_code == 202
# #
#
#
# import pytest
# import requests
# import unittest
#
# @pytest.mark.parametrize('post_data', ({'name': 'aniket'},{'name': 'suraj'},{'name': 'kavya'}))
# def correct_data_posted(post_data):
#     response = requests.post('http://localhost:5000/insert', data=post_data)
#     assert response.status_code == 200
#
#
#
# # Cases where incorrect data is posted to '/update/'
# @pytest.mark.parametrize('post_data', ({'name': None},{'name': 'rutuja'},{'name': None}))
# def validation_errors_for_incorrect_data_post(post_data):
#     response = requests.post('http://localhost:5000/insert',data=post_data,)
#     assert response.status_code == 422
#
#
# # Cases where correct data is posted to '/update/'
# @pytest.mark.parametrize('post_data', ({'name': 'aniket'},{'name': 'suraj'},{'name': 'kavya'}))
# def correct_data_posted(post_data):
#     response = requests.post('/update/', data=post_data)
#     assert response.status_code == 200
#
#
#
# # Cases where incorrect data is posted to '/del/'
# @pytest.mark.parametrize('post_data', ({'name': 999},{'name': 188},{'name': 277}))
# def correct_delete_data_posted(post_data):
#     response = requests.post('http://localhost:5000//del', data=post_data)
#     assert response.status_code == 422
#
#
#
# #Incorrect request type
# @pytest.mark.parametrize('http_method,endpoint', (('put', '/insert/'),('put', '/del/')))
# def test_return_404_error_for_not_finding_resource_for_endpoints(http_method,endpoint):
#     endpoint = endpoint.format()
#     response = getattr(requests, http_method)(endpoint,data={'name':'name'})
#
#     assert response.status_code == 404
#



import pytest
import requests
id_var = '8dc427ee-544e-11e9-b8cb-a860b63b5469'
from flask import Flask, render_template, request, redirect
@pytest.mark.parametrize("test_input", [{'name': 'suraj'},{'name': 'avil'}])
def test_insert(test_input):
    response = requests.post('http://localhost:5000/insert', data=test_input)
    assert response.status_code == 200




@pytest.mark.parametrize('post_data', [{'name': 'fgd', 'id': id_var}])
def test_update(post_data):
    response = requests.post('http://localhost:5000/update', data=post_data)
    assert response.status_code == 200


@pytest.mark.parametrize('post_data', [{'id': id_var}])
def test_update(post_data):
    response = requests.post('http://localhost:5000/del', data=post_data)
    assert response.status_code == 200



@pytest.mark.parametrize('http_method,endpoint', [
    ('put', 'http://localhost:5000/insert'),
    ('put', 'http://localhost:5000/del')])
def test_return_404_error_for_not_finding_resource_for_endpoints(http_method,endpoint):
    endpoint = endpoint.format()
    response = getattr(requests, http_method)(endpoint,data={'id': id_var, 'name': 'asda'})


@pytest.mark.parametrize('post_data', [{'name': None, 'id': '8dc427ee-544e-11e9-b8cb-a860b63b5469'},])
def validation_errors_for_incorrect_data_post(post_data):
    response = requests.post('http://localhost:5000/update',data=post_data)
    assert response.status_code == 422
