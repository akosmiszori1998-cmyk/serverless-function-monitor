from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from compute import ComputeFunction
from storage import StorageFunction
from monitoring_system import CloudMonitor

app = FastAPI()
system_monitor = CloudMonitor()
class ComputeRequest(BaseModel):
    name: str
    memory: int
    time: int

class StorageRequest(BaseModel):
    name: str
    memory: int
    data_gb: int

@app.get("/")
def home():
    return {"Message": "Hi! The Cloud Monitor API Server is running!"}

@app.post("/add-compute")
def add_compute_server(request: ComputeRequest):
    try:
        new_server = ComputeFunction(request.name, request.memory, request.time)
        system_monitor.add_function(new_server)
        return {"status": "success", "message": f"Server: {request.name} added"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/add-storage")
def add_storage_service(request: StorageRequest):
    try:
        new_storage = StorageFunction(request.name, request.memory, request.data_gb)
        system_monitor.add_function(new_storage)
        return {"status": "success", "message": f"Storage {request.name} added"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/report")
def get_report():
    total_cost = system_monitor.generate_report()
    return {
        "active_functions": len(system_monitor.active_functions),
        "total_cost": total_cost,
        "currency": "USD"
    }
        