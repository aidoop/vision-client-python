from package.operato_vision_api import OperatoVisionClient

client = OperatoVisionClient('http://localhost:3000', 'system')
client.signin('admin@hatiolab.com', 'admin')

print(client.access_token)
