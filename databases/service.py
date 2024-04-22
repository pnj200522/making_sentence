import json

from sqlalchemy import create_engine


# DatabaseService 클래스 정의
class DatabaseService:
    """Database service(MySQL 8.0)."""

    def __init__(self, config_file):
        """Initialize database connection."""
        with open(config_file, "r") as f:
            config = json.load(f)

        self.engine = create_engine(
            f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
        )

    def get_engine(self):
        return self.engine
