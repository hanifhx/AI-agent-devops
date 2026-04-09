from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AppRequest(BaseModel):
    app_type: str


@app.get("/")
def home():
    return {"message": "Working 🚀"}


@app.post("/generate-ci")
def generate_ci(req: AppRequest):
    return {"ci": f"CI for {req.app_type}"}


@app.post("/generate-k8s")
def generate_k8s(req: AppRequest):
    return {"k8s": f"K8s for {req.app_type}"}
