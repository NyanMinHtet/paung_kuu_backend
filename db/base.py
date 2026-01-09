# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base
from models.user import User
from models.skill import Skill
from models.task import Task
from models.job import Job
from models.rating import Rating
from models.wallet import Wallet
from models.transaction import Transaction
