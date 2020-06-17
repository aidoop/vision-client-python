import asyncio
import json
import requests
import asyncio

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


class OperatoVisionClient:

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

        self.client = Client(
            transport=_transport,
            fetch_schema_from_transport=True,
        )

        return

    def get_tracking_cameras(self):

        return

    def get_tracking_camera(self, cameraName):
        query = gql('''
            query trackingCamera($name: String!) {
                trackingCamera(name:$name) {
                    id
                    name
                    domain {
                        name
                    }
                    description
                    type
                    endpoint
                    status
                    active
                    params
                    updater {
                        email
                    }
                    creator {
                        email
                    }
                    updatedAt
                    createdAt
                }
            }
        ''')

        variables = {
            "name": cameraName
        }

        # Synchronous request
        data = self.client.execute(query, variable_values=variables)
        # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}
        # print(data)

        # Asynchronous request
        # data = asyncio.run(self.client.execute_async(
        #     query, variable_values=variables))
        # # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}

        return data

    def update_tracking_camera(self, cameraPatch):
        return

        # from gql import Client
        # from gql.transport.requests import RequestsHTTPTransport

        # from .someSchema import SampleSchema

        # client = Client(transport=RequestsHTTPTransport(
        #     url='/graphql', headers={'Authorization': 'token'}), schema=SampleSchema)
