import uvicorn
from fastapi import FastAPI
from router import homework
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from db import models
from db.database import engine

app = FastAPI(
    title="Homework API",
    version="0.0.1",
    terms_of_service="http://localhost:5000",
)
app.include_router(homework.router)

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>FastAPI homework: Docker</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
            </ul>
        </div>
    </body>
</html>
"""


@app.get("/")
def root():
    return HTMLResponse(html)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)


origins = [
    'http://localhost:3000',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)