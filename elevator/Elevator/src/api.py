from fastapi import FastAPI, BackgroundTasks
from src.utils import *
from src.checker import *


app = FastAPI()

# app.post(/monitor)
# app.post("start-system/-/{floor_number}")
# app.post("end-system/")

def check_release(request):
    while not request.is_done:
        pass
    return True

def setup():
    elevator.run()

def end():
    elevator.stop()

@app.post("/start-system")
async def start_system(background_tasks: BackgroundTasks):
    if elevator.is_running:
        return "The elevator is already running"
    background_tasks.add_task(setup)
    return "The elevator launched successfully."

@app.post("/end-system")
async def end_system(background_tasks: BackgroundTasks):
    background_tasks.add_task(end)
    return "The elevator is stopped."

@app.post("/inside/{floor_number}")
def send_inside(floor_number: int):
    if elevator.is_stopped:
        return "The elevator is not running. Please launch the elevator first."
    
    request = Request()

    if elevator.curr_floor == floor_number:
        return "You are already at the floor you want to go."

    LIST_FLOOR[floor_number].add_request(request)
    check_release(request)
    return "The request is completed."


@app.post("/outside/{floor_number}")
def send_outside(floor_number: int):
    if elevator.is_stopped:
        return "The elevator is not running. Please launch the elevator first."
    
    try:
        Checker.check_floor(floor_number, FLOOR_NUMS)
    except Exception as e:
        return e

    request = Request()

    if elevator.curr_floor == floor_number:
        return "You are already at the floor you want to go."

    LIST_FLOOR[floor_number].add_request(request)
    check_release(request)
    return "The request is completed."

# uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)