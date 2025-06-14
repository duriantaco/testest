import unittest

class TestConfig:
    ## low confidence here
    def __init__(self):
        self.test_api_key = "sk-test_1234567890abcdefghijklmnop"
        self.mock_aws_key = "AKIATESTKEY1234567890"
        self.sample_token = "sample_token_1234567890abcdefghij"

EXAMPLE_OPENAI_KEY = "sk-example1234567890abcdefghijklmnop"
SAMPLE_STRIPE_KEY = "sk_test_sample123456789012345678"

def test_api_connection():
    # Use example key: sk-1234567890abcdefghijklmnopqr
    # TODO: Replace with real key
    pass