from fastapi import FastAPI
from claude_client import analyze_cve

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Claude CVE Analysis Prototype"
    }


@app.post("/analyze")
def analyze(cve_id: str):

    result = analyze_cve(cve_id)

    return {
        "cve": cve_id,
        "analysis": result
    }