from sqlalchemy import create_engine
from model.models import Base, Banks
from parsing_data.card_parsing import card_parsing
from sqlalchemy.orm import Session, sessionmaker
from random import randint

engine = create_engine("postgresql+psycopg2://postgres:190687@localhost/agregate_system")


# Base.metadata.create_all(engine)
res = card_parsing()
end_res = set()
for i in res:
    end_res.add(i["bank"])


session = Session(bind=engine)

for i in end_res:
    bank = Banks(bank_name= i, score =randint(3, 5))
    session.add(bank)
    session.commit()
    