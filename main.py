from fastapi import FastAPI

app = FastAPI(title="TestApp")

@app.get('/items')
async def list_items():
    return []

@app.get('/health')
async def health_check():
    return {"status": "ok"}

@app.get('/test_data')
async def get_test_data():
    return {"message": "This is test data"}
