from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user, task

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

# Include routers
app.include_router(user.router)
app.include_router(task.router)