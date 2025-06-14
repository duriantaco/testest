import requests

## all should be high confidence here

OPENAI_API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
OPENAI_ORG_ID = "org-1234567890abcdefghijklmnop"

GOOGLE_API_KEY = "AIzaSyD1234567890abcdefghijklmnopqrstuv"
GOOGLE_MAPS_KEY = "AIzaSyMaps567890abcdefghijklmnopqrstuv"

ANTHROPIC_KEY = "sk-ant-api03-1234567890abcdefghijklmnopqrstuvwxyz"

SENDGRID_API_KEY = "SG.1234567890123456789012.abcdefghijklmnopqrstuvwxyz1234567890123"

class APIClient:
    def __init__(self):
        self.openai_key = "sk-OpenAIProductionKey1234567890abcdef"
        self.headers = {
            'Authorization': f'Bearer {self.openai_key}',
            'Content-Type': 'application/json'
        }