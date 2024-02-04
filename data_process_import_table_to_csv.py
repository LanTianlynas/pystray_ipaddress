'''下面的代码只适合SQLite DB'''

# from main.model.symbol_model import Symbol
# import pandas as pd
# from sqlalchemy import create_engine
#
# # SQLAlchemy connectable
# cnx = create_engine("mysql://root:makemoney@mysql:3306/market_data_dev").connect()
#
# # table named 'contacts' will be returned as a dataframe.
# df = pd.read_sql_table('symbols', cnx)
# df.to_csv("symbols.csv", index=False)

# # Step1: import
# import pandas as pd
# from sqlalchemy import create_engine
#
# # Step2: create_engine
# connection_string = "mysql://root:makemoney@mysql:3306/market_data_dev"
# engine = create_engine(connection_string)
#
# # Step3: select table
# print (engine.symbols())
#
# # Step4: read table
# table_df = pd.read_sql_table('symbols', engine)
# table_df.head()


"""下面的代码适合所有DB, 但是测试中报错了"""
"""df = pd.read_sql(query.all(), engine)"""
"""raise TypeError("Query must be a string unless using sqlalchemy.")"""

# import pandas as pd
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# import sqlalchemy as db
#
# connection_string = "mysql://root:makemoney@mysql:3306/market_data_dev"
# engine = create_engine(connection_string, echo=False)
# session = Session(engine)
#
# # sqlalchemy: Reflect the tables
# Base = automap_base()
# Base.prepare(engine, reflect=True)
#
# # Mapped classes are now created with names by default matching that of the table name.
# Table_Name = Base.classes.symbols
#
# # Example query with filtering
# query = session.query(Table_Name).filter()
#
# # Convert to DataFrame
# df = pd.read_sql(query.all(), engine)
# df.head()

"""下面的代码适合所有DB Hu Ray!"""
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

connection_string = "mysql://root:makemoney@mysql:3306/market_data_dev"
engine = create_engine(connection_string, echo=False)
session = Session(engine)

# sqlalchemy: Reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Mapped classes are now created with names by default matching that of the table name.
SQLA_Table = Base.classes.symbols

cols = [c.name for c in SQLA_Table.__table__.columns]
pk = [c.name for c in SQLA_Table.__table__.primary_key]
result_list = session.query(SQLA_Table).all()
tuplefied_list = [(getattr(item, col) for col in cols) for item in result_list]

df = pd.DataFrame.from_records(tuplefied_list, index=pk, columns=cols)
df.to_csv("symbols.csv", index=False)