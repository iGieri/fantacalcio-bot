
"""

Fantacalcio Discord Bot

made by Federico PyGera Gerardi


"""


import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
import requests
import datetime

GIORNATA = 2
FOOTBALL_API_HEADERS = {"apikey": "471a2be0-1178-11ec-aa3b-6d04c0326cac"}


intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    print(f'Logged on as 🧙⚽🤖#2397')

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')  


@slash.slash(
    name="live",
    description="Cerca una squadra e ottieni tutti i suoi voti in diretta!", 
    options=[
        create_option(
            name='squadra', 
            description='nome della squadra',
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name='Atalanta',
                    value='1'
                ),
                create_choice(
                    name='Bologna',
                    value='2'
                ),
                create_choice(
                    name='Empoli',
                    value='5'
                ),
                create_choice(
                    name='Fiorentina',
                    value='6'
                ),
                create_choice(
                    name='Genoa',
                    value='7'
                ),
                create_choice(
                    name='Inter',
                    value='9'
                ),
                create_choice(
                    name='Juventus',
                    value='10'
                ),
                create_choice(
                    name='Lazio',
                    value='11'
                ),
                create_choice(
                    name='Milan',
                    value='12'
                ),
                create_choice(
                    name='Napoli',
                    value='13'
                ),
                create_choice(
                    name='Roma',
                    value='15'
                ),
                create_choice(
                    name='Sampdoria',
                    value='16'
                ),
                create_choice(
                    name='Sassuolo',
                    value='17'
                ),
                create_choice(
                    name='Torino',
                    value='18'
                ),
                create_choice(
                    name='Udinese',
                    value='19'
                ),
                create_choice(
                    name='Verona',
                    value='20'
                ),
                create_choice(
                    name='Cagliari',
                    value='21'
                )
            ]
        )
    ]
)
async def _live(ctx, squadra):
    
    actual = 0

    condition = True

    my_round = {}

    params = (
        ("season_id","2100"),
    )
    
    rounds_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/rounds', headers=FOOTBALL_API_HEADERS, params=params).json()

    for rund in rounds_req['data']:
        if rund['is_current']:
            my_round = rund
    
    req = requests.get(f'https://www.fantacalcio.it/api/live/{squadra}?g={rund["name"]}&i=16')

    title = ''
    logo = ''

    if squadra == '1':
        title = 'Atalanta :black_circle::blue_circle:'
        color = 0x0034ad
        logo = 'https://cdn.sportdataapi.com/images/soccer/teams/100/109.png'
    elif squadra == '2':
        title = 'Bologna :red_circle::blue_circle:'
        color = 0xad0031
        logo = 'https://cdn.sportdataapi.com/images/soccer/teams/100/400.png'
    elif squadra == '5':
        title = 'Empoli :blue_circle:'
        color = 0x0045ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/2345.png"
    elif squadra == '6':
        title = 'Fiorentina :purple_circle:'
        color = 0x5c00ad
        logo = 'https://cdn.sportdataapi.com/images/soccer/teams/100/389.png'
    elif squadra == '7':
        title = 'Genoa :red_circle::blue_circle:'
        color = 0xad0031
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/402.png"
    elif squadra == '9':
        title = 'Inter :black_circle::blue_circle:'
        color = 0x0034ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/94.png"
    elif squadra == '10':
        title = 'Juventus :white_circle::black_circle:'
        color = 0xbfbfbf
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/108.png"
    elif squadra == '11':
        title = 'Lazio :blue_circle::white_circle:'
        color = 0x0088c2
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/398.png"
    elif squadra == '12':
        title = 'Milan :red_circle::black_circle:'
        color = 0xad0031
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/391.png"
    elif squadra == '13':
        title = 'Napoli :blue_circle:'
        color = 0x0034ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/102.png"
    elif squadra == '15':
        title = 'Roma :orange_circle::red_circle:'
        color = 0xd46a00
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/401.png"
    elif squadra == '16':
        title = 'Sampdoria :blue_circle::white_circle::red_circle:'
        color = 0x0034ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/397.png"
    elif squadra == '17':
        title = 'Sassuolo :green_circle::black_circle:'
        color = 0x00a838
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/394.png"
    elif squadra == '18':
        title = 'Torino :brown_circle:'
        color = 0x913000
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/393.png"
    elif squadra == '19':
        title = 'Udinese :black_circle::white_circle:'
        color = 0xbfbfbf
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/390.png"
    elif squadra == '20':
        title = 'Verona :yellow_circle::blue_circle:'
        color = 0xd4e300
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/399.png"
    elif squadra == '21':
        title = 'Cagliari :red_circle::blue_circle:'
        color = 0xad0031
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/395.png"
    
    description = ''

    if req.json() == []:
        description += 'Non sono ancora disponibili i dati della '

    description += f'*{my_round["name"]}a giornata Serie A TIM*'

    embedVar = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    
    embedVar.set_thumbnail(url=logo)

    if req.json() == []:

        for player in req.json():
            
            if player['ruolo'] == 'P':
                ruolo = ':regional_indicator_p:'
            elif player['ruolo'] == 'D':
                ruolo = ':regional_indicator_d:'
            elif player['ruolo'] == 'C':
                ruolo = ':regional_indicator_c:'
            elif player['ruolo'] == 'A':
                ruolo = ':regional_indicator_a:'
            elif player['ruolo'] == 'ALL':
                ruolo = ':person_lifting_weights:'

            '''
            Eventi:

            1: Cartellino Giallo
            2: Cartellino Rosso
            3: Gol Fatto
            4: Gol Subito
            14: Esce Giocatore
            15: Entra Giocatore
            22: Assist Normale

            '''

            eventi = ''
            bonus = 0

            for evento in player['evento'].split(','):
                if evento == '1':
                    eventi += ':yellow_square: '
                    bonus -= 0.5
                elif evento == '2':
                    eventi += ':red_square: '
                    bonus -= 1
                elif evento == '3':
                    eventi += ':soccer: '
                    bonus += 3
                elif evento == '4':
                    eventi += ':x: '
                    bonus -= 1
                elif evento == '14':
                    eventi += ':arrow_down: '
                elif evento == '15':
                    eventi += ':arrow_up:'
                elif evento == '22':
                    eventi += ':athletic_shoe: '
            
            if not ':x: ' in eventi and player['ruolo'] == 'P':
                eventi += ':gloves: '
                bonus += 1

            embedVar.add_field(name="\u200b", value=f'{ruolo} {player["nome"][0]}{player["nome"][1:].lower()} - {"SV" if player["voto"] == 55.0 else player["voto"]} **{"SV" if player["voto"] == 55.0 else player["voto"]+bonus}** {eventi}', inline=False)

    await ctx.send(embed=embedVar)

