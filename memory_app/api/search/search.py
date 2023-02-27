from fastapi import APIRouter, HTTPException
from .searchresponse import SearchResponse

router = APIRouter(
    prefix="/search",
    tags=["search"],
    responses={404: {"description": "Not found"}},
)

list = [
    SearchResponse(
        firstname="Jan",
        surname="Kowalski",
        position="Prezydent",
    ),
    SearchResponse(
        firstname="Andrzej",
        surname="Duda",
        position="Prezydent",
    ),
    SearchResponse(
        firstname="Mateusz",
        surname="Kaczyński",
        position="Prezydent",
    ),
]

@router.get("/")
async def search():
    return []

@router.get("/{search_value}")
async def search(search_value: str = None):
    return list
