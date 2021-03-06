# Couchbase JSON Insert Tool

## Preqrequisites
-Install Couchbase Server<br/>
-Install Couchbase Python SDK (3.0)<br/>
-Download travel-sample.json file from Couchbase sample data.

## Description
Reads in an array of JSON objects and inserts into Couchbase. The array of JSON objects are parsed into a dictionary of key value pairs before being inserted using collection.upsert_multi().<br/>

## How to Use:
First, place the "travel-sample.json" file in the working directory. Currently, it is under the assumption of a fixed schema (in this case, on the travel-sample data). Change the way the key is created in the create_kv_dict() function as necessary to your schema. <br/>

Then, run:
```
python3 json_insert_singlethread.py
```
Go back to the Couchbase server and verify that your data has been inserted into the correct bucket.
