# Network requests with library
import requests as requestlib
import urllib
import json

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}

try:
    r = requestlib.get("https://jsonplaceholder.typicode.com/users/10")
    print(r.status_code)
    print("json:", r.json())
except (requestlib.HTTPError, Exception) as e:
    print("ERROR:", repr(e))

#Request with urlib
print("""
    Using urlib
""")
try:
    data = {}
    req = urllib.request.Request(url="https://jsonplaceholder.typicode.com/users/10",
                                 headers=HEADERS, method="GET")
    with urllib.request.urlopen(req) as response:
        response_text = response.read()
        print(response.status)
        data = json.loads(response_text)
        if not data:
            print("NO user")
    print("URLIBDATA:", data)
except (urllib.error.HTTPError, Exception ) as e:
    print("ERROR:", repr(e))
