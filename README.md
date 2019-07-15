# Trello Public Board Lister

A quick Python program that I wrote to list all public Trello boards given a file containing Trello usernames one-per-line. You will need to `pip install loguru`. This has been tested with Python 3. 

## Usage
Put the usernames that you care about in a file in this directory called `trello-usernames.txt`. 

Run `python3 main.py --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN`

Run `python3 main.py --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN --usernames /path/to/usernames` if you have the usernames elsewhere.

Run `python3 main.py --help` to see the help information.
