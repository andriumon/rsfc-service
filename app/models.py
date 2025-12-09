from pydantic import BaseModel
from typing import List

class ResourceAssessmentRequest(BaseModel):
    resource_identifier: str
    
    
class TestIdentifier(BaseModel):
    identifier: str


class IndicatorIdentifier(BaseModel):
    identifier: str


class TestInfo(BaseModel):
    test_id: TestIdentifier
    test_name: str
    test_description: str
    indicator_assessed: str


class Assessment(BaseModel):
    context: str
    type: str
    name: str
    description: str
    dateCreated: str
    license: dict
    assessedSoftware: dict
    checks: list


class TestIdentifierList(BaseModel):
    identifiers: List[TestIdentifier]
