import asyncio

async def task():
    print("task started")
    await asyncio.sleep(3)
    print("task completed")


asyncio.run(task())