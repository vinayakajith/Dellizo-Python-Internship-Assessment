# this program will check a bunch of websites at the same time
# and tell me how long they take to respond + status code

import asyncio  # this is needed for async programming in python
import aiohttp  # this is for making async http requests
import time     # this is just to measure how long it takes

# ok here is a list of websites i want to check
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://fastapi.tiangolo.com"
]

# this function will go to one website and get status + time taken
# session = aiohttp session (so we can reuse connections)
# url = the website to check
async def fetch_url(session, url):
    start_time = time.perf_counter()  # start the timer
    try:
        # making the request (async way)
        async with session.get(url) as response:
            # read the page (this is needed otherwise the request is not complete)
            await response.text()
            elapsed = time.perf_counter() - start_time  # time taken
            return {
                "url": url,
                "status": response.status,  # http status code like 200
                "time": round(elapsed, 2)   # rounded time
            }
    except Exception as e:
        # if something goes wrong (like no internet), handle it here
        elapsed = time.perf_counter() - start_time
        return {
            "url": url,
            "status": f"Error: {e}",  # put the error in status
            "time": round(elapsed, 2)
        }

# this is the main function which will run all requests at once
async def main():
    # create one aiohttp session for all requests
    async with aiohttp.ClientSession() as session:
        # make a list of tasks (one for each url)
        tasks = [fetch_url(session, url) for url in urls]

        # run all tasks together (instead of one by one)
        results = await asyncio.gather(*tasks)

        # print the results in a nice table
        print(f"{'URL':<40} {'Status':<15} {'Time (s)':<8}")
        print("-" * 65)
        for r in results:
            print(f"{r['url']:<40} {r['status']:<15} {r['time']:<8}")

# this is the thing that actually starts the program
if __name__ == "__main__":
    asyncio.run(main())
