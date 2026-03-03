import requests, re

url = "https://hexhunt2025.pythonanywhere.com/"
data = {"user":"reverse_engineer","action":"get_flag"}

resp = requests.post(url, json=data)
print("HTTP", resp.status_code)
print(resp.text)

m = re.search(r'(swt\{.*?\})', resp.text)
if m:
    print("\nFLAG:", m.group(1))
else:
    print("\nNo swt{...} found in response.")
