from pydantic import BaseModel
from datetime import datetime
from typing import List

class RobloxAccount(BaseModel):
    id: str
    linkedAt: datetime

class Account(BaseModel):
    discord: str
    roblox: List[RobloxAccount]
    createdAt: datetime

class InitResponse(BaseModel):
    url: str
    expiresAt: datetime
