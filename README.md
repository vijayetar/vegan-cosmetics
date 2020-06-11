# Vegan Cosmetics
* Jesse Pena, Corey Marchand, Vij Rangarajan
* Check cosmetics for vegan ingredients

### Dependencies
* gitignore
* requests
* bs4
* black 
* pytest
* regex
* json
* sys

### How to run program
* Open repo
* Do a `poetry install` in terminal to add dependencies to your local machine
* In terminal type: `python main.py`
* Follow instructions in terminal to progress through application
* Type and enter `q` at any time to quit


## Title
* Looking for vegan cosmetics
### User Story sentence
* I want to be able to find all vegan cosmetics from WalMart. I want to be able to arrange the results in a specific order and save it in a file.
### Feature Tasks
* Find a working API for WalMart to get cosmetics with ingredients
### Acceptance Tests
* Successfully retrieve cosmetics
* Successfully review ingredients and sieve the data
* Successfully find vegan ingredients 

## Title
* Data storage
### User Story sentence
* As a user I want to have the data retrieved saved to a file(.txt)
### Feature Tasks
* Traverse the api and save unique vegan cosmetic data 
### Acceptance Tests
* Successfully find unique vegan cosmetic data
* Save vegan cosmetic data

## Title
* User Input
### User Story sentence
* As a user I want to be able to input a cosmetic and get search results (eyeliner, lipstick, foundation, etc.)
### Feature Tasks
* Create an input interface for the user to type in their search query
### Acceptance Tests
* Have an interface for the user to select products

## Title
* Data retrieval
### User Story sentence
* As a user I want to retrieve vegan cosmetic data from the storage (.txt file)
### Feature Tasks
* Traverse the text file and extract saved vegan cosmetic data and return it
### Acceptance Tests
* Successfully traverse the file 
* Search for a particular cosmetic
* Pull out the particular cosmetic's information

## Title
* Looking for vegan cosmetics in a web page without an API
### User Story sentence
* As a user I want to scrape provided urls for vegan cosmetics
### Feature Tasks
* Scrape the provided the web page for vegan cosmetics
### Acceptance Tests
* Successfully retrieve cosmetics
* Successfully review ingredients and sieve the data
* Successfully find vegan ingredients 


## Title
* Save personalized search results to .txt file
### User Story sentence
* As a user I want to save the results of my searches to a separate a .txt file
### Feature Tasks
* Save results of personalized searches to a separate .txt file
### Acceptance Tests
* Successfully create new .txt file with personalized search results

## Domain Model
* https://ibb.co/SsFPVPW

## References  
* [Regex references](https://www.regexpal.com/95367)  
* [Regex development tool](https://regex101.com/)
* [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Testing
* The tests determine if user input on main.py works as expected