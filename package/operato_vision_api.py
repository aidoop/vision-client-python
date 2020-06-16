import json
import requests


class OperatoVisionClient:

    def __init__(self, endpoint, domain):
        self.endpoint = endpoint
        self.domain = domain

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

    def getTrackingCameras(self):
        return

    def getTrackingCamera(self, cameraName):
        return

    def updateTrackingCamera(self, cameraPatch):
        return

        # from gql import Client
        # from gql.transport.requests import RequestsHTTPTransport

        # from .someSchema import SampleSchema

        # client = Client(transport=RequestsHTTPTransport(
        #     url='/graphql', headers={'Authorization': 'token'}), schema=SampleSchema)
