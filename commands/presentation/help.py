import discord

async def help(ctx):
    embedVar = discord.Embed(
        title='Ecco tutti i comandi disponibili!',
        description='',
        color=0x1853c9
    )

    embedVar.set_thumbnail(url="https://content.fantacalcio.it/web/img/app/fantacalcio.png")

    embedVar.add_field(name='f!help', value='Elenco di tutti i comandi disponibili')
    embedVar.add_field(name='f!invite', value='Link per invitare il bot nel proprio server')
    embedVar.add_field(name='f!live <squadra>', value='N.A.')
    embedVar.add_field(name='f!matches', value='Mostra i risultati in diretta della giornata corrente')
    embedVar.add_field(name='f!standings', value='Mostra la classifica di Serie A TIM in diretta')
    embedVar.add_field(name='f!marcatori', value='Soon...')
    
    await ctx.reply(embed=embedVar, mention_author=False)