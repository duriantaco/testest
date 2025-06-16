import os
import requests

AWS_ACCESS_KEY = "[REDACTED_VERY_LOW_[RED...UCT]]ION"
AWS_SECRET_KEY = "[REDACTED_VERY_LOW_[RED...ion]]KEY"
STRIPE_LIVE_KEY = "sk_live_51H7XYZ987654321098765"
OPENAI_API_KEY = "sk-[REDACTED_VERY_LOW_[RED...xyz]]"
ANTHROPIC_KEY = "sk-ant-api03-[REDACTED_VERY_LOW_[RED...rst]]uvwxyz"

GOOGLE_API_KEY = "[REDACTED_VERY_LOW_[RED...pqr]]"
FIREBASE_KEY = "[REDACTED_VERY_LOW_[RED...nop]]"

GITHUB_TOKEN = "[REDACTED_VERY_LOW_[RED...nop]]"
GITHUB_PAT = "ghp_mainbranch567890abcdefghijklmnopqr"

class DatabaseConfig:
    def __init__(self):
        self.host = "prod-db.company.com"
        self.username = "dbadmin" 
        self.password = "P@ssw0rd!2024#Secure" 
        self.connection_string = "postgresql://admin:Pr0ductionP@ss@prod-db:5432/maindb"

os.environ["STRIPE_SECRET_KEY"] = "sk_live_production234567890123"
os.environ["DATABASE_PASSWORD"] = "SecureDbP@ssw0rd2024!"
os.environ["API_TOKEN"] = "prod_token_abcdefghijklmnop123"
os.environ["JWT_SECRET"] = "productionJWTsecret!2024@secure"

# Production API client
class ProductionAPI:
    def __init__(self):
        # These look like real production keys (HIGH confidence)
        self.openai_key = "[REDACTED_VERY_LOW_[RED...ijk]]"
        self.stripe_key = "[REDACTED_VERY_LOW_[RED...789]]"
        self.aws_key = "[REDACTED_VERY_LOW_[RED...ABC]]DEF"
        self.aws_secret = "productionAWSsecret/Key/123456789012345"
        
    def authenticate(self):
        headers = {
            'Authorization': f'Bearer {self.openai_key}',
            'X-API-Key': self.stripe_key
        }
        return headers


TEST_STRIPE_KEY = "sk_test_fake1234567890abcdef"
SAMPLE_AWS_KEY = "AKIATESTKEY123456789EXAMPLE"
DUMMY_OPENAI_KEY = "sk-dummy1234567890abcdef"
MOCK_GITHUB_TOKEN = "ghp_mock1234567890abcdef" 
EXAMPLE_API_KEY = "example_api_key_1234567890"  

os.environ["TEST_DATABASE_PASSWORD"] = "fake_password_123"
os.environ["SAMPLE_JWT_SECRET"] = "test_jwt_secret_placeholder"
os.environ["DUMMY_API_TOKEN"] = "dummy_token_abcdefghijk"

class TestConfig:
    def __init__(self):
        self.test_api_key = "sk-test_1234567890abcdefghijklmnop"
        self.mock_aws_key = "AKIATESTKEY1234567890"
        self.sample_token = "sample_token_1234567890abcdefghij"
        self.fake_password = "fake_database_password_123"
        self.dummy_secret = "dummy_secret_placeholder"


TWILIO_ACCOUNT_SID = "ACprod1234567890abcdefghijklmnop"
TWILIO_AUTH_TOKEN = "prodauth1234567890abcdefghijklmn"
TEST_TWILIO_SID = "ACtest1234567890abcdefghijklmn"

SENDGRID_API_KEY = "SG.ProductionSendGrid12.[REDACTED_VERY_LOW_[RED...rod]]"
TEST_SENDGRID_KEY = "SG.TestSendGrid12.fake1234567890abcdef"

STRIPE_WEBHOOK_SECRET = "whsec_production1234567890abcdefghijklmnopqr"
TEST_WEBHOOK_SECRET = "whsec_fake_test_webhook_123456"
GITHUB_WEBHOOK_SECRET = "webhook_prod_secret_123456789abcdef"
SAMPLE_WEBHOOK = "webhook_sample_dummy_secret"

OAUTH_CLIENT_SECRET = "production_oauth_secret_abcdefghijklmnop"
OAUTH_CLIENT_ID = "prod_client_id_123456789"
TEST_OAUTH_SECRET = "fake_oauth_secret_for_testing"
SAMPLE_CLIENT_ID = "example_client_id_12345"

REDIS_PASSWORD = "RedisSecure!2024@Production"
REDIS_URL = "redis://admin:RedisP@ss!@prod-redis:6379"
TEST_REDIS_PASSWORD = "fake_redis_password_123"
SAMPLE_REDIS_URL = "redis://testuser:dummy_pass@localhost:6379"

def get_api_credentials(environment="production"):
    if environment == "production":
        return {
            "openai": "[REDACTED_VERY_LOW_[RED...lmn]]",
            "stripe": "[REDACTED_VERY_LOW_[RED...789]]",
            "aws_key": "[REDACTED_VERY_LOW_[RED...345]]6789",
            "aws_secret": "LiveProjectAWSsecret/Key/1234567890"
        }
    else:
        return {
            "openai": "sk-test_fake_development_key",
            "stripe": "sk_test_sample_123456789",
            "aws_key": "AKIATESTFAKEKEY123456",
            "aws_secret": "fake_aws_secret_for_testing"
        }

MIXED_CONFIG = {
    "prod_database_url": "postgresql://admin:ProductionDB2024!@prod-db:5432/maindb",
    "prod_api_key": "live_api_key_abcdefghijklmnop123456789",
    "prod_webhook": "whsec_live_webhook_secret_abcdefghijk",
    
    "test_database_url": "postgresql://testuser:fake_password@localhost/testdb",
    "sample_api_key": "sample_api_key_dummy_placeholder",
    "mock_webhook": "whsec_fake_webhook_for_testing"
}

def main():
    print("Loading configuration...")
    
    api_client = ProductionAPI()
    headers = api_client.authenticate()
    
    test_config = TestConfig()
    test_key = test_config.test_api_key
    
    print("Configuration loaded successfully")
    print(f"Production API key: {api_client.openai_key[:20]}...")
    print(f"Test API key: {test_key[:20]}...")
    
    prod_creds = get_api_credentials("production")
    test_creds = get_api_credentials("test")
    
    return {
        "production": prod_creds,
        "testing": test_creds
    }

if __name__ == "__main__":
    main()