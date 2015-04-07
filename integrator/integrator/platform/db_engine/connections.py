from sqlalchemy import create_engine

# Sqlite engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Mysql engine
mysql = create_engine("mysql://root:pwd@localhost/test",
                      encoding='latin1', echo=True)
