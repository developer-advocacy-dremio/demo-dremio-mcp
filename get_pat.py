import os
import requests
import sys

DREMIO_HOST = os.environ.get("DREMIO_HOST", "http://dremio:9047")
USERNAME = os.environ.get("DREMIO_USERNAME")
PASSWORD = os.environ.get("DREMIO_PASSWORD")

if not USERNAME or not PASSWORD:
    print("❌ Missing DREMIO_USERNAME or DREMIO_PASSWORD environment variables.")
    sys.exit(1)

# Step 1: Login to Dremio
try:
    response = requests.post(
        f"{DREMIO_HOST}/apiv2/login",
        json={"userName": USERNAME, "password": PASSWORD}
    )
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"❌ Failed to connect to Dremio: {e}")
    sys.exit(1)

# Step 2: Extract and print the session token
token = data.get("token")

if not token:
    print("❌ Login succeeded but no token returned.")
    print("🔍 Full response:", data)
    sys.exit(1)

print("\n🪪 Use this token as your DREMIO_PAT value:\n")
print(token)
