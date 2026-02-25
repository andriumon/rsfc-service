from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.data import utils
from app.helpers.fetcher import fetch_json


router = APIRouter(prefix="/tests", tags=["api-controller"])


@router.get("")
async def get_test(testid: Optional[str] = Query(None, description="Test ID to fetch (optional)")):

    if testid == None:
        return {
            "available_tests": utils.TEST_IDENTIFIERS,
            "note": "Additionally, you can use the short version of these identifiers (i.e. RSFC-01-2)"
        }

    if testid not in utils.TEST_IDENTIFIERS:
        raise HTTPException(status_code=404, detail="Test not found")

    return await fetch_json(testid)