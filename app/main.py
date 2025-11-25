from fastapi import FastAPI

app=FastAPI(title="InnoInspect Backend")

@app.get("/health")
def health_check():
    return{"status": "ok", "message": "InnoInspect backend is running"}