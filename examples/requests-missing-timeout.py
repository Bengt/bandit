import httpx
import requests
import not_requests

# Errors
requests.get('https://gmail.com')
requests.get('https://gmail.com', timeout=None)
requests.post('https://gmail.com')
requests.post('https://gmail.com', timeout=None)
requests.put('https://gmail.com')
requests.put('https://gmail.com', timeout=None)
requests.delete('https://gmail.com')
requests.delete('https://gmail.com', timeout=None)
requests.patch('https://gmail.com')
requests.patch('https://gmail.com', timeout=None)
requests.options('https://gmail.com')
requests.options('https://gmail.com', timeout=None)
requests.head('https://gmail.com')
requests.head('https://gmail.com', timeout=None)
httpx.get('https://gmail.com')
httpx.get('https://gmail.com', timeout=None)
httpx.post('https://gmail.com')
httpx.post('https://gmail.com', timeout=None)
httpx.put('https://gmail.com')
httpx.put('https://gmail.com', timeout=None)
httpx.delete('https://gmail.com')
httpx.delete('https://gmail.com', timeout=None)
httpx.patch('https://gmail.com')
httpx.patch('https://gmail.com', timeout=None)
httpx.options('https://gmail.com')
httpx.options('https://gmail.com', timeout=None)
httpx.head('https://gmail.com')
httpx.head('https://gmail.com', timeout=None)
httpx.Client()
httpx.Client(timeout=None)
httpx.AsyncClient()
httpx.AsyncClient(timeout=None)
with httpx.Client() as client:
    client.get('https://gmail.com')
with httpx.Client(timeout=None) as client:
    client.get('https://gmail.com')
async with httpx.AsyncClient() as client:
    await client.get('https://gmail.com')
async with httpx.AsyncClient(timeout=None) as client:
    await client.get('https://gmail.com')

# Okay
not_requests.get('https://gmail.com')
requests.get('https://gmail.com', timeout=5)
requests.post('https://gmail.com', timeout=5)
requests.put('https://gmail.com', timeout=5)
requests.delete('https://gmail.com', timeout=5)
requests.patch('https://gmail.com', timeout=5)
requests.options('https://gmail.com', timeout=5)
requests.head('https://gmail.com', timeout=5)
httpx.get('https://gmail.com', timeout=5)
httpx.post('https://gmail.com', timeout=5)
httpx.put('https://gmail.com', timeout=5)
httpx.delete('https://gmail.com', timeout=5)
httpx.patch('https://gmail.com', timeout=5)
httpx.options('https://gmail.com', timeout=5)
httpx.head('https://gmail.com', timeout=5)
httpx.Client(timeout=5)
httpx.AsyncClient(timeout=5)
with httpx.Client(timeout=5) as client:
    client.get('https://gmail.com')
async with httpx.AsyncClient(timeout=5) as client:
    await client.get('https://gmail.com')
