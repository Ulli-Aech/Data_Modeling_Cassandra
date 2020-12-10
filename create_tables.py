import cassandra
from cassandra.cluster import Cluster
from cql_queries import create_keyspace, drop_table_queries, create_table_queries

def create_keyspace():
    """
    - connects to cluster on local machine
    - creates keyspace sparkifydb 
    - creates session on keyspace sparkifydb
    """

    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    session.execute("""CREATE KEYSPACE IF NOT EXISTS sparkifydb
    WITH REPLICATION =
    { 'class': 'SimpleStrategy', 'replication_factor' : 1}""")

    session.set_keyspace('sparkifydb')

    return session, cluster

def drop_tables(session):
    """
    - drops tables if they already exist
    """
    for query in drop_table_queries:
        session.execute(query)


def create_tables(session):
    """
    - creates tables 
    """

    for query in create_table_queries:
        session.execute(query)


def main():
    """
    - creates keyspace sparkifydb and connects to it
    - drops tables
    - creates tables 
    - closes connection
    """
    session, cluster = create_keyspace()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()




