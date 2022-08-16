import asyncio
from ably import AblyRest

async def main():
    client = AblyRest('your-ably-api-key')
    channel = client.channels.get('random-channel')
    await channel.publish('event-type', 'This is a Python message')
    await client.close()

asyncio.run(main())
