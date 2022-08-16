import asyncio
from ably import AblyRest

async def main():
    async with AblyRest('your-ably-api-key') as ably_client:
        channel = ably_client.channels.get("channel_name")

if __name__ == "__main__":
    print ('call main')
    asyncio.run(main())
