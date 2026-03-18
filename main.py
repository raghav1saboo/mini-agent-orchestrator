from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from planner import create_plan
from orchestrator import execute_plan

app = FastAPI(title="Mini Agent Orchestrator")

class UserRequest(BaseModel):
    request: str

@app.get("/")
async def root():
    return {"message": "Mini Agent Orchestrator is running. Visit /docs to test the API."}

@app.post("/process-request")
async def process_user_request(user_input: UserRequest):
    """
    Single API endpoint that receives a natural language user request.
    """
    try:
        print(f"Received request: {user_input.request}")
        plan = await create_plan(user_input.request)
        
        results = await execute_plan(plan)
        
        return {
            "input": user_input.request,
            "plan_generated": plan,
            "execution_results": results
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))