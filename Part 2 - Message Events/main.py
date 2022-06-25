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
# Event Triggered whenever a message is recieved by the bot on any channel, DM or Server.
async def handle_all_Messages(event):

    print("A new message has been sent.")


@bot.listen(hikari.GuildMessageCreateEvent)
# Event Triggered whenever a message is recieved by the bot on a Server.
async def handle_message(event):
    
    Author = event.author               # Gives Username#1234 for user that sent the message.

    Author_ID = event.author_id         # Gives a unique numeric User ID for user that sent the message

    Content = event.content             # Gives Text segment of Message as a String

    Embed = event.embeds                # Gives Embed segment of Message

    Message = event.message             # Gives all data of Message as a Dictionary

    Message_ID = event.message_id       # Gives a Unique Numeric Message ID

    Channel_ID = event.channel_id       # Gives a Unique Numeric Channel ID for the channel in which the message was sent. 
    
    Guild_ID = event.guild_id           # Gives a Unique Numeric Guild ID for the server in which the message was sent.
    
    Bot = event.is_bot                  # Gives a boolean value if the author of message is a Bot
    
    Human = event.is_human              # Gives a boolean value if the author of message is a Human
    
    Webhook = event.is_webhook          # Gives a boolean value if the author of message is a Webhook

    print(Author, " said ", Content, " on ", Channel_ID, " ", Guild_ID)


@bot.listen(hikari.DMMessageCreateEvent)
# Event Triggered whenever a direct message is recieved by the bots. 
async def handle_DM_message(event):
    
    Author = event.author               # Gives Username#1234 for user that sent the message.

    Author_ID = event.author_id         # Gives a unique numeric User ID for user that sent the message

    Content = event.content             # Gives Text segment of Message as a String

    Embed = event.embeds                # Gives Embed segment of Message

    Message = event.message             # Gives all data of Message as a Dictionary

    Message_ID = event.message_id       # Gives a Unique Numeric Message ID
    
    Bot = event.is_bot                  # Gives a boolean value if the author of message is a Bot
    
    Human = event.is_human              # Gives a boolean value if the author of message is a Human
    
    Webhook = event.is_webhook          # Gives a boolean value if the author of message is a Webhook

    print(Author, " said ", Content, " in DM." )


bot.run()
