
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import threading
import time


# Function to view the webcam URL
def view_webcam(url, session_duration):
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable- automation"])

   

    # Start the WebDriver
    driver = webdriver.Chrome(options=options)


    try:
        driver.get(url)
        # Keep the session alive for the specified duration
        time.sleep(session_duration)
    except Exception as e:
        print(f"Error viewing {url}: {e}")
    finally:
        driver.quit()


# Main function to create multiple threads for viewing webcam URLs
def main():
    # List of webcam URLs to view
    urls = [
        "https://www.webcamtaxi.com/en/poland/greater-poland/pogrzybowo-reservoir-cam.html"  
    ]

    session_duration = 60  # Duration to keep each session active (in seconds)
    total_views_per_url = 5  # Number of views per URL

    threads = []

    for url in urls:
        for _ in range(total_views_per_url):
            thread = threading.Thread(target=view_webcam, args=(url, session_duration))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
