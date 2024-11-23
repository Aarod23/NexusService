import aiohttp
from typing import List, Dict, Union
from .models import InitResponse, Account
from .errors import APIError
from .utils import get_headers

BASE_URL = "https://nexus.tychosystems.xyz/api/v1"

class SubjectTypes:
    Roblox = 0
    Discord = 1

class Nexus:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def _fetch(self, url: str, params: dict) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=get_headers(self.api_key), params=params) as response:
                if response.status != 200:
                    raise APIError(response.status, await response.text())
                return await response.json()

    async def initiate_verification_session(self, subject_type: int, sub: str) -> InitResponse:
        data = await self._fetch(f"{BASE_URL}/init", {"type": subject_type, "sub": sub})
        return InitResponse(**data)

    async def query_account(self, subject_type: int, sub: str) -> Account:
        data = await self._fetch(f"{BASE_URL}/query", {"type": subject_type, "sub": sub})
        return Account(**data)

    async def query_bulk_accounts(self, subject_type: int, subs: List[str]) -> Dict[str, Union[Account, List[Account], None]]:
        data = await self._fetch(f"{BASE_URL}/query/bulk", {"type": subject_type, "sub": ",".join(subs)})
        return data
