from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="BookReview API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

# Instrument Prometheus metrics at /metrics
Instrumentator().instrument(app).expose(app)
