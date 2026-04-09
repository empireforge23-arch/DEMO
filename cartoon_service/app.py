app = FastAPI()

# ---- Models ----
class Lead(BaseModel):
    name: str
    email: str
    budget: float
    source: str


# ---- Routes ----
@app.get("/")
def root():
    return {"message": "API is alive. Try not to break it."}


@app.post("/score-lead")
def score_lead(lead: Lead):
    score = 0

    if lead.budget > 1000:
        score += 50
    if lead.source == "ads":
        score += 30

    return {
        "name": lead.name,
        "score": score,
        "status": "high" if score > 50 else "low"
    }