
"""

Fantacalcio Discord Bot

made by Federico PyGera Gerardi


TODO:

- Aggiornamento giornata automatico.
- Campo Avversario in live
- Comando /partite
- Comando per i singoli giocatori
- Comando statistiche squadra
- Trovare Salernitana, Spezia e Venezia


"""


import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
import requests



intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
slash = SlashCommand(client, sync_commands=True)

guild_ids = []

GIORNATA = 2

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

    req = requests.get(f'https://www.fantacalcio.it/api/live/{squadra}?g=2&i=16')

    title = ''

    if squadra == '1':
        title = 'Atalanta :black_circle::blue_circle:'
        color = 0x0034ad
    elif squadra == '2':
        title = 'Bologna :red_circle::blue_circle:'
        color = 0xad0031
    elif squadra == '5':
        title = 'Empoli :blue_circle:'
        color = 0x0045ad
    elif squadra == '6':
        title = 'Fiorentina :purple_circle:'
        color = 0x5c00ad
    elif squadra == '7':
        title = 'Genoa :red_circle::blue_circle:'
        color = 0xad0031
    elif squadra == '9':
        title = 'Inter :black_circle::blue_circle:'
        color = 0x0034ad
    elif squadra == '10':
        title = 'Juventus :white_circle::black_circle:'
        color = 0xbfbfbf
    elif squadra == '11':
        title = 'Lazio :blue_circle::white_circle:'
        color = 0x0088c2
    elif squadra == '12':
        title = 'Milan :red_circle::black_circle:'
        color = 0xad0031
    elif squadra == '13':
        title = 'Napoli :blue_circle:'
        color = 0x0034ad
    elif squadra == '15':
        title = 'Roma :orange_circle::red_circle:'
        color = 0xd46a00
    elif squadra == '16':
        title = 'Sampdoria :blue_circle::white_circle::red_circle:'
        color = 0x0034ad
    elif squadra == '17':
        title = 'Sassuolo :green_circle::black_circle:'
        color = 0x00a838
    elif squadra == '18':
        title = 'Torino :brown_circle:'
        color = 0x913000
    elif squadra == '19':
        title = 'Udinese :black_circle::white_circle:'
        color = 0xbfbfbf
    elif squadra == '20':
        title = 'Verona :yellow_circle::blue_circle:'
        color = 0xd4e300
    elif squadra == '21':
        title = 'Cagliari :red_circle::blue_circle:'
        color = 0xad0031

    description = '*2a giornata Serie A TIM*'

    embedVar = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    
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

        # string += f' {ruolo} {player["nome"][0]}{player["nome"][1:].lower()} - {"SV" if player["voto"] == 55.0 else player["voto"]} **{"SV" if player["voto"] == 55.0 else player["voto"]+bonus}** {eventi} \n'
        embedVar.add_field(name="\u200b", value=f'{ruolo} {player["nome"][0]}{player["nome"][1:].lower()} - {"SV" if player["voto"] == 55.0 else player["voto"]} **{"SV" if player["voto"] == 55.0 else player["voto"]+bonus}** {eventi}', inline=False)

    await ctx.send(embed=embedVar)


client.run('ODgzNTAxMTE4ODYzMzIzMjE2.YTK2iQ.vHPwBOi-HGu0cLDfpAN9m_NBNQs')