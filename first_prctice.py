import asyncio 


async def func_one():
    """
    First function that prints weird staff
    """
    while True:
        print("Smth 1...")
        await asyncio.sleep(1)


async def func_two():
    """
    Second function that prints weird staff
    """
    while True:
        print("Smth 2...")
        await asyncio.sleep(2)


async def main():
    """
    Creating and gathering two taks
    """
    first_task = asyncio.create_task(func_one())
    second_task = asyncio.create_task(func_two())
    await asyncio.gather(first_task, second_task)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except asyncio.exceptions.CancelledError:
        print("Getting deffined error")
    else:
        print("Ended without errors")


