## Bonus Task: Async URL Fetcher (Extra Credit)

This script uses Python’s `aiohttp` and `asyncio` libraries to fetch multiple URLs concurrently.  
It measures and prints the response status and time taken for each URL.

**How it works:**  
- Sends all URL requests asynchronously, so they run at the same time.  
- Collects status codes and response times for each URL.  
- Prints results to the terminal.

**How to run:**  
1. Install dependencies with `pip install aiohttp`  
2. Run the script with `python async_fetcher.py`

This approach is useful to speed up network-bound tasks like web scraping or API calls.
