# Data_Modeling_Cassandra
Data Modeling with Apache Cassandra
  
  
*An Udacity Data Engineer Nanodegree project*

## Content
- [Description](#description)
- [Data](#data)
- [Cassandra Database](#cassandra-database)
- [Workflow](#workflow)
- [Repository Organization](#repository-organization)
- [Links](#links)

## Description  

In this project I used Python to build an ETL pipeline and Cassandra to show data modeling. The subject of the project is the fictional music streaming provider "Sparkify", which is in need of a database to analyze their data generated from the app.  
The tables in the cassandra keyspace 'sparkifydb' are build to answer three different queries. The queries are given in the [Cassandra Database](#cassandra-database) section. 

## Data  

The data used for this project consists out of one directory with 30 csv files. The files contain event data for every event of user activity that happended in the app during one day. Each event in the csv has 19 columns and the number of rows varies per day/file.
An ETL pipeline is used to process the data from the different csv files into one event datafile named <code>event_data_file.csv</code> which has 6821 rows. This file is used to insert the data in the different tables in the Cassandra keyspace.  

![Screenshot of table head event_datafile_new.csv](/images/image_event_datafile_new.jpg "event datafile after processing")

All data was provided by Udacity as part of the data engineer nanodegree. 

## Cassandra Database  

The database is named "sparkifydb" and consists out of the following tables:  

### - artist_songs table:  
This table is modeled to query for the artist(name), songtitle and songlength based on session ID and nr. of item streamed in session.  
Columns: sessionId, itemInSession, artist, song_title, songs_length  
**Primary Key: sessionId, itemInSession (composite partition key without clustering columns) **  

The artist_songs table is modeled to this query:  
<code>
    """SELECT artist, song_title, songs_length  
        FROM artist_songs  
        WHERE sessionId = 338 AND itemInSession = 4"""
</code>  
         
### - artist_song_username table: 
The table is modeled to query for artist(name), songtitle, firstname of the user and lastname of the user based on user ID and session ID.  
Columns: user_id, session_id, itemInSession, firstname_user, lastname_user, artist, song_title   
**Primary Key: (user_id, session_id), itemInSession (compound primary key with a composite partition key)**  

The artist_song_username table is modeled to this query:  
<code>
     """SELECT artist, song_title, firstname_user, lastname_user   
         FROM artist_song_username  
         WHERE user_id = 10 AND session_id = 182 """
</code>  
         
### - username_song table:  
It is modeled to query for the firstname and lastname of the users based on a songtitle that was streamed.   
Columns: song_title, session_id, itemInSession int, firstname_user, lastname_user
**Primary Key: (song_title), session_id, itemInSession (compound primary key with a simple partition key and two clustering columns)**

The username_song table is modeled to this query:  
<code>
      """SELECT firstname_user, lastname_user   
         FROM username_song   
         WHERE song_title = 'All Hands Against His Own' """
</code>  

## Workflow
  
1) I started out with working through the <code>working_nb.ipynb</code> jupyter notebook. In the first part of the notebook the data from the csv files in the event_data directory is processed into the event_datafile_new.csv   

2) The second part of the notebook is dedicated to the Cassandra code to build the keyspace and tables based on three different questions/queries. 

**Questions:**  
**1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4**   
**2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182**        
**3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'**
 
example CQL create table query: 
<code>create_artist_songs = ("""CREATE TABLE IF NOT EXISTS artist_songs   
                             (sessionId int, itemInSession int, artist text,   
                             song_title text, songs_length float,   
                             PRIMARY KEY(sessionId, itemInSession))  
""")</code>
  
3) After creating each table and inserting data into it, the code was tested by querying the tables. The output of each query was saved in a pandas dataframe for readability. 

![Screenshot of the output of query2 as a pandas dataframe](/images/df_query2_output.jpg "DF output query2")

The project instructons by Udacity stop with the end of the notebook. 
  
4) Based on the code in the jupyter notebook I tried to build an ETL pipeline in Python with a similiar structure as in the [PostgreSQL Data Modeling](https://github.com/Ulli-H/Data_Modeling_Postgres) project.

  
5) In the end I confirmed that the process is successfull by running the files in this order:
- create_tables.py
- process_data.py
- test.py (to query the tables and show the resulting dataframes)


## Repository Organization

1) The event_ data directory contains seperate csv files with the event data. 
  
2) The images directory contains two the two images used in the readme file. 

3) The python files consist out of the create_tables.py which creates the sparkify database and necessary tables, the process_data.py which extracts the data from the data files and inserts them into the database and the cql_queries.py with the queries used in create_tables.py and process_data.py  


## Links

[Repository](https://github.com/Ulli-H/Data_Modeling_Cassandra)  
