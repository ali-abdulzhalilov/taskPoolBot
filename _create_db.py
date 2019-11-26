from app import db

db.init_db()

for _t in db.Base.metadata.tables:
   print("Table: ", _t)
