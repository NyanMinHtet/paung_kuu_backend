from app import create_app, db
from app.models.users import Users
from dotenv import load_dotenv

load_dotenv()

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users}
