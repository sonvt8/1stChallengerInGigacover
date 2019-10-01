import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import os.path
import sys, traceback
from config_sample import config_string

# Load configuration file
file_exists = os.path.isfile('config.py')
if file_exists:
    from config import USER, PASSWD, DB, HOST, PORT
else:
    with open("config.py", "a+") as f:
        f.write(config_string)
        print("File config.py not found. Please create one by copying from config.sample.py")
        sys.exit(1)


class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user   = USER,
        passwd = PASSWD,
        host   = HOST,
        port   = PORT,
        db     = DB,
    )
    engine = db.create_engine(url)
    session = sessionmaker(bind= engine)()

    def __init__(self):
        try:
            self.connection = self.engine.connect()
            print("Hura!!!Successfully connect to database...")
        except Exception:
            print("Ops!!!You have got fail connection")
            sys.exit(1)

    # Using RAW SQL to querry
    def fetchByQyery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery.fetchall():
            print(data)
