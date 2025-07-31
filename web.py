from pygbag import aio as asyncio
from pygbag.aio import serve
import main
import os

async def serve_game():
    port = int(os.environ.get("PORT", 8000))
    await serve(main.main, "0.0.0.0", port)

asyncio.run(serve_game())
