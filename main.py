import uvicorn
from httpx import AsyncClient
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("quidnav")
client = AsyncClient()

QUIDNAV_URL = "https://www.quidnav.com"


# resources
@mcp.tool(
    description="Returns max 50 online financial resources",
)
async def get_resources():
    response = await client.get(QUIDNAV_URL + "/api/resources")
    return response.text


# local server
if __name__ == "__main__":
    uvicorn.run(mcp.app)
