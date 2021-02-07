# couchbase_json_insert

## Preqrequisites
-Install Couchbase Server<br\>
-Install Couchbase Python SDK (3.0)<br\>

## Description
Reads in an array of JSON objects and inserts into Couchbase. The array of JSON objects are parsed into a dictionary of key value pairs before being inserted using collection.upsert_multi().
