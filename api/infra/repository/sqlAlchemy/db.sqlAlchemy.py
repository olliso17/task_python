from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean

Base = declarative_base()


class TodoList(Base):
    __tablename__ = 'todo_list'
    id = Column(String, primary_key=True)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    deleted_at = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    name = Column(String, nullable=False)
    type_task = Column(String, nullable=False)
    user_id = Column(String, foreign_key = True)


engine = create_engine("sqlite:///db.sqlite3")


connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

Main().run()

connection.close()
