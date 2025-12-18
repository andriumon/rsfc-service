

# RSFC API Service

A REST API to call RSFC (Research Software FAIRness Checks) via requests.

## API endpoints

- GET /benchmarks/{benchmark_id}
- GET /metrics/{metric_id}
- GET /tests/{test_id}
- POST /assess/{repo_url}/{test_id}


## Usage

Preferably in a virtual environment and inside the app/ directory, run the following to run the app:

```
uvicorn main:app
```

**Note**: The application will try to pull the docker image for RSFC, which is strictly necessary.

After the preparations are done, you can perform requests to the API. Here are some examples:

- Fetch a benchmark using its id

```
curl -G "http://localhost:8000/benchmarks/" \
  -H "Accept: application/ld+json" \
  --data-urlencode "benchmark_id=https://w3id.org/rsfc/benchmark/FAIR4RS"

```

- Fetch a metric using its id

```
curl -G "http://localhost:8000/metrics/" \
  -H "Accept: application/ld+json" \
  --data-urlencode "metric_id=https://w3id.org/everse/i/indicators/software_has_license"
```

- Fetch a test using its id

```
curl -G "http://localhost:8000/tests/" \
  -H "Accept: application/ld+json" \
  --data-urlencode "test_id=https://w3id.org/rsfc/test/RSFC-01-1"

```

- Perform an assessment on a repository

```
curl -X POST "http://localhost:8000/assess/" \
  -H "Content-Type: application/json" \
  -d '{
    "resource_identifier": "https://github.com/oeg-upm/rsfc"
  }'
```

