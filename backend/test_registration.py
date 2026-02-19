import urllib.request
import json
import urllib.error

url = "http://127.0.0.1:8000/auth/register"

def register_user(data):
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Success: {response.getcode()}")
            print(f"Response: {response.read().decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

# Test Patient
print("\nTesting Patient Registration:")
patient_data = {
    "email": "paciente@example.com",
    "password": "securepassword123",
    "full_name": "Juan Perez",
    "identification": "12345678",
    "phone": "999888777",
    "role": "paciente"
}
register_user(patient_data)

# Test Specialist
print("\nTesting Specialist Registration:")
specialist_data = {
    "email": "dr.house@example.com",
    "password": "securepassword123",
    "full_name": "Gregory House",
    "identification": "87654321",
    "phone": "555666777",
    "role": "especialista",
    "medical_license": "CMP-12345",
    "specialty": "Diagnostico"
}
register_user(specialist_data)
