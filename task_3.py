from concurrent.futures import ThreadPoolExecutor
from typing import List

import requests
from tqdm import tqdm


def request(url):
    payload = '{\n\t"query": "West Shaorapara,around Mirpur 10,\\nShapla sharani.\\nHouse no:438/3"\n}'
    headers = {
        "x-api-key": "1234",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text.encode("utf8")


def request_pool(urls: str, workers: int = 10) -> List:
    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(
            tqdm(executor.map(request, urls, timeout=60), total=len(urls))
        )
        return results


if __name__ == "__main__":
    url = "http://helloworld.tech/"
    urls = [url] * 1000

    results = request_pool(urls, workers=10)
    for result in results:
        print(result)
