import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list in sql_queries.py
    """


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list in sql_queries.py
    """



def main():
    """    
    - Connects to Redshift.  
    
    - Loads data from Amazon S3 to Amazon Redshift  
    
    - Drops (if exists) and Creates the tables. 
    
    - Finally, closes the connection. 
    """



if __name__ == "__main__":
    main()