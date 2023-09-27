from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Banks(Base):
    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True)
    bank_name = Column(String(100), nullable=False)
    score = Column(Integer, nullable=False)
    
    
class Hypoptheca(Base):
    __tablename__ = 'hypotheca'
    id = Column(Integer, primary_key=True)
    bank_id= Column(Integer, ForeignKey('banks.id'), nullable=False)
    sunn_over = Column(String(100), nullable=False)
    bet = Column(String(50), nullable=False)
    contribution_rate = Column(String(200), nullable=False)   
    

class Cards(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    bank_id= Column(Integer, ForeignKey('banks.id'), nullable=False)
    cashback = Column(String(100), nullable=False)
    service = Column(String(50), nullable=False)
    interest_per_balance = Column(String(200), nullable=False)       
      