# web-scraping-challenge

Once we execute app.py, click on 'scrape new data' button to display scrapped data contents on the 'Mission to Mars' html page created. 

Step 1 - Scraping
Created the code on jupyter notebook 'mission_to_mars.ipynb' to connect to mars news website and gather the following images and information related to scrapping:

NASA Mars News
Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
news_title 
news_p 
JPL Mars Space Images - Featured Image

Used splinter to navigate the site and found the image urls for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.
######featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

Mars Facts
Next launched Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

The above information is converted to a HTML table string in the resultant page

Mars Hemispheres
fetched high resolution images for each of Mar's hemispheres.
Python dictionary mars[] was used to store the data using the keys img_url and title.

Later, the dictionary was appended with the image url string and the hemisphere title to a list. 

Step 2 - Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
A flask route was created to import scrape_mars.py script and call scrape function.

Created a template HTML file 'index.html' with mars data dictionary to display all of the data along with the appropriate HTML elements

