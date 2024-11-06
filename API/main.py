from fastapi import FastAPI
from API.routers import load_routers

app = FastAPI(
    title = "Fast API",
    description = "FastAPI"
)

for router in load_routers():
    app.include_router(router=router)