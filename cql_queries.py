# CREATE KEYSPACE
create_keyspace = ("""CREATE KEYSPACE IF NOT EXISTS sparkifydb
    WITH REPLICATION =
    { 'class': 'SimpleStrategy', 'replication_factor' : 1}""")

# DROP TABLES 

drop_artist_songs = ("DROP TABLE IF EXISTS artist_songs")

drop_artist_song_username = ("DROP TABLE IF EXISTS artist_song_username")

drop_username_song = ("DROP TABLE IF EXISTS username_song")

# CREATE TABLES

create_artist_songs = ("""CREATE TABLE IF NOT EXISTS artist_songs 
                             (sessionId int, itemInSession int, artist text, 
                             song_title text, songs_length float, 
                             PRIMARY KEY((sessionId, itemInSession), artist,
                             song_title, songs_length))
""")

create_artist_song_username = ("""CREATE TABLE IF NOT EXISTS artist_song_username
                                     (user_id int, session_id int, itemInSession int,
                                      firstname_user text, lastname_user text,
                                      artist text, song_title text,
                                      PRIMARY KEY ((user_id, session_id), itemInSession))
""")

create_username_song = ("""CREATE TABLE IF NOT EXISTS username_song 
                              (song_title text, session_id int,
                               itemInSession int, firstname_user text,
                               lastname_user text,
                               PRIMARY KEY ((song_title), session_id, itemInSession))
""")

# INSERT DATA

insert_artist_songs = ("""INSERT INTO artist_songs (sessionId, itemInSession, artist, 
                                song_title, songs_length)VALUES (%s, %s, %s, %s, %s)
""")

insert_artist_song_username = ("""INSERT INTO artist_song_username (user_id, 
                                    session_id, itemInSession, firstname_user, 
                                    lastname_user, artist, song_title)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s) 
""")

insert_username_song = ("""INSERT INTO username_song (song_title, session_id,
                             itemInSession, firstname_user, lastname_user)
                             VALUES (%s, %s, %s, %s, %s) """)


# SELECT 

query1 = """SELECT artist, song_title, songs_length
             FROM artist_songs
             WHERE sessionId = 338 AND itemInSession = 4"""

query2 = """SELECT artist, song_title, firstname_user, lastname_user 
             FROM artist_song_username
             WHERE user_id = 10 AND session_id = 182 """

query3 = """SELECT firstname_user, lastname_user 
             FROM username_song 
             WHERE song_title = 'All Hands Against His Own' """

# LISTS OF QUERIES 

drop_table_queries = [drop_artist_songs, drop_artist_song_username, drop_username_song]

create_table_queries = [create_artist_songs, create_artist_song_username, create_username_song]