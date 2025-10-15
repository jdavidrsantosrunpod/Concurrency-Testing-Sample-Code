from fastapi import FastAPI
import asyncio
# Create FastAPI instance
app = FastAPI()

# Example root endpoint
@app.get("/health")
async def health():
    return {"message": "Hello, FastAPI is running!"}

# Example POST endpoint
@app.post("/generate_audio")
async def generate_audio(data: dict):
    print("============ generating audio ...")
    for i in range(15):
        print(f"=================== i :{i}")
        await asyncio.sleep(1)
    return {"response": data}
