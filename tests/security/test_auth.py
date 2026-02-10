import pytest
from api.auth.security import create_access_token, get_current_user

@pytest.mark.asyncio
async def test_jwt_generation_and_decode():
    token = create_access_token({"sub": "tester_user"})
    user = await get_current_user(token)
    assert user == "tester_user"
