import hikari
from secret import TOKEN
bot = hikari.GatewayBot(token=TOKEN)

"""
Messages
    hikari.MessageCreateEvent # All Messages

    Guild Messages - Messages sent on a server.
        hikari.GuildMessageCreateEvent

    DM Messages - Messages that are sent to the bot.
        hikari.DMMessageCreateEvent

"""
@bot.listen(hikari.MessageCreateEvent)
async def handle_allMessages(event):
    print("A new message has been sent.")

@bot.listen(hikari.GuildMessageCreateEvent)
async def handle_message(event):
    Author = event.author
    Author_ID = event.author_id
    Content = event.content
    Embed = event.embeds
    Message = event.message
    Message_ID = event.message_id
    channel_ID = event.channel_id
    Guild_ID = event.guild_id
    Bot = event.is_bot
    Human = event.is_human
    Webhook = event.is_webhook
    print(Author, " said ", Content, " on ", channel_ID, " ", Guild_ID)

@bot.listen(hikari.DMMessageCreateEvent)
async def handle_DM_message(event):
    Author = event.author
    Author_ID = event.author_id
    Content = event.content
    Embed = event.embeds
    Message = event.message
    Message_ID = event.message_id
    Bot = event.is_bot
    Human = event.is_human
    Webhook = event.is_webhook 
    print(Author, " said ", Content, " in DM." )


bot.run()