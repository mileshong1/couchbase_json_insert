# imports to connect to couchbase
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

#insert options
from couchbase.durability import ClientDurability, ServerDurability, Durability, ReplicateTo, PersistTo
from datetime import timedelta

#imports for .env file
import os
from dotenv import load_dotenv
load_dotenv()

#import for JSON
import json

#import for timing
import time

def connect():
    #connect to cluster using auth
    cluster = Cluster("couchbase://localhost", ClusterOptions(
        PasswordAuthenticator(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    ))
            
    #get travel-sample bucket
    cb = cluster.bucket('json_insert')

    return cb

def create_kv_dict(data):
    kv_dict = dict()

    for row in data:
        key = f"{row['type']}_{row['id']}"

        if (key in kv_dict.keys()):
            print(f"{key} already inserted!")
        else:
            kv_dict[key] = row

    return kv_dict

def insert_batch(collection, batch):
    #build kv dict
    kv_dict = create_kv_dict(batch)

    #upsert_multi
    collection.upsert_multi(kv_dict)

def main():
    #open JSON file
    with open('./travel-sample.json') as f:
        data = json.load(f)

    cb = connect()

    #if we know the data before hand, we could create a collection for each.
    #going to use default_collection here for now. 
    collection = cb.default_collection()

    start_time = time.time()
    insert_batch(collection, data)
    end_time = time.time()

    print(end_time-start_time)

if __name__ == '__main__':
    main()