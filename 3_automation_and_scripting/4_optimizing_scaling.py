"""
Profiling tools -> cProfile and line_profiler

cProfile gives you a broad overview of your program's performance,
line_profiler -> see exactly how much time is spent on each individual line of code within a specific function.

Concurrency, often implemented using multiple threads (multithreading) in Python, manages multiple tasks within a single process. These threads share the same memory space but are typically limited in their ability to run truly simultaneously on multi-core processors due to Python's Global Interpreter Lock (GIL). Concurrency excels in scenarios where tasks involve waiting, such as network requests or user input, as the program can switch between tasks during these idle periods.
Multiprocessing, on the other hand, involves running multiple independent processes, each with its own Python interpreter and dedicated memory space. This allows for true parallel execution across multiple CPU cores,
"""

# Scaling automation with concurrency
# concurrency using threads
import concurrent.futures
import requests


def fetch_data(api_url):
    """Fetches data from a given API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None


if __name__ == "__main__":
    api_urls = [
        "https://api.example.com/data1",
        "https://api.another-example.com/data2",
        "https://api.yet-another-example.com/data3",
        # Add more API URLs as needed
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit API requests concurrently
        future_to_url = {executor.submit(fetch_data, url): url for url in api_urls}

        # Process results as they become available
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                if data:
                    print(f"Data from {url}: {data}")
            except Exception as exc:
                print(f"Exception while fetching data from {url}: {exc}")


# Scaling automation with multiprocessing
import multiprocessing
from PIL import Image  # Example of an image processing library


def process_image(image_path):
    """Performs CPU-intensive image processing on a single image."""
    # Load the image
    image = Image.open(image_path)
    # Apply filters, transformations, or any desired processing
    image = image.convert("L")  # Example: convert to grayscale
    # Save the processed image
    image.save(f"processed_{image_path}")


if _name_ == "__main__":
    image_paths = ["image1.jpg", "image2.jpg", ...]  # List of image paths
    # Create a pool of processes (adjust the number based on your CPU cores)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the 'process_image' function to each image path in parallel
        pool.map(process_image, image_paths)


"""
Scaling web scraping with Scrapy clusters

# scrapy.cfg file, which resides in the root directory of your Scrapy project on each node in your cluster.

[settings]
default = myproject.settings

[deploy]
url = http://your_scrapyd_server_address:6800/ 
project = my_scraping_project 

# (Optional) If Scrapyd has authentication enabled
# username = your_scrapyd_username
# password = your_scrapyd_password

"""
