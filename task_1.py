""" Homework """

import os
import json
import requests
import aiohttp
import asyncio


if not os.path.exists('json_files_combined'):
    os.makedirs('json_files_combined')


def save_json_to_file(data, index):
    with open(f"json_files_combined/file_{index}.json", 'w') as f:
        json.dump(data, f, indent=4)


def requestsing(url, index):
    response = requests.get(url)
    data = response.json()
    save_json_to_file(data, index)


async def aiohttping(url, index):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            save_json_to_file(data, index)


async def main():
    urls = ["https://jsonplaceholder.typicode.com/posts"] * 10

    for index, url in enumerate(urls):
        requestsing(url, index)

    await asyncio.gather(*[aiohttping(url, index) for index, url in enumerate(urls)])


asyncio.run(main())
