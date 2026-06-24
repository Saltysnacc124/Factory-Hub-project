from database.db import engine, Base

# Import all models so SQLAlchemy knows about them
from database.models import (
    Machine,
    Telemetry,
    Alarm,
    ToolChange,
    CycleEvent,
)


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ All database tables created successfully.")


if __name__ == "__main__":
    create_tables()
