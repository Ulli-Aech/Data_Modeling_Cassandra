import pandas as pd
import numpy as np
import cassandra
from cassandra.cluster import Cluster
from cql_queries import query1, query2, query3

def test_queries(session, query):
    """
    Takes in a query and returns the output in a pandas dataframe.
    """
    rows = session.execute(query)
    output = pd.DataFrame(rows)
    
    return output.head()

def main():
    """
    Tests the queries in cql_queries.py on the tables in sparkify db 
    and prints the output as a dataframe. 

    - creates connection and session on cluster
    - tests queries
    - closes session and connection
    """
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('sparkifydb')

    print("Result Query 1")
    print(test_queries(session, query1))
    print("\n")
    print("Result Query 2")
    print(test_queries(session, query2))
    print("\n")
    print("Result Query 3")
    print(test_queries(session, query3))   

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()