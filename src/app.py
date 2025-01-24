from database.interaction.base import init_db
from general import app, db

with app.app_context():
    db.create_all()
    init_db()
    print("Created all?")
