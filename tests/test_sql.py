import pyexcel as pe
import datetime
from textwrap import dedent
from db import Session, Base, Pyexcel, engine

class TestSQL:
    def setUp(self):
        Base.metadata.create_all(engine)
        p1 = Pyexcel(id=0,
                     name="Adam",
                     weight=11.25,
                     birth=datetime.date(2014, 11, 11))
        session = Session()
        session.add(p1)
        p1 = Pyexcel(id=1,
                     name="Smith",
                     weight=12.25,
                     birth=datetime.date(2014, 11, 12))
        session.add(p1)
        session.commit()

    def test_sql(self):
        sheet = pe.load_from_sql(Session(), Pyexcel)
        content = dedent("""
        Sheet Name: pyexcel
        +----+-------+--------+------------+
        | id | name  | weight |   birth    |
        +====+=======+========+============+
        | 0  | Adam  | 11.250 | 2014-11-11 |
        +----+-------+--------+------------+
        | 1  | Smith | 12.250 | 2014-11-12 |
        +----+-------+--------+------------+""").strip('\n')
        assert str(sheet) == content