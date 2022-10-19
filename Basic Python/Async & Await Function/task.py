import asyncio

async def main(name):
    print("Hello")
    await asyncio.sleep(2)
    print(name)


async def runner():
    task1 = asyncio.create_task(coro=main("Alamin"))
    task2 = asyncio.create_task(coro=main("Tania"))

    # await task1
    # await task2

    await asyncio.gather(task1, task2)


asyncio.run(runner())