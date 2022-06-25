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
# Event triggered whenever a user's ban status is modified for a server. 
async def Ban_Event(event):
    user = event.user           # Gives Username#1234 for concerned user.
    
    print(f"There is an update to {user}'s Ban Status.")

@bot.listen(hikari.BanCreateEvent)
# Event triggered whenever a user is banned from a server.
async def Ban_Create(event):
    guild_id= event.guild_id    # Gives a unique numeric Server ID for the concerned server.
    
    shard= event.shard          # Gives Shard ID under which the particular instance of bot is being run.
    
    user = event.user           # Gives Username#1234 for concerned user.
    
    user_id = event.user_id     # Gives a unique numeric User ID for concerned user.

    print(f"{user} having {user_id} is banned from Guild - {guild_id} in Shard {shard}.")

@bot.listen(hikari.BanDeleteEvent)
# Event Triggered whenever a user is unbanned from a server.
async def Unban(event):
    guild_id= event.guild_id    # Gives a unique numeric Server ID for the concerned server.
    
    shard= event.shard          # Gives Shard ID under which the particular instance of bot is being run.
    
    user = event.user           # Gives Username#1234 for concerned user.

    print(f"{user} has been unbanned from Guild - {guild_id} in Shard - {shard}.")

bot.run()
