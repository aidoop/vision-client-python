from .queries import QUERIES

QUERY_TRACKING_CAMERA = 'trackingCamera'
TRACKING_CAMERAS = 'trackingCameras'

QUERIES[QUERY_TRACKING_CAMERA] = '''
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
        cameraMatrix {
            rows
            columns
            data
        }
        handEyeMatrix {
            rows
            columns
            data
        }
        rois {
            id
            region {
                tl {
                    x
                    y
                }
                rb {
                    x
                    y
                }
            }
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

QUERIES[TRACKING_CAMERAS] = '''
query {
    trackingCameras {
        items {
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
            cameraMatrix {
                rows
                columns
                data
            }
            handEyeMatrix {
                rows
                columns
                data
            }
            rois {
                id
                region {
                    tl {
                        x
                        y
                    }
                    rb {
                        x
                        y
                    }
                }
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
