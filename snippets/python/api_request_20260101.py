"""
API Request Helper
"""
import json
from urllib.request import urlopen, Request
from urllib.error import URLError

def make_request(url, method="GET", data=None, headers=None):
    """Make HTTP request and return JSON response."""
    headers = headers or {"Content-Type": "application/json"}
    
    if data and isinstance(data, dict):
        data = json.dumps(data).encode()
    
    try:
        req = Request(url, data=data, headers=headers, method=method)
        with urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except URLError as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    result = make_request("https://api.github.com")
    print(f"Response keys: {list(result.keys())[:5]}")
