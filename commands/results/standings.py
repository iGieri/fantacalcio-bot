import discord
import requests

async def standings(ctx, client, FOOTBALL_API_HEADERS):
    params = (
        ("season_id","2100"),
    )
    
    standing_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/standings', headers=FOOTBALL_API_HEADERS, params=params).json()

    

    embedVar = discord.Embed(
        title="Classifica Serie A TIM",
        color=0x00197d
    )

    embedVar.set_thumbnail(url="https://www.legaseriea.it/assets/legaseriea/images/logo_main_seriea.png?v=34")

    for team in standing_req['data']['standings']:
        team_data = {}

        params = (
            ("country_id", "62"),
        )

        teams_req = requests.get(f'https://app.sportdataapi.com/api/v1/soccer/teams/{team["team_id"]}', headers=FOOTBALL_API_HEADERS, params=params).json()

        team_data = teams_req['data']

        logo_stand = ''

        if team['position'] == 1:
            logo_stand = 'scudetto'
        elif team['result'] == 'Champions League':
            logo_stand = 'champions'
        elif team['result'] == 'Europa League':
            logo_stand = 'europa'
        elif team['result'] == 'Conference League Qualification':
            logo_stand = 'conference'
        elif team['result'] == 'Relegation':
            logo_stand = 'serieb'

        embedVar.add_field(name='\u200b', value=f"**{team['position']} {str(discord.utils.get(client.emojis, name=team_data['short_code']))} {team_data['name']} **  {team['points']} {str(discord.utils.get(client.emojis, name=logo_stand)) if logo_stand != '' else ''}", inline=False)

    message = await ctx.reply(embed=embedVar, mention_author=False)

    emojis = ["🔁"]

    for emoji in emojis:
        await message.add_reaction(emoji)

async def standings_now(message, client, FOOTBALL_API_HEADERS):
    params = (
        ("season_id","2100"),
    )
    
    standing_req = requests.get('https://app.sportdataapi.com/api/v1/soccer/standings', headers=FOOTBALL_API_HEADERS, params=params).json()

    

    embedVar = discord.Embed(
        title="Classifica Serie A TIM",
        color=0x00197d
    )

    embedVar.set_thumbnail(url="https://www.legaseriea.it/assets/legaseriea/images/logo_main_seriea.png?v=34")

    for team in standing_req['data']['standings']:
        team_data = {}

        params = (
            ("country_id", "62"),
        )

        teams_req = requests.get(f'https://app.sportdataapi.com/api/v1/soccer/teams/{team["team_id"]}', headers=FOOTBALL_API_HEADERS, params=params).json()

        team_data = teams_req['data']

        logo_stand = ''

        if team['position'] == 1:
            logo_stand = 'scudetto'
        elif team['result'] == 'Champions League':
            logo_stand = 'champions'
        elif team['result'] == 'Europa League':
            logo_stand = 'europa'
        elif team['result'] == 'Conference League Qualification':
            logo_stand = 'conference'
        elif team['result'] == 'Relegation':
            logo_stand = 'serieb'

        embedVar.add_field(name='\u200b', value=f"**{team['position']} {str(discord.utils.get(client.emojis, name=team_data['short_code']))} {team_data['name']} **  {team['points']} {str(discord.utils.get(client.emojis, name=logo_stand)) if logo_stand != '' else ''}", inline=False)

    message = await message.edit(embed=embedVar, mention_author=False)