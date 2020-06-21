import asyncio
import json
import requests
import asyncio

from gql import gql, Client as GqlClient
from gql.transport.requests import RequestsHTTPTransport

from .graphql import graphql_query, QUERY_TRACKING_CAMERA, TRACKING_CAMERAS


class Client:

    def __init__(self, endpoint, domain):
        self.endpoint = endpoint
        self.domain = domain
        self.client = None

    def signin(self, email, password):

        url = '{0}/signin'.format(self.endpoint)
        headers = {
            "Content-Type": "application/json",
            "x-only-token": "true"
        }
        security = {
            'email': email,
            'password': password
        }

        response = requests.post(url,
                                 headers=headers,
                                 json=security)

        if response.status_code == 200:
            self.access_token = response.text
        else:
            self.access_token = None

        reqHeaders = {
            'authorization': self.access_token,
            'x-things-factory-domain': self.domain
        }

        _transport = RequestsHTTPTransport(
            url='{0}/graphql'.format(self.endpoint),
            headers=reqHeaders,
            use_json=True,
        )

        self.client = GqlClient(
            transport=_transport,
            fetch_schema_from_transport=True,
        )

        return

    @graphql_query(TRACKING_CAMERAS)
    def get_tracking_cameras(self):
        pass

    @graphql_query(QUERY_TRACKING_CAMERA, ['name'])
    def get_tracking_camera(self, name):
        pass

    def update_tracking_camera(self, cameraPatch):
        return
