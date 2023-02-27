from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from memory_app.api.search.search import router as searchRouter

app = FastAPI()
app.include_router(searchRouter)

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def search(search_value: str):
    ret = [x for x in range(10)]
    return {"search_value": ret}