import json

ROIs = [{
    "id": 'A',
    "region": {
        "lt": {
            "x": 103,
            "y": 100
        },
        "rb": {
            "x": 203,
            "y": 200
        }
    }
}, {
    "id": 'B',
    "region": {
        "lt": {
            "x": 105,
            "y": 100
        },
        "rb": {
            "x": 205,
            "y": 200
        }
    }
}]

print(json.dumps(ROIs))
