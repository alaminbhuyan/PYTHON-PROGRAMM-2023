import asyncio

async def main(name):
    print("Hello")
    await asyncio.sleep(2)
    print(name)


async def runner():
    names = ["Alamin", "Tania", "Fatema"]
    tasks = []

    for name in names:
        tasks.append(asyncio.create_task(coro=main(name)))

    await asyncio.gather(*tasks)


asyncio.run(runner())