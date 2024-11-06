from API.users.router import router as users_router

def load_routers():
    return (
        users_router,
    )