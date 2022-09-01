import asyncio
from ably import AblyRest

async def main():
    # automatic close connection
    async with AblyRest('your-ably-api-key') as ably:
        channel = ably.channels.get("channel-name")

asyncio.run(main())
    
