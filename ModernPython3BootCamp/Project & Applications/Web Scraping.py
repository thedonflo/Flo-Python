# Web Scraping Project
# Introduction
# In this project you'll be building a quotes guessing game.
# When run, your program will scrape a website for a collection of quotes.
# Pick one at random and display it. The player will have four chances to guess who said the quote.
# After every wrong guess they'll get a hint about the author's identity.

from bs4 import BeautifulSoup  #Import BeautifulSoup for scraping
import requests #Import requests to read website
from time import sleep      #used for setting delay so website does not flag us
from random import choice   #This will be used to select random choice

base_url = "http://quotes.toscrape.com" #desired website

url = "/page/1"      #Look at notes below on how we pulled this information
#****** Part 1 Build the scraper

all_quotes = [] #create a list to store the quotes
while url:                  #Start loop to go through every page. You can look at logic below to identify page
    response = requests.get(f"{base_url}{url}")  #set website to variable
    print(f"Now Scraping {base_url}{url}....")
    soup = BeautifulSoup(response.text, "html.parser")#Send url contents to BeautifulSoup for parsing
    # print(soup)
    quotes = soup.find_all(class_="quote")#Inspector page identifies quote as class quote. Remember to use "class_"
    # print(quotes)
    for quote in quotes:    #search for class = text within class="quote" to find the actual quote. Then loop
        all_quotes.append({                             #store the quotes as dictionaries in list
            "text": quote.find(class_="text").get_text(),      #pull the quote using class="text"
            "author": quote.find(class_="author").get_text(),  #pull the quote using class="author"
            "bio-link": quote.find("a")["href"]                #pull the author's biolink by looking for the first anchor tag
        })
        # print(all_quotes)
        # print(quote.find(class_="text").get_text())
        # print(quote.find(class_="author").get_text())
        # print(quote.find("a")["href"])

        #We need to reiterate for every page on website. Best way to do this is for looking for every page with "Next" at bottom
        #If there isn't one, we stop
    next_btn = soup.find(class_="next")  #class="net" identifies the Next button
    # print(next_btn.find("a")["href"]) #This provides the next url to scrape. However, we start with "/page/1"
    url = next_btn.find("a")["href"] if next_btn else None #reset variable if there is a next button, else nothing
    # sleep(2)                 #Delay time. For this example, this waits for two seconds.  This is normal protocol
# print(all_quotes)           #Read the data scraped


#****** Part 2 Build the Game logic
#  It is best to store the scraped data into a file so we can pull from persistent storage instead of re-scraping

quote = choice(all_quotes)      #Select a random quote. This is a dictionary as defined above
remaining_guesses = 4           #Guess counter
print("Here's a quote: ")
print(quote["text"])            #Pull text quote
# print(quote["author"])
guess = ''
while guess.lower() != quote["author"].lower() and remaining_guesses > 0: #loop to repeat if guesses are incorrect
    guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
    if guess.lower() == quote['author'].lower():                          #Check if first guess is correct
        print("YOU GOT IT RIGHT!")
        break
    remaining_guesses -= 1                      #Decrement amount of guesses
    if remaining_guesses == 3:                  #This message is initially displayed during first wrong guess
        res = requests.get(f"{base_url}{quote['bio-link']}")   #We will provide guess for wrong guess by adding link to author's bio
        soup = BeautifulSoup(res.text, "html.parser")
        # print(soup.body)
        birth_date = soup.find(class_="author-born-date").get_text()   #Pull the birth date from page
        birth_place = soup.find(class_="author-born-location").get_text()   #Pull the birth location from page
        print(f"Here's a hint: The author was born on {birth_date} in {birth_place}")
    elif remaining_guesses == 2:
        print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")      #Using index to pull first character
    elif remaining_guesses == 1:
        last_initial = quote['author'].split(" ")[1][0]                                     #Using split and then get corresponding index
        print(f"Here's a hint: The author's last name starts with: {quote['author'][0]}")      #Build string for last name character
    else:
        print(f"Sorry you ran out of guesses. The answer was {quote['author']}")            #Final failure message that gives solutions


# print("AFTER WHILE LOOP")

