# importing libraries
from googlesearch import search
from bs4 import BeautifulSoup
import csv
import regex as re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# initializing a list for storing data
data = []

# queries
queries = [
    "Identify the industry in which Canoo operates, along with its size, growth rate, trends, and key players",
    "Canoo's main competitors, including their market share, products or services offered, pricing strategies, and marketing efforts",
    "Identify key trends in the market, including changes in consumer behavior, technological advancements, and shifts in the competitive landscape",
    "Canoo's financial performance, including its revenue, profit margins, return on investment, and expense structure",
]

try:
    # Set up Selenium with a headless Chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # looping through every query
    for query in queries:
        urls = search(query, num_results=3)

        # looping through every url of each query
        for url in urls:

            # Check if the URL not ends with a common PDF extension
            if not url.lower().endswith((".pdf", ".pdf/")):
                # Open the URL in a headless browser
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)

                # Wait for the page to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )

                # Get the page source
                page_content = driver.page_source
                driver.quit()  # Close the browser after getting the page source

                # Parse using BeautifulSoup
                soup = BeautifulSoup(page_content, "html.parser")

                # Extract the text alone
                text = soup.get_text()

                # Remove unnecessary spaces
                cleaned_text = " ".join(
                    re.sub(r"\s+", " ", string.strip())
                    for string in soup.stripped_strings
                )

                # Check the length of the cleaned text
                if len(cleaned_text.split()) >= 100:
                    # Append the data
                    data.append({"query": query, "url": url, "data": str(cleaned_text)})
                else:
                    print(f"Skipping short content for URL: {url}")

                
except Exception as e:
    print(f"Error while processing: {e}")

# Save data to CSV
csv_filename = "output_data.csv"
fields = ["query", "url", "data"]

with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(data)
