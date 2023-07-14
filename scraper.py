import requests
from credentials import creds

LOGIN_URL = 'https://www.fie.undef.edu.ar/siu/3w/'
PROMEDIO_URL = 'https://www.fie.undef.edu.ar/siu/3w/porcentaje_avance_carrera'

payload = {
    'usuario': creds['username'],
    'password': creds['password'],
    'login': 'Ingresar',
}

