from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
def chat(query: str):
    return {"response": f"Your query was: {query}"}

# Running locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
