import discord

async def invite(ctx):
    embedVar = discord.Embed(
        title='Invita il bot nel tuo server!',
        description='*Porta tutto il mondo di fantacalcio.it nel tuo server ora!*',
        color=0x1853c9
    )

    embedVar.set_thumbnail(url="https://content.fantacalcio.it/web/img/app/fantacalcio.png")

    embedVar.add_field(name='Link', value='[Invita](https://discord.com/oauth2/authorize?client_id=883501118863323216&permissions=277025745920&scope=bot%20applications.commands)')
    
    await ctx.reply(embed=embedVar, mention_author=False)
