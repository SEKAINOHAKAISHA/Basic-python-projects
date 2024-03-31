#uses sportsdb's free API calls to fetch player data

import requests
import json
import argparse
from urllib.parse import unquote

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('player',metavar='player',type=str,help='Specify player name')
    args = parser.parse_args()

    #use %20 to add spaces in player names or can also use underscore '_'
    player = args.player
    url = 'https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=' + player
    r = requests.get(url)
    data = json.loads(r.text)
    player = unquote(player)
    player = player.replace('_', ' ')
    try:
        if data['player'] == None:
            print(f'Player not found, try again')
            exit(0)
        print(f'{player} was born in ',end="")
        print(data['player'][0]['strBirthLocation'])
        print(f'{player} plays ',end="")
        print(data['player'][0]['strSport'],end=" ")
        print(f'and he plays for ',end="")
        print(data['player'][0]['strTeam'])
    except Exception as error:
        print(f'{type(error).__name__} error occurred!!')
        print(f'Try again!')