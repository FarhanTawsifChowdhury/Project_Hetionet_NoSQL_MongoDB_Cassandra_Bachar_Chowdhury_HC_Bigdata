#####     Tal Bachar     #####
#####  Farhan Chowdhury  #####
##### CSCI 49371 Project #####

### Commands used in terminal to import files into Cassandra are:
#COPY node_tsv_import3 (id, name, kind) FROM '/DIRECTORY/nodes.tsv' WITH DELIMITER='\t' AND HEADER=TRUE;
#COPY edge_tsv_import (id, name, kind) FROM '/DIRECTORY/edges.tsv' WITH DELIMITER='\t' AND HEADER=TRUE;


from cassandra.cluster import Cluster

KEYSPACE = "test_keyspace"
#cluster = Cluster(['127.0.0.1'])
cluster = Cluster()
session = cluster.connect("test_keyspace")

#Setting keyspace . . .
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS %s
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """ % KEYSPACE)

    #session.set_keyspace(KEYSPACE)

#   Creating table . . .(Have to change the table name after every run)
session.execute("""
    CREATE TABLE Disk01 (id text PRIMARY KEY,
                                  name text, kind text);
                                  """)

prepared = session.prepare("""
        INSERT INTO Disk01 (id, name, kind)
        VALUES(?, ?, ?)
        """)

#Importing the datasets
with open('/home/farhan/Downloads/project1_hetionet/project1_hetionet/nodes.tsv', "r") as hnodes:
    data = hnodes.readlines()
    for node in data:
        columns=node.split("\t")
        id=columns[0]
        name=columns[1]
    kind=columns[2]

    session.execute(prepared, [id, name, kind])
    rows = session.execute("SELECT * FROM node_tsv_import4")
    for row in rows:
        print(row.id, row.name, row.kind)
    print("Finished")

#closing the file
hnodes.close()

#closing Cassandra connection
session.shutdown()
