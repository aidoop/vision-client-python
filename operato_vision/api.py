import asyncio
import json
import requests
import asyncio

from gql import gql, Client as GqlClient
from gql.transport.requests import RequestsHTTPTransport

from .graphql import graphql_query, graphql_mutation
from .graphql import QUERY_VISION_WORKSPACE, QUERY_VISION_WORKSPACES, QUERY_TRACKING_CAMERA, QUERY_TRACKING_CAMERAS
from .graphql import QUERY_TRACKABLE_OBJECT, QUERY_TRACKABLE_OBJECTS, QUERY_ROBOT_ARM, QUERY_ROBOT_ARMS, QUERY_ROBOT_ARM_POSE, MUTATION_ROBOT_ARM_POSE


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

    @graphql_query(QUERY_VISION_WORKSPACES)
    def get_vision_workspaces(self):
        pass

    @graphql_query(QUERY_VISION_WORKSPACE, ['name'])
    def get_vision_workspace(self, name):
        pass

    @graphql_query(QUERY_TRACKING_CAMERAS)
    def get_tracking_cameras(self):
        pass

    @graphql_query(QUERY_TRACKING_CAMERA, ['name'])
    def get_tracking_camera(self, name):
        pass

    @graphql_query(QUERY_TRACKABLE_OBJECTS)
    def get_trackable_objects(self):
        pass

    @graphql_query(QUERY_TRACKABLE_OBJECT, ['name'])
    def get_trackable_object(self, name):
        pass

    @graphql_query(QUERY_ROBOT_ARMS)
    def get_robot_arms(self):
        pass

    @graphql_query(QUERY_ROBOT_ARM, ['name'])
    def get_robot_arm(self, name):
        pass

    @graphql_query(QUERY_ROBOT_ARM_POSE, ['name'])
    def get_robot_arm_pose(name):
        pass

    @graphql_mutation(MUTATION_ROBOT_ARM_POSE, ['name', 'pose'])
    def set_robot_arm_pose(name, pose):
        pass
