import argparse
import loguru
import os
import requests


def get_public_trello_boards(user_name, api_key, api_token):
    loguru.logger.add('public-trello-boards.log', rotation="500 MB")
    my_parameters = (
        ('filter', 'public'),
        ('fields', 'url'),
        ('key', api_key),
        ('token', api_token),
    )
    url = "https://api.trello.com/1/members/" + user_name + "/boards"
    response = requests.get(url=url, params=my_parameters)
    trello_boards = response.text
    number_of_boards = str(len(trello_boards))
    json_body = response.json() 
    if len(trello_boards) > 2:
        filename = user_name + ".boards"
        with open(filename, mode="w") as trello_boards_file:
            full_path = os.path.abspath(filename)
            trello_boards_file.write(trello_boards)
    else:
        loguru.logger.debug("{}: No public Trello boards for {}", user_name.upper(), user_name, level="DEBUG")
    return json_body


def get_api_keys_from_environment():
    api_key = os.getenv('TRELLO_API_KEY')
    api_token = os.environ.get('TRELLO_API_TOKEN')
    return(api_key, api_token)


def count_the_boards(json_body):
    number_of_boards = int()
    for i in json_body:
        number_of_boards = number_of_boards + 1
    return number_of_boards


def main(user_name_list, api_key, api_token):
    if not (api_key and api_token):
        loguru.logger.error("No API key and token at the CLI; checking environment variables")
        api_key, api_token = get_api_keys_from_environment()
    for trello_user in set(user_name_list):
        json_body = get_public_trello_boards(trello_user, api_key, api_token)
        my_lists = count_the_boards(json_body)
        loguru.logger.info("{}: I found {} public Trello boards while looking around https://trello.com/{}.", trello_user.upper(), my_lists, trello_user)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Trello Public Board Lister // This is a Python program that will list all public boards for the Trello usernames that you specify.""")
    parser.add_argument('--api_key',  type=str, help="Your Trello API key")
    parser.add_argument('--api_token', type=str, help="Your Trello API token")
    parser.add_argument('--usernames', type=str, default="trello-usernames.txt", help="Path to file containing usernames")
    args = parser.parse_args()
    api_key = args.api_key
    api_token = args.api_token
    user_name_file = args.usernames
    user_name_file = open(user_name_file)
    user_name_list = [line.rstrip('\n') for line in user_name_file.readlines()]
    main(user_name_list, api_key, api_token)
