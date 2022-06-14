
## FastAPI SQL Sample 

### Initialize 

```sh
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt 
```

### Start 

```sh
./start.sh
INFO:     Will watch for changes in these directories: ['/Users/cdecl/temp/fastapi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [23808] using statreload
INFO:     Started server process [23810]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Test

```sh
$ curl -XGET -H 'content-type: application/json' -d '{ "id": 4, "name": "cafe" }' http://localhost:8000/add
{"r":"ok","d":{"id":4,"name":"cafe"}}%

$ curl -XGET -H 'content-type: application/json' http://localhost:8000/select
{"r":[{"name":"cafe","id":4}]}%
```