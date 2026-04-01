from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.data import utils
from app.helpers.fetcher import fetch_json


router = APIRouter(prefix="/metrics", tags=["api-controller"])



@router.get("", description="Returns the specified metric's metadata. If no specified metric, returns the available metrics instead")
async def get_metric(metricid: Optional[str] = Query(None, description="Metric ID to fetch")):
    
    if metricid == None:
        return utils.METRIC_IDENTIFIERS

    if metricid not in utils.METRIC_IDENTIFIERS:
        raise HTTPException(status_code=404, detail="Metric not found")

    return await fetch_json(metricid)