#####     Tal Bachar     #####
#####  Farhan Chowdhury  #####
##### CSCI 49371 Project #####

### Commands used in terminal to import files into Cassandra are:
#COPY node_tsv_import3 (id, name, kind) FROM '/DIRECTORY/nodes.tsv' WITH DELIMITER='\t' AND HEADER=TRUE;
#COPY edge_tsv_import (id, name, kind) FROM '/DIRECTORY/edges.tsv' WITH DELIMITER='\t' AND HEADER=TRUE;

from cassandra.cluster import Cluster

KEYSPACE = "test_keyspace"
cluster = Cluster(['127.0.0.1'])
#cluster = Cluster()
session = cluster.connect("test_keyspace")

#Creating KEYSPACE
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS %s
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """ % KEYSPACE)

#Query for loading the database table
rows = session.execute("SELECT * FROM node_tsv_import3")
for row in rows:
    print(row.id, row.name, row.kind)
print("Finished")

rows = session.execute("SELECT * FROM node_tsv_import2")
for row in rows:
    print(row.id, row.name, row.kind)
print("Finished")

rows = session.execute("SELECT * FROM edges_tsv_import;")
for row in rows:
    print(row.id, row.name, row.kind)
print("Finished")

#closing Cassandra connection
session.shutdown()
