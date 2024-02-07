from database import Base
from sqlalchemy import Coulumn, Integer, Boolean ,Float,String

class transaction(Base):
    __tablename__= 'transaction'

    id = Coulumn(Integer,primary_key=True,index=True)
    account = Coulumn(Float)
    category = Coulumn(String)
    description = Coulumn(Boolean)
    data= Coulumn(String)
