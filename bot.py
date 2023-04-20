import discord
import responses
import os



def run_discord_bot():

    TOKEN = os.environ['TOKEN']
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("start working")


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_name = str(message.author),
        user_message = str(message.content)
        channel = str(message.channel)
        print("message :",message)
        print(f"{user_name} said {user_message} in {channel}")

        if user_message and user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)
    
    client.run(TOKEN)





async def send_message(message, user_message, is_private):
    print("message is: ", user_message)
    try:
        response = responses.handle_response(user_message)
    
        if is_private:
            await message.author.send(response)
        else :
            await message.channel.send(response)


    except Exception as e:
        await message.author.send(e)

