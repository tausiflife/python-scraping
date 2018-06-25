from splinter import Browser
import pandas as pd

url = "https://www.google.com"
search_keyword = "web scraping python"
browser = Browser('chrome')  # open a chrome browser
browser.visit(url)  # goes to the url
xpath = '//*[@id="lst-ib"]'

search_bar = browser.find_by_xpath(xpath)[0]

search_bar.fill(search_keyword)

search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
search_button = browser.find_by_xpath(search_button_xpath)[0]
search_button.click()

search_results_xpath = '//h3[@class="r"]/a'
search_results = browser.find_by_xpath(search_results_xpath)

scraped_data = []
for search_result in search_results:
    title = search_result.text.encode('utf8')  # trust me
    link = search_result["href"]
    scraped_data.append((title, link))

df = pd.DataFrame(data=scraped_data, columns=["Title", "Link"])
df.to_csv("links.csv")