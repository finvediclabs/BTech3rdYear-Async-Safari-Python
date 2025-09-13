import httpx
import asyncio

ENDPOINTS = [
    "/blocking-io",
    "/event-loop-misuse",
    "/decorator-bug",
    "/context-var-lost",
    "/tracing-span"
]

async def load_test():
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        for ep in ENDPOINTS:
            resp = await client.get(ep)
            print(f"{ep}: {resp.status_code} {resp.text}")

if __name__ == "__main__":
    asyncio.run(load_test())
