import hikari
from secret import TOKEN
bot = hikari.GatewayBot(token=TOKEN)

"""
BanEvent
    BanCreateEvent
        guild_id, shard, user, user_id
    BanDeleteEvent
        guild_id, shard, user
"""

@bot.listen(hikari.BanEvent)
async def Ban_Event(event):
    user = event.user

    print(f"There is an update to {user}'s Ban Status.")

@bot.listen(hikari.BanCreateEvent)
async def Ban_Create(event):
    guild_id= event.guild_id
    shard= event.shard
    user = event.user
    user_id = event.user_id

    print(f"{user} having {user_id} is banned from Guild - {guild_id} in Shard {shard}.")

@bot.listen(hikari.BanDeleteEvent)
async def Unban(event):
    guild_id = event.guild_id
    shard = event.shard
    user = event.user

    print(f"{user} has been unbanned from Guild - {guild_id} in Shard - {shard}.")

bot.run()
