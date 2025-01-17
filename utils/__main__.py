from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiohttp import ClientSession 
import socket 

def host():
    host_id = "https://"+socket.getfqdn()
    return host_id
    
async def job():
    aio_session = ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
    async with aio_session.get(host()) as response:
       print("✅ online!")
    await aio_session.close()


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=600)

scheduler.start()
