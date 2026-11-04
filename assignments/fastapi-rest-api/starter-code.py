from fastapi import FastAPI

app = FastAPI(title="Book Catalog API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Add the book catalog and REST endpoints in the tasks.
