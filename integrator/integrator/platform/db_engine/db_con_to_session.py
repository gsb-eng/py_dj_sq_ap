"""
Adding db connections to the session.
"""
from sqlalchemy.orm import sessionmaker

from .connections import MYSQL


# Binding MYSQL engine to the sqlalchey orm session.
Session = sessionmaker(bind=MYSQL)

# create a Session
SESSION = Session()
