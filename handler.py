import runpod
import httpx

SERVER_URL = "http://127.0.0.1:8000" 


async def process_request(job):
    job_input = job["input"]
    script = job_input['script']
    
    timeout = httpx.Timeout(60)
    async with httpx.AsyncClient(timeout=timeout, verify=False) as client:
        response = await client.post(
            f"{SERVER_URL}/generate_audio",
            json={
                "script": script
            },
        )
    
    return f"Processed: {response.json()}"

# Placeholder code for a dynamic concurrency adjustment function 
def adjust_concurrency(current_concurrency):
    return 2

# Start the Serverless function when the script is run
if __name__ == "__main__":
    runpod.serverless.start({
        "handler": process_request,
        "concurrency_modifier": adjust_concurrency
    })