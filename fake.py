
import os

config = {
    "stripe_api_key": "sk_test_51234567890abcdefghijklmnopqrstuvwxyz123456789",
    "aws_access_key_id": "AKIAIOSFODNN7EXAMPLE",
    "aws_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "database_url": "postgresql://fakeuser:fakepass123@localhost:5432/testdb",
    
    "jwt_secret": "fake_jwt_secret_key_for_testing",
    
    "openai_api_key": "sk-fake1234567890abcdefghijklmnopqrstuvwxyz123456789012",
    "github_token": "ghp_fake1234567890abcdefghijklmnopqrstuvwxyz",
    
    "private_key": """-----BEGIN PRIVATE KEY-----
[REDACTED_VERY_LOW_[RED...gSj]]AgEAAoIBAQC7VJTUt9Us8cKB
FAKE_KEY_CONTENT_FOR_TESTING_ONLY
-----END PRIVATE KEY-----""",
}

# Fake credentials in comments
# Password: admin123
# API_SECRET=fake_secret_123456789

os.environ["STRIPE_SECRET_KEY"] = "sk_test_fake1234567890"
os.environ["DATABASE_PASSWORD"] = "secret_password_123"
os.environ["API_TOKEN"] = "fake_token_abcdef123456789"

STRIPE_KEY = "sk_test_fake1234567890abcdefghijklmnopqrstuvwxyz"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_PASSWORD = "secret_password123"

def main():
    print("This is a fake py script for testing snugbug")
    
    api_key = "sk_live_fake1234567890abcdefghijklmnopqrstuvwxyz"
    print(f"Using API key: {api_key}")

if __name__ == "__main__":
    main()