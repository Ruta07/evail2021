from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import MetaData
from sqlalchemy_searchable import make_searchable


#Custom Schema
SQLALCHEMY_DATABASE_SCHEMA = "public"

metadata = MetaData(schema=SQLALCHEMY_DATABASE_SCHEMA) if SQLALCHEMY_DATABASE_SCHEMA is not None else None
db = SQLAlchemy(metadata=metadata)


#To apply sqlalchemy searchable on all models
make_searchable(db.metadata)
