import requests
import discord

async def live(ctx, squadra, FOOTBALL_API_HEADERS):
    '''
    Live command:

    Get live points scored by all players from a specific team in the current matchday

    '''
    
    my_round = {}

    params = (
        ("season_id","2100"),
    )
    
    # Getting the current matchday
    rounds_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/rounds', headers=FOOTBALL_API_HEADERS, params=params).json()

    for rund in rounds_req['data']:
        if rund['is_current']:
            my_round = rund
    
    

    n_team = 0

    title = ''
    logo = ''

    # Getting all the information about the requested team

    if squadra == 'Atalanta':
        title = 'Atalanta :black_circle::blue_circle:'
        color = 0x0034ad
        logo = 'https://cdn.sportdataapi.com/images/soccer/teams/100/109.png'
        n_team = 1
    elif squadra == 'Bologna':
        title = 'Bologna :red_circle::blue_circle:'
        color = 0xad0031
        logo = 'https://cdn.sportdataapi.com/images/soccer/teams/100/400.png'
        n_team = 2
    elif squadra == 'Empoli':
        title = 'Empoli :blue_circle:'
        color = 0x0045ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/2345.png"
        n_team = 5
    elif squadra == 'Fiorentina':
        title = 'Fiorentina :purple_circle:'
        color = 0x5c00ad
        logo = 'https://cdn.sportdataapi.com/images/soccer/teams/100/389.png'
        n_team = 6
    elif squadra == 'Genoa':
        title = 'Genoa :red_circle::blue_circle:'
        color = 0xad0031
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/402.png"
        n_team = 8
    elif squadra == 'Inter':
        title = 'Inter :black_circle::blue_circle:'
        color = 0x0034ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/94.png"
        n_team = 9
    elif squadra == 'Juventus':
        title = 'Juventus :white_circle::black_circle:'
        color = 0xbfbfbf
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/108.png"
        n_team = 10
    elif squadra == 'Lazio':
        title = 'Lazio :blue_circle::white_circle:'
        color = 0x0088c2
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/398.png"
        n_team = 11
    elif squadra == 'Milan':
        title = 'Milan :red_circle::black_circle:'
        color = 0xad0031
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/391.png"
        n_team = 12
    elif squadra == 'Napoli':
        title = 'Napoli :blue_circle:'
        color = 0x0034ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/102.png"
        n_team = 13
    elif squadra == 'Roma':
        title = 'Roma :orange_circle::red_circle:'
        color = 0xd46a00
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/401.png"
        n_team = 15
    elif squadra == 'Sampdoria':
        title = 'Sampdoria :blue_circle::white_circle::red_circle:'
        color = 0x0034ad
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/397.png"
        n_team = 16
    elif squadra == 'Sassuolo':
        title = 'Sassuolo :green_circle::black_circle:'
        color = 0x00a838
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/394.png"
        n_team = 17
    elif squadra == 'Torino':
        title = 'Torino :brown_circle:'
        color = 0x913000
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/393.png"
        n_team = 18
    elif squadra == 'Udinese':
        title = 'Udinese :black_circle::white_circle:'
        color = 0xbfbfbf
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/390.png"
        n_team = 19
    elif squadra == 'Verona':
        title = 'Verona :yellow_circle::blue_circle:'
        color = 0xd4e300
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/399.png"
        n_team = 20
    elif squadra == 'Cagliari':
        title = 'Cagliari :red_circle::blue_circle:'
        color = 0xad0031
        logo = "https://cdn.sportdataapi.com/images/soccer/teams/100/395.png"
        n_team = 21
    
    # Requesting player points
    req = requests.get(f'https://www.fantacalcio.it/api/live/{n_team}?g={int(my_round["name"])}&i=16')

    # Formatting the message and the relative embed
    description = '*'

    if req.json() == []:
        description += 'Non sono ancora disponibili i dati della '

    description += f'{my_round["name"]}a giornata Serie A TIM*'

    embedVar = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    
    embedVar.set_thumbnail(url=logo)

    if req.json() != []:

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
            
            if ':x: ' not in eventi and player['ruolo'] == 'P':
                eventi += ':gloves: '
                bonus += 1

            embedVar.add_field(name="\u200b", value=f'{ruolo} {player["nome"][0]}{player["nome"][1:].lower()} - {"SV" if player["voto"] == 55.0 else player["voto"]} **{"SV" if player["voto"] == 55.0 else player["voto"]+bonus}** {eventi}', inline=False)

    # Send everything
    await ctx.reply(embed=embedVar, mention_author=False)
