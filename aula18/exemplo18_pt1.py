from sqlalchemy import create_engine
import pandas as pd 

host = 'localhost'
user = 'root'
password = ''
database = 'db_aula18'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
