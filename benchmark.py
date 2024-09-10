import requests
import time
from concurrent.futures import ThreadPoolExecutor

# 테스트할 API URL
ORM_API_URL = "http://localhost:8000/orm_api/"
RAW_SQL_API_URL = "http://localhost:8000/raw_api/"


def benchmark(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    if response.status_code == 200:
        return end_time - start_time
    else:
        return None


def load_test(url, num_requests=100):
    with ThreadPoolExecutor(max_workers=20) as executor:
        times = list(executor.map(lambda _: benchmark(url), range(num_requests)))
    return times


if __name__ == "__main__":
    print("ORM API 테스트 중...")
    orm_times = load_test(ORM_API_URL, num_requests=1000)

    print("Raw SQL API 테스트 중...")
    raw_sql_times = load_test(RAW_SQL_API_URL, num_requests=1000)

    orm_avg_time = sum([t for t in orm_times if t is not None]) / len(
        [t for t in orm_times if t is not None]
    )
    raw_sql_avg_time = sum([t for t in raw_sql_times if t is not None]) / len(
        [t for t in raw_sql_times if t is not None]
    )

    print(f"ORM API 평균 응답 시간: {orm_avg_time:.4f}초")
    print(f"Raw SQL API 평균 응답 시간: {raw_sql_avg_time:.4f}초")