@slash.slash(
    name="matches",
    description="Guarda i risultati delle partite in diretta!"
)
async def _matches(ctx):

    my_round = {}

    params = (
        ("season_id","2100"),
    )
    
    matches_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=FOOTBALL_API_HEADERS, params=params).json()

    matches = []

    for match in matches_req['data']:
        if match['round']['is_current']:
            my_round = { 'name': match['round']['name'], 'id': match['round']['round_id'] }
            matches.append(match)
    
    matches.sort(key=lambda match: datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S'))

    embedVar = discord.Embed(
        title=f'{my_round["name"]}a Giornata di Serie A TIM',
        color=0x00197d
    )

    embedVar.set_thumbnail(url="https://www.legaseriea.it/assets/legaseriea/images/logo_main_seriea.png?v=34")

    for match in matches:
        embedVar.add_field(name=f"{(datetime.datetime.strptime(match['match_start'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=2)).strftime('%H:%M %d/%m/%Y') if match['status_code'] == 0 else f''':red_circle: LIVE {match['minute']}''' if match['status_code'] == 1 else ':clock10: Primo Tempo' if match['status_code'] == 11 else 'Partita Terminata'}", value=f"{str(discord.utils.get(client.emojis, name=match['home_team']['short_code']))} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['home_team']['name']} {f'''{match['stats']['home_score']} {'**'if match['stats']['home_score'] > match['stats']['away_score'] and match['status_code'] == 3 else ' '} - {'**'if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '}{match['stats']['away_score']}''' if match['status_code'] != 0 else ' - '} {match['away_team']['name']}{'**' if match['stats']['home_score'] < match['stats']['away_score'] and match['status_code'] == 3 else ' '} {str(discord.utils.get(client.emojis, name=match['away_team']['short_code']))}", inline=False)

    await ctx.send(embed=embedVar)

client.run('ODgzNTAxMTE4ODYzMzIzMjE2.YTK2iQ.vHPwBOi-HGu0cLDfpAN9m_NBNQs')