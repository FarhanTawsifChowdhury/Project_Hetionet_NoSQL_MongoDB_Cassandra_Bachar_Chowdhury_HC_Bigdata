# Project_Hetionet_NoSQL_MongoDB_Cassandra_Bachar_Chowdhury_HC_Bigdata

• Build a database system to model HetioNet
• The database should at least answer the following
questions in the quickest response time:
– Given a disease, what is its name, what are drug names that
can treat or palliate this disease, what are gene names that
cause this disease, and where this disease occurs? Obtain and
output this information in a single query.
– Supposed that a drug can treat a disease if the drug or its
similar drugs (similarity>0.9) up-regulate/down-regulate a
gene, but the location down-regulates/up-regulates the gene
in an opposite direction where the disease occurs. Find all
drugs that can treat a new disease (i.e. the missing edges
between drug and disease excluding existing drugs). Obtain
and output all drugs in a single query.

• A Python command-line client interface for
database creation and query
• Use at least two types of NoSQL stores
(Key-value, Document, Column Family, or
Graph)

# Environment setup:


### install mongoDB:
https://docs.mongodb.com/manual/administration/install-community/


### Use pip to install pymongo:
$ python -m pip install pymongo


### Commands used in terminal to import files into mongoDB are:
mongoimport --db projectDB --collection nodes --type tsv <PATH/TO/FILE.tsv> --headerline
mongoimport --db projectDB --collection edges --type tsv <PATH/TO/FILE.tsv> --headerline


### run code
$ python part1.py


### enter name of disease



### Cassandra Setup

# Prerequisites: Install Java 8

# Download: http://cassandra.apache.org/download/

# Configuration: In conf/cassandra.yaml

### Commands used in terminal to import files into Cassandra are:

COPY node_tsv_import3 (id, name, kind) FROM '/DIRECTORY/nodes.tsv' WITH DELIMITER='\t' AND HEADER=TRUE;
COPY edge_tsv_import (id, name, kind) FROM '/DIRECTORY/edges.tsv' WITH DELIMITER='\t' AND HEADER=TRUE;

### run code
$ python cassandratest3.py

### run code
$ python cassandratest5.py
