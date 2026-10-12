from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import api_router

def create_app():
    app =  FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://harupandi.com", "http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    return app