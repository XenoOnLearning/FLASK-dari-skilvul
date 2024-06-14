from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return "hello  world"

@app.post("sensor/data/")
def sensor():
    return {
        "temperature": 30,
        "kelembapan": 1,
        "timestamp":"09:09:30",
    }

if__name__ == "__main__"
uvicorn.run(app, host="0.0.0.0", port=8000)