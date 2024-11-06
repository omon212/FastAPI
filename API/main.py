from fastapi import FastAPI
from API.routers import load_routers

app = FastAPI(
    title = "eMaktab API",
    description = "This is test eMaktab API"
)

for router in load_routers():
    app.include_router(router=router)