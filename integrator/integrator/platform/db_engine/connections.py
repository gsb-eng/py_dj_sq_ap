from sqlalchemy import create_engine


# Mysql engine
MYSQL = create_engine("mysql://root:pwd@localhost/test",
                      encoding='latin1', echo=True)
