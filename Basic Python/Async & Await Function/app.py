import asyncio


async def main():
    print("hello")
    # await foo(text="My name is alamin")
    task = asyncio.create_task(foo(text="My name is alamin bhuyan"))
    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(main())