from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine(r"sqlite:///DataEntryApp/training_data.db")

Base = declarative_base()

class training_data(Base):
    __tablename__ = "training_data"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    user = Column(String, nullable=False)
    agent = Column(String, nullable=True)

Base.metadata.create_all(engine)