import requests
import time

BASE_URL = "http://127.0.0.1:8000"
# Generamos un usuario único para cada prueba
suffix = int(time.time())
USER_DATA = {"username": f"user_{suffix}", "password": "secure_password123"}

def test_backend():
    print("--- 🛡️ DIAGNÓSTICO DE EMERGENCIA ---")
    
    # 1. Registro (JSON)
    r_reg = requests.post(f"{BASE_URL}/api/auth/register", json=USER_DATA)
    print(f"[1] Registro: {r_reg.status_code}")

    # 2. Login (Debe ser FORM DATA, no JSON)
    # Cambiamos json=USER_DATA por data=USER_DATA
    r_login = requests.post(f"{BASE_URL}/api/auth/login", data=USER_DATA)
    
    if r_login.status_code != 200:
        print(f"❌ Fallo Login: {r_login.status_code} - {r_login.text}")
        return

    token = r_login.json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    print(f"[2] Auth: Token JWT obtenido.")

    # 3. Tarot (Llamada al orquestador)
    r_tarot = requests.post(f"{BASE_URL}/api/v1/tarot/analysis", 
                           json={"query": "Prueba de sistema", "depth": 1}, 
                           headers=headers)
    print(f"[3] Tarot: {r_tarot.status_code}")
    
    if r_tarot.status_code == 200:
        print(f"    Respuesta: {r_tarot.json()['narrative'][:50]}...")

    # 4. Historial
    r_hist = requests.get(f"{BASE_URL}/api/v1/history/", headers=headers)
    print(f"[4] Historial: {r_hist.status_code} - Items: {len(r_hist.json().get('items', []))}")

if __name__ == "__main__":
    test_backend()
