import cassandra
from cassandra.cluster import Cluster

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

    return session

def drop_tables(session):
    """
    - drops tables if they already exist
    """
    session.execute("DROP TABLE IF EXISTS artist_songs")

    session.execute("DROP TABLE IF EXISTS artist_song_username")

    session.execute("DROP TABLE IF EXISTS username_song ;")

def create_tables(session):
    """
    - creates tables 
    """
    query = ("CREATE TABLE IF NOT EXISTS artist_songs")
    query = query + ("(sessionId varchar, itemInSession varchar, artist text, song_title text, songs_length varchar, PRIMARY KEY((sessionId, itemInSession), artist , song_title, songs_length))")
    session.execute(query)

    query = ("CREATE TABLE IF NOT EXISTS artist_song_username")
    query = query + ("(session_id varchar, itemInSession varchar, \
                        user_id varchar, firstname_user text, lastname_user text,\
                        artist text, song_title text, \
                        PRIMARY KEY ((session_id, user_id), itemInSession))")
    session.execute(query)

    session.execute("""CREATE TABLE IF NOT EXISTS username_song (song_title text, session_id varchar,
                            itemInSession varchar, firstname_user text, lastname_user text,
                            PRIMARY KEY ((song_title), session_id, itemInSession))""")

def main():
    """
    - creates keyspace sparkifydb and connects to it
    - drops tables
    - creates tables 
    - closes connection
    """
    session = create_keyspace()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()




