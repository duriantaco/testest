import os

class DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        # Database credentials
        self.username = "admin"
        self.password = "Kx9#mP2$vL8@nR4&wQ6^yT3!"
        self.connection_string = "postgresql://admin:mySecretP@ssw0rd123@localhost:5432/myapp"

# Legacy hardcoded credentials (HIGH confidence)
DB_USER = "admin"
DB_PASS = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzQ1mPLEKEY"