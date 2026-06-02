from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd 
import os 

load_dotenv()
host = os.getenv('DB_host')
user = os.getenv('DB_user')
password = os.getenv('DB_password')
database = os.getenv('DB_database')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
