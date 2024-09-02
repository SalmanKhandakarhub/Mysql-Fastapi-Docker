## For migrations
# Initialize Alembic:
    $ cd /path/to/your/project
    $ alembic init app/models/migrations

## Migration files are in the correct location in your Docker container.
# If mysql database with async then should maintain in alembin.ini
    sqlalchemy.url = mysql://root:ows1234@mysqldb/BigFast_db
# Enter the Docker Container
sudo docker compose exec fastapi sh
# Navigate to the directory containing alembic.ini
cd /app
# Show installed Alembic package (verify it's installed)
pip show alembic
# Generate a new migration script
alembic revision -m "initial migration"
alembic revision --autogenerate -m "initial migration"
# Apply the migrations to the database
alembic upgrade head
# Drop all tables (use with caution)
alembic downgrade base