import requests
import time
import hmac
import hashlib
import argparse
from pathlib import Path

_FBX_HEADERS = {"Content-type": "application/json", "X-Fbx-App-Auth": ""}
_FBX_URL = ""
_FBX_TOKEN = ""
_FBX_ARGS = None


def get(url: str):
    response = requests.get(
        url,
        headers=_FBX_HEADERS,
        verify=Path(__file__).resolve().parent / "free.cert",
    ).json()

    if _FBX_ARGS.verbose:
        print("\n")
        print(f" ? GET: {url}")
        print(f" > Response: {response}")
        print("\n")

    return response


def post(url, params=None):
    response = requests.post(
        url,
        json=params,
        headers=_FBX_HEADERS,
        verify=Path(__file__).resolve().parent / "free.cert",
    ).json()

    if _FBX_ARGS.verbose:
        print("\n")
        print(f" ? GET: {url}")
        print(f" - Parameters: {params}")
        print(f" - Headers: {_FBX_HEADERS}")
        print(f" > Response: {response}")
        print("\n")

    return response


def check_token():
    global _FBX_TOKEN
    global _FBX_HEADERS

    token_path = Path(__file__).resolve().parent / "freebox.token"

    if not token_path.is_file():
        print(" - Aucun token enregistré")
        return False

    with open(token_path, "r") as f:
        _FBX_TOKEN = f.read()

    print(" - Token local chargé")

    return True


def save_token(token: str):
    current_path = Path(__file__).resolve().parent
    token_path = current_path / "freebox.token"

    with open(token_path, "w") as f:
        f.write(token)

    print(" - Token enregistré localement")


def get_sha1(challenge: str):
    hash = hmac.new(
        key=str.encode(_FBX_TOKEN),
        msg=str.encode(challenge),
        digestmod=hashlib.sha1,
    )
    return hash.hexdigest()


def login():
    global _FBX_HEADERS

    login_endpoint = get(f"{_FBX_URL}/login")
    challenge = login_endpoint["result"]["challenge"]

    params = {
        "app_id": "fr.freebox.reboot",
        "app_version": "1.0.0",
        "password": get_sha1(challenge=challenge),
    }
    session_endpoint = post(url=f"{_FBX_URL}/login/session/", params=params)
    _FBX_HEADERS["X-Fbx-App-Auth"] = session_endpoint["result"]["session_token"]


def check_auth():
    lang = get(f"{_FBX_URL}/lang")

    return lang["success"]


def discover():
    global _FBX_URL

    if _FBX_ARGS.http:
        base_url = "http://mafreebox.freebox.fr"
    else:
        base_url = "https://mafreebox.freebox.fr"

    discover_endpoint = get(f"{base_url}/api_version")
    api_version = discover_endpoint["api_version"]
    major_version = api_version.split(".")[0]

    _FBX_URL = f"{base_url}/api/v{major_version}"


def get_token():
    global _FBX_HEADERS

    get_token_endpoint = f"{_FBX_URL}/login/authorize/"
    params = {
        "app_id": "fr.freebox.reboot",
        "app_name": "Freebox Reboot",
        "app_version": "1.0.0",
        "device_name": "Reboot Signal Sender",
    }
    request_token = post(url=get_token_endpoint, params=params)
    app_token = request_token["result"]["app_token"]
    track_id = request_token["result"]["track_id"]

    print(" -!- Autorisez l'application sur l'écran de votre freebox")

    track_auth = get(f"{_FBX_URL}/login/authorize/{track_id}")
    while track_auth["result"]["status"] == "pending":
        print(" - En attente d'autorisation")
        time.sleep(2)
        track_auth = get(f"{_FBX_URL}/login/authorize/{track_id}")

    print(" - Autorisation accordée !")

    _FBX_TOKEN = app_token

    save_token(token=_FBX_TOKEN)


def reboot():
    print(" - Envoi du signal de reboot")
    reboot_endpoint = post(url=f"{_FBX_URL}/system/reboot/")

    if reboot_endpoint["success"]:
        print(" - Succès ! Freebox en cours de redémarrage")
    else:
        print(" !!! Echec de la demande de redémarrage")
        if reboot_endpoint["missing_right"] == "settings":
            rights_error()


def rights_error():
    print("\nL'application n'a pas les droits nécessaires pour le reboot.")
    print(" - Allez sur http://mafreebox.freebox.fr/#Fbx.os.app.settings.Accounts")
    print(" - Ouvrez l'onglet 'Applications'")
    print(" - Trouvez l'application 'Freebox Reboot'")
    print(" - Cochez la case 'Modification des réglages de la Freebox'")
    print(" - Validez vos modifications")


def parse_args():
    global _FBX_ARGS
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", "--debug", help="Debug mode", action="store_true")
    parser.add_argument("-d", "--dry", help="Run without rebooting", action="store_true")
    parser.add_argument("--http", help="Use HTTP instead of HTTPS", action="store_true")
    _FBX_ARGS = parser.parse_args()


def main():
    parse_args()
    discover()
    if not check_token():
        get_token()

    login()
    if not check_auth():
        print(" -!- Echec de l'authentification, supprimez le fichier 'freebox.token'.")
        return
    print(" - Authentification réussie")

    if not _FBX_ARGS.dry:
        reboot()


if __name__ == "__main__":
    main()
