from sqlalchemy import text

from app.database.connection import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))

        print(result.fetchone())

    print("\n✅ Database Connected Successfully!")

except Exception as e:
    print(e)