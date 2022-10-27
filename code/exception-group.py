# Exception Group

import asyncio


async def connect_to_db():
    raise ConnectionError("Not connected")


async def call_api():
    raise ValueError("Quota exceeded!")


async def prepare_request():
    raise KeyError("Sample Key")


async def do_request():
    res = await asyncio.gather(
        connect_to_db(),
        call_api(),
        prepare_request(),
        return_exceptions=True,
    )
    exceptions = [ex for ex in res if isinstance(ex, Exception)]
    if exceptions:
        raise ExceptionGroup("There were exceptions", exceptions)
    

async def have_exception_group():
    await do_request()


async def main():
    await have_exception_group()

if __name__ == "__main__":
    asyncio.run(main())