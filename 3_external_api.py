import requests

## all should be high confidence here

OPENAI_API_KEY = "[REDACTED_VERY_LOW_[RED...xyz]]"
OPENAI_ORG_ID = "org-1234567890abcdefghijklmnop"

GOOGLE_API_KEY = "[REDACTED_VERY_LOW_[RED...tuv]]"
GOOGLE_MAPS_KEY = "AIzaSyMaps567890abcdefghijklmnopqrstuv"

ANTHROPIC_KEY = "[REDACTED_VERY_LOW_[RED...xyz]]"

SENDGRID_API_KEY = "SG.1234567890123456789012.abcdefghijklmnopqrstuvwxyz1234567890123"

class APIClient:
    def __init__(self):
        self.openai_key = "[REDACTED_VERY_LOW_[RED...def]]"
        self.headers = {
            'Authorization': f'Bearer {self.openai_key}',
            'Content-Type': 'application/json'
        }