import requests
import json

url = 'https://clientsettings.roblox.com/v2/settings/application/PCDesktopClient'

response = requests.get(url)
settings = response.json()

formatted_settings = json.dumps(settings, indent=4, sort_keys=True)

with open('PCDesktopClient.json', 'w') as f:
    f.write(formatted_settings)
