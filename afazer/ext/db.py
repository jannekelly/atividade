from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy


engine = create_engine('sqlite:///database.db', convert_unicode=True)
db = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


def iniciar_app(app):
    d = SQLAlchemy()
    d.init_app(app)
    init_db()
