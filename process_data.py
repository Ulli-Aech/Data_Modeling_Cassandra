import pandas as pd
import re
import os
import glob
import numpy as np
import json
import csv

import cassandra
from cassandra.cluster import Cluster

from cql_queries import insert_artist_songs, insert_artist_song_username, insert_username_song

files = '/event_data'

def process_data(files):
    """
    Takes in string of file location as files and processes eventdata
    into a new csv file 'event_datafile_new.csv'.
    """

    filepath = os.getcwd() + files
    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root,'*'))

    full_data_rows_list = [] 

    for f in file_path_list:
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            csvreader = csv.reader(csvfile) 
            next(csvreader)

            for line in csvreader:
                full_data_rows_list.append(line)


    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))


    #with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
    #    print(sum(1 for line in f))
    return 'event_datafile_new.csv'

def insert_data(session, file):
    """
    Reads data from new datafile csv into tables on Cassandra cluster.
    """
    #file = 'event_datafile_new.csv'

    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:

            session.execute(insert_artist_songs, (line[8], line[3], line[0], line[9], line[5]))

            session.execute(insert_artist_song_username, (line[8], line[3], line[10], line[1], line[4], line[0], line[9]))

            session.execute(insert_username_song , (line[9], line[8], line[3], line[1], line[4]))

def main():
    """
    Processes event data files into new datafile csv and inserts data into 
    tables in sparkifydb.
    """

    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('sparkifydb')

    insert_data(session, process_data(files))

    session.shutdown()
    cluster.shutdown()    

if __name__ == "__main__":
    main()