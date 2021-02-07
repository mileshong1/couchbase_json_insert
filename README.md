# couchbase_json_insert

## Preqrequisites
-Install Couchbase Server<br\>
-Install Couchbase Python SDK (3.0)<br\>

## Description
Reads in an array of JSON objects and inserts into Couchbase. The array of JSON objects are parsed into a dictionary of key value pairs before being inserted using collection.upsert_multi().<br\>

Did not do multi-threading because when inserting into the same bucket, each thread will have to wait for the others. There is nothing gained from doing multi-threaded compared to single-threaded. (source: https://docs.couchbase.com/sdk-api/couchbase-python-client-3.0.0/api/threads.html#multiple-threads)
