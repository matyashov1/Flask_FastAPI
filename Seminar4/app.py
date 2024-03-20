python

Копировать код
import os
import sys
import threading
import multiprocessing
import asyncio
import aiohttp
from flask import Flask, request

app = Flask(__name__)

async def download_image(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            filename = url.split('/')[-1]
            with open(filename, 'wb') as f:
                f.write(await response.read())
            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {url}")

async def async_download(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url) for url in urls]
        await asyncio.gather(*tasks)

def download_with_threads(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image_sync, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def download_with_processes(urls):
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image_sync, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

def download_image_sync(url):
    with aiohttp.ClientSession() as session:
        asyncio.run(download_image(session, url))

@app.route('/download', methods=['POST'])
def download_images():
    urls = request.json.get('urls', [])
    if not urls:
        return "No URLs provided", 400

    start_time = time.time()

    # Using async approach
    asyncio.run(async_download(urls))

    # Using threads
    download_with_threads(urls)

    # Using processes
    download_with_processes(urls)

    total_time = time.time() - start_time
    print(f"Total execution time: {total_time} seconds")

    return "Images downloaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
