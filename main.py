from httpx import AsyncClient
from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("quidnav")
client = AsyncClient()

QUIDNAV_URL = "https://www.quidnav.com/api/"


# tools
@mcp.tool(
    description="Returns max 50 online financial resources",
)
async def get_resources():
    response = await client.get(QUIDNAV_URL + "resources")
    response.raise_for_status()
    return response.json()


# railway serer
if __name__ == "__main__":
    uvicorn.run(mcp.app, host="0.0.0.0", port=8000)
