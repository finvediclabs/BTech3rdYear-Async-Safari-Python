from fastapi import FastAPI
import time
import asyncio
from contextvars import ContextVar

app = FastAPI()

# Context var for tracing
request_id_var = ContextVar("request_id", default=None)

# Decorator with side-effect bug
def buggy_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator side-effect: blocking call!")
        time.sleep(1)  # blocks event loop
        return func(*args, **kwargs)
    return wrapper

@app.get("/blocking-io")
async def blocking_io():
    time.sleep(2)  # blocking I/O in async route
    return {"message": "This endpoint blocks the event loop!"}

@app.get("/event-loop-misuse")
async def event_loop_misuse():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.sleep(1))  # event loop misuse
    return {"message": "Misused event loop!"}

@app.get("/decorator-bug")
@buggy_decorator
async def decorator_bug():
    await asyncio.sleep(1)
    return {"message": "Decorator side-effect!"}

@app.get("/context-var-lost")
async def context_var_lost():
    request_id_var.set("abc123")
    await asyncio.sleep(1)
    # context var may be lost in async
    return {"request_id": request_id_var.get()}

@app.get("/tracing-span")
async def tracing_span():
    # Simulate tracing span
    print("Tracing span started")
    await asyncio.sleep(1)
    print("Tracing span ended")
    return {"message": "Tracing span simulated"}
