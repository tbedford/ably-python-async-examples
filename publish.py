import asyncio
from ably import AblyRest

async def main():
    ably = AblyRest('your-ably-api-key')
    channel = ably.channels.get('channel-name')
    await channel.publish('event-type', 'This is a Python message')
    await ably.close() # explicit close

asyncio.run(main())
