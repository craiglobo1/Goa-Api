import requests

url = 'http://127.0.0.1:8000/api/create/'
data = {
    'owner': '',
    'houseNo': '',
    'establishmentName': 'Amani',
    'noOfRooms': 12,
    'type': 'rental',
    'vaddo': 'Khobra'
}
r = requests.post(url, data=data)
print(r.json(), r.status_code)
