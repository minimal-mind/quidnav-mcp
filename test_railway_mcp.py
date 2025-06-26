import asyncio
import httpx
import json


async def test_railway_mcp():
    url = "https://quidnav-mcp-production.up.railway.app"

    async with httpx.AsyncClient() as client:
        try:
            # Test 1: Check if server is alive
            print("Testing server connectivity...")
            response = await client.get(url)
            print(f"Server status: {response.status_code}")

            # Test 2: List available tools
            print("\nTesting tools/list...")
            response = await client.get(f"{url}/tools/list")
            print(f"Tools response: {response.status_code}")
            if response.status_code == 200:
                tools = response.json()
                print(f"Available tools: {json.dumps(tools, indent=2)}")

            # Test 3: Call get_resources tool
            print("\nTesting get_resources...")
            response = await client.post(
                f"{url}/tools/call", json={"name": "get_resources", "arguments": {}}
            )
            print(f"Get resources response: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                print(f"Result preview: {str(result)[:200]}...")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(test_railway_mcp())
