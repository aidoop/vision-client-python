from package.operato_vision_api import OperatoVisionClient

client = OperatoVisionClient('http://localhost:3000', 'system')
client.signin('admin@hatiolab.com', 'admin')

print(client.get_tracking_camera('usbcam'))
print(client.get_tracking_camera('webcam'))
