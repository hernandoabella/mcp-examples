from pydantic import BaseModel

class MCPRequest(BaseModel):
    request_id: str
    action: str
    user_id: str

class MCPResponse(BaseModel):
    request_id: str
    result: dict
