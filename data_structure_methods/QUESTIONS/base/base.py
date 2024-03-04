import requests

responses= requests.get("https://api.postalpincode.in/pincode/673634")

print(responses.status_code)