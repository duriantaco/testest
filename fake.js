
const config = {
    stripeApiKey: "sk_test_51234567890abcdefghijklmnopqrstuvwxyz123456789",
    awsAccessKeyId: "AKIAIOSFODNN7EXAMPLE",
    awsSecretAccessKey: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    
    databaseUrl: "postgresql://fakeuser:fakepass123@localhost:5432/testdb",
    
    jwtSecret: "fake_jwt_secret_key_for_testin",
    
    openaiApiKey: "sk-fake1234567890abcdefghijklmnopqrstuvwxyz123456789012",
    githubToken: "ghp_fake1234567890abcdefghijklmnopqrstuvwxyz",
    
    privateKey: `-----BEGIN PRIVATE KEY-----
[REDACTED_VERY_LOW_[RED...gSj]]AgEAAoIBAQC7VJTUt9Us8cKB
FAKE_KEY_CONTENT_FOR_TESTING_ONLY
-----END PRIVATE KEY-----`,
};

// Fake credentials in comments
// Password: admin123
// API_SECRET=fake_secret_123456789

process.env.STRIPE_SECRET_KEY = "sk_test_fake1234567890";
process.env.DATABASE_PASSWORD = "super_secret_password_123";
process.env.API_TOKEN = "fake_token_abcdef123456789";

class ApiClient {
    constructor() {
        this.apiKey = "sk_live_fake1234567890abcdefghijklmnopqrstuvwxyz";
        this.clientSecret = "fake_client_secret_abcdef123456789";
    }
    
    async makeRequest(endpoint) {
        const headers = {
            'Authorization': `Bearer ${this.apiKey}`,
            'X-Client-Secret': this.clientSecret
        };
        
        console.log(`Making request to ${endpoint} with headers:`, headers);
        return fetch(endpoint, { headers });
    }
}

const oauthConfig = {
    clientId: "fake_client_id_123456789",
    clientSecret: "fake_client_secret_abcdefghijklmnopqrstuvwxyz",
    redirectUri: "https://localhost:3000/auth/callback",
    scope: "read write"
};

const dbConnection = {
    host: "localhost",
    port: 5432,
    database: "myapp",
    username: "dbuser",
    password: "fake_db_password_123456789",
};

const WEBHOOK_SECRET = "whsec_fake1234567890abcdefghijklmnopqrstuvwxyz";

function main() {
    console.log("This is a fake JS script for testing snugbug");
    
    const twilioAccountSid = "ACfake1234567890abcdefghijklmnopqr";
    const twilioAuthToken = "fake1234567890abcdefghijklmnopqr";
    
    console.log(`Using Twilio SID: ${twilioAccountSid}`);
    console.log(`Using Auth Token: ${twilioAuthToken}`);
    
    const slackWebhook = "https://hooks.slack.com/services/T123456789/B123456789/fake1234567890abcdefghijklmn";
    console.log(`Slack webhook: ${slackWebhook}`);
}

module.exports = {
    config,
    apiKey: "sk_test_fake_export_key_123456789",
    secrets: {
        stripe: "sk_live_fake1234567890abcdefghijklmnopqrstuvwxyz",
        aws: "AKIAIOSFODNN7EXAMPLE",
        database: "postgresql://user:fake_pass_123@db:5432/prod"
    }
};

if (require.main === module) {
    main();
}