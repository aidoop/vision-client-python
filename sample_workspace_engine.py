import sys
import json
from operato_vision import Client


def main(argv):
    workspaceName = argv[1]

    client = Client('http://localhost:3000', 'system')
    client.signin('admin@hatiolab.com', 'admin')

    status = {
        "objectStatus": [{
            "id": "obj",
            "state": {
                "roi": "A",
                "pose": {
                    "x": 1.0,
                    "y": 2.0,
                    "z": 3.4,
                    "u": 4.0,
                    "v": 5.9,
                    "w": 6.0
                }
            }
        }]
    }

    result = client.update_tracking_workspace_status(
        name='workspace', status=status)

    print(result)


if __name__ == "__main__":
    # main(sys.argv)
    main("abc")
