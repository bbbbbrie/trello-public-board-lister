# Trello Public Board Lister

![GitHub last commit](https://img.shields.io/github/last-commit/bbbbbrie/trello-public-board-lister?style=for-the-badge) | ![GitHub Repo stars](https://img.shields.io/github/stars/bbbbbrie/trello-public-board-lister?style=for-the-badge)

A quick Python program that I wrote to list all public Trello boards given a file containing Trello usernames one-per-line. You should get a Trello API key and token and `pip install -r requirements.txt` in order to follow along. You can pass your API key and token at the command line or set them in your environment variables:

  * `export TRELLO_API_KEY=yourtrelloapikey`
  * `export TRELLO_API_TOKEN=yourtrelloapitoken`


This has been tested with Python 3.7. 

## Get a Trello API key and token
You will need a Trello API key and token. 

  1. Log in to [Trello](https://trello.com)
  1. Go to [https://trello.com/app-key](https://trello.com/app-key)
  1. Follow the prompts
  1. Record the key and token 

## Usage
Put the usernames that you care about in a file in this directory called `trello-usernames.txt`. 

Run `python3 main.py --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN`

Run `python3 main.py --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN --usernames /path/to/usernames` if you have the usernames elsewhere.

Run `python3 main.py --help` to see the help information.
