from .queries import QUERIES

QUERY_VISION_WORKSPACE = 'visionWorkspace'
QUERY_VISION_WORKSPACES = 'visionWorkspaces'

QUERIES[QUERY_VISION_WORKSPACE] = '''
query visionWorkspace($name: String!) {
    visionWorkspace(name:$name) {
        id
        name
        domain {
            name
        }
        description
        type
        endpoint
        active
        params
        RobotArms {
            id
            name
        }
        TrackingCameras {
            id
            name
        }
        TrackableObject {
            id
            name
        }
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
'''

QUERIES[QUERY_VISION_WORKSPACES] = '''
query {
    visionWorkspaces {
        items {
            id
            name
            domain {
                name
            }
            description
            type
            endpoint
            active
            RobotArms {
                id
                name
            }
            TrackingCameras {
                id
                name
            }
            TrackableObject {
                id
                name
            }
            updater {
                email
            }
            creator {
                email
            }
            updatedAt
            createdAt
        }
        total
    }
}
'''
