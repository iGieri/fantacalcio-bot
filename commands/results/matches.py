import discord
import datetime
import requests

async def matches(ctx, client, FOOTBALL_API_HEADERS):

    '''
    Matches command:
    
    Getting live data about the current Serie A TIM matchday

    '''

    my_round = {}

    params = (
        ("season_id","2100"),
    )
    
    # Requesting to the API all the data about the matches
    matches_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=FOOTBALL_API_HEADERS, params=params).json()

    matches = []

    # Getting the current matchday
    for match in matches_req['data']:
        if match['round']['is_current']:
            my_round = { 'name': match['round']['name'], 'id': match['round']['round_id'] }
            matches.append(match)
    
    # Sorting the matches by time
    matches.sort(key=lambda match: datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S'))


    # Message formatting
    embedVar = discord.Embed(
        title=f'{my_round["name"]}a Giornata di Serie A TIM',
        color=0x00197d
    )

    embedVar.set_thumbnail(url="https://www.legaseriea.it/assets/legaseriea/images/logo_main_seriea.png?v=34")

    for match in matches:
        embedVar.add_field(name=f"{(datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=2)).strftime('%H:%M %d/%m/%Y') if match['status_code'] == 0 else f''':red_circle: LIVE {match['minute']}' ''' if match['status_code'] == 1 else ':clock10: Primo Tempo' if match['status_code'] == 11 else 'Partita Terminata'}", value=f"{str(discord.utils.get(client.emojis, name=match['home_team']['short_code']))} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['home_team']['name']} {f'''{match['stats']['home_score']} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '} - {'**'if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['stats']['away_score']}''' if match['status_code'] != 0 else ' - '} {match['away_team']['name']}{'**' if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '} {str(discord.utils.get(client.emojis, name=match['away_team']['short_code']))}", inline=False)

    # Send everything
    message = await ctx.reply(embed=embedVar, mention_author=False)

    emojis = ["⬅️", "➡️","🔄"]

    # React to create the matches menu
    for emoji in emojis:
        await message.add_reaction(emoji)

async def match_back(message, client, FOOTBALL_API_HEADERS):
    my_round = {}

    params = (
        ("season_id","2100"),
    )
    
    matches_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=FOOTBALL_API_HEADERS, params=params).json()

    matches = []

    for match in matches_req['data']:
        if match['round']['is_current']:
            my_round = { 'name': str(int(match['round']['name'])-1), 'id': match['round']['round_id'] }
            
    for match in matches_req['data']:        
        if match['round']['name'] == my_round['name']:
            matches.append(match)
    
    matches.sort(key=lambda match: datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S'))

    embedVar = discord.Embed(
        title=f'{my_round["name"]}a Giornata di Serie A TIM',
        color=0x00197d
    )

    embedVar.set_thumbnail(url="https://www.legaseriea.it/assets/legaseriea/images/logo_main_seriea.png?v=34")

    for match in matches:
        embedVar.add_field(name=f"{(datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=2)).strftime('%H:%M %d/%m/%Y') if match['status_code'] == 0 else f''':red_circle: LIVE {match['minute']}' ''' if match['status_code'] == 1 else ':clock10: Primo Tempo' if match['status_code'] == 11 else 'Partita Terminata'}", value=f"{str(discord.utils.get(client.emojis, name=match['home_team']['short_code']))} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['home_team']['name']} {f'''{match['stats']['home_score']} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '} - {'**'if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['stats']['away_score']}''' if match['status_code'] != 0 else ' - '} {match['away_team']['name']}{'**' if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '} {str(discord.utils.get(client.emojis, name=match['away_team']['short_code']))}", inline=False)

    edit = await message.edit(embed=embedVar, mention_author=False)

    emojis = ["🕙"]

    for emoji in emojis:
        await message.add_reaction(emoji)

async def match_forward(message, client, FOOTBALL_API_HEADERS):
    my_round = {}

    params = (
        ("season_id","2100"),
    )
    
    matches_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=FOOTBALL_API_HEADERS, params=params).json()

    matches = []

    for match in matches_req['data']:
        if match['round']['is_current']:
            my_round = { 'name': str(int(match['round']['name'])+1), 'id': match['round']['round_id'] }
            
    for match in matches_req['data']:        
        if match['round']['name'] == my_round['name']:
            matches.append(match)
    
    matches.sort(key=lambda match: datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S'))

    embedVar = discord.Embed(
        title=f'{my_round["name"]}a Giornata di Serie A TIM',
        color=0x00197d
    )

    embedVar.set_thumbnail(url="https://www.legaseriea.it/assets/legaseriea/images/logo_main_seriea.png?v=34")

    for match in matches:
        embedVar.add_field(name=f"{(datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=2)).strftime('%H:%M %d/%m/%Y') if match['status_code'] == 0 else f''':red_circle: LIVE {match['minute']}' ''' if match['status_code'] == 1 else ':clock10: Primo Tempo' if match['status_code'] == 11 else 'Partita Terminata'}", value=f"{str(discord.utils.get(client.emojis, name=match['home_team']['short_code']))} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['home_team']['name']} {f'''{match['stats']['home_score']} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '} - {'**'if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['stats']['away_score']}''' if match['status_code'] != 0 else ' - '} {match['away_team']['name']}{'**' if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '} {str(discord.utils.get(client.emojis, name=match['away_team']['short_code']))}", inline=False)

    edit = await message.edit(embed=embedVar, mention_author=False)

    emojis = ["🕙"]

    for emoji in emojis:
        await message.add_reaction(emoji)

async def match_now(message, client, FOOTBALL_API_HEADERS):
    my_round = {}

    params = (
        ("season_id","2100"),
    )
    
    matches_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=FOOTBALL_API_HEADERS, params=params).json()

    matches = []

    for match in matches_req['data']:
        if match['round']['is_current']:
            my_round = { 'name': str(match['round']['name']), 'id': match['round']['round_id'] }
            matches.append(match)
            
    matches.sort(key=lambda match: datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S'))

    embedVar = discord.Embed(
        title=f'{my_round["name"]}a Giornata di Serie A TIM',
        color=0x00197d
    )

    embedVar.set_thumbnail(url="https://www.legaseriea.it/assets/legaseriea/images/logo_main_seriea.png?v=34")

    for match in matches:
        embedVar.add_field(name=f"{(datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=2)).strftime('%H:%M %d/%m/%Y') if match['status_code'] == 0 else f''':red_circle: LIVE {match['minute']}' ''' if match['status_code'] == 1 else ':clock10: Primo Tempo' if match['status_code'] == 11 else 'Partita Terminata'}", value=f"{str(discord.utils.get(client.emojis, name=match['home_team']['short_code']))} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['home_team']['name']} {f'''{match['stats']['home_score']} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '} - {'**'if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['stats']['away_score']}''' if match['status_code'] != 0 else ' - '} {match['away_team']['name']}{'**' if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '} {str(discord.utils.get(client.emojis, name=match['away_team']['short_code']))}", inline=False)

    edit = await message.edit(embed=embedVar, mention_author=False)

    emojis = ["⬅️", "➡️","🔄"]

    for emoji in emojis:
        await message.add_reaction(emoji)
