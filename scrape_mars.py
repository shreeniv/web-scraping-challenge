# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pymongo


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    mars = {}

    # Mars News URl of the page to be scrapped
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    news_soup = bs(html, "html.parser")

    # Retrieve the latest news title and paragraph
    news_title = news_soup.find_all('div', class_='content_title')[0].text
    news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text
    mars["news_title"] = news_title
    mars["news_p"] = news_p
    # Mars Image to be scraped
    jpl_nasa_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(jpl_nasa_url)
    time.sleep(5)
    browser.find_by_id("full_image").click()
    time.sleep(5)
    browser.find_link_by_partial_text("more info").click()
    html = browser.html

    images_soup = BeautifulSoup(html, 'html.parser')
    image_link = images_soup.find('figure',class_="lede")
    print(image_link)
    space_image=image_link.a.img["src"]
    space_image

    # fetch featured image link
    featured_image_url = "https://www.jpl.nasa.gov" + space_image
    print(featured_image_url)
    mars["featured_image_url"]=featured_image_url
    
    # mars facts table to be scraped
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    mars_facts_df = tables[0]
    mars_facts_df

    # scrapped data into pandas data frame

    mars_facts_df.columns = ["Description", "Value"]
    mars_facts_df
    mars_facts_df.set_index('Description', inplace=True)

    # converting pandas dataframe to a html page

    mars_html_table = mars_facts_df.to_html()
    mars_html_table

    # formatting html
    mars_html_table = mars_html_table.replace('\n', '')

    #print(mars_html_table)
    mars["facts"] = mars_html_table
    mars

     # Mars hemisphere name and image to be scraped
    # usgs_url = 'https://astrogeology.usgs.gov'
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hemispheres_url)
    hemispheres_html = browser.html
    hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    headers=[]
    titles = hemispheres_soup.find_all('h3')
    time.sleep(5)
    for title in titles:
        headers.append(title.text)
    images=[]
    count=0
    for thumb in headers:
        browser.find_by_css('img.thumb')[count].click()
        images.append(browser.find_by_text('Sample')['href'])
        browser.back()
        count=count+1
    hemisphere_image_urls = []
    counter = 0
    for item in images:
        hemisphere_image_urls.append({"title":headers[counter],"img_url":images[counter]})
        counter=counter+1
    browser.back()
    time.sleep(5)
    mars["hemispheres"] = hemisphere_image_urls
    # return mars dictionary
    return mars

    