import discord,os,asyncio
from discord import app_commands,AllowedMentions,TextChannel
from typing import Final
from dotenv import load_dotenv
from responses import get_response
from vidPlayer import play
# Load Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# bot setup
intents = discord.Intents.all() 
intents.message_content = True  # NOQA
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
message = discord.Message

# Queue for audio URLs
queue = []

# tells us when the bot is online
@client.event
async def on_ready() -> None:
    print(f'{client.user} have awakened!')
    await tree.sync()
    print("Ready!")
    client.loop.create_task(check_queue())  # Start the check_queue task

# Background task to check if the bot can start playing the next audio in the queue
async def check_queue():
    await client.wait_until_ready()
    while not client.is_closed():
        if client.voice_clients and not client.voice_clients[0].is_playing() and queue:
            voice_client, url = queue.pop(0)
            await play(voice_client, url)
        await asyncio.sleep(5)

# message functionality
async def send_message(message: message, userMessage: str) -> None:

    if not userMessage:
        print('(Message was empty, maybe intent issue)')
        return
    
    userMessage = userMessage[1:]

    try:
        response = get_response(userMessage)
        if isinstance(response, list):  # If response is a list of strings (chunks)
            for chunk in response:
                await message.channel.send(chunk)
        else:  # If response is a single string
            await message.channel.send(response)

    except Exception as e:
        print(e)
    
#bot commands

def is_admin():
    async def predicate(interaction: discord.Interaction) -> bool:
        # Replace 'administrator' with the specific permission you want to check for
        return interaction.user.guild_permissions.administrator
    return app_commands.check(predicate)

@tree.command(name="hello", description="I`ll hello u back hehehe")
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Hello {interaction.user.mention} this is a slash command!")

@tree.command(name="talk", description="I will say whatever you want me to")
@app_commands.checks.has_permissions(administrator=True)  # This line checks for admin permissions
async def announce(interaction: discord.Integration, channel: discord.TextChannel, message: str):
    await channel.send(message)
    await interaction.response.send_message(f"Message sent to {channel.mention}", ephemeral=True)

@tree.command(name="announce", description="I will announce whatever you want me to")
@app_commands.checks.has_permissions(administrator=True)  # This line checks for admin permissions
async def announce(interaction: discord.Integration, channel: discord.TextChannel, announcement: str):
    allowed_mentions = AllowedMentions(everyone=True)
    await channel.send(f"{announcement}\n ||@everyone||", allowed_mentions=allowed_mentions)
    await interaction.response.send_message(f"Announcement sent to {channel.mention}", ephemeral=True)

@tree.command(name="play", description="I will play the audio of this url")
async def play_command(interaction: discord.Integration, url: str):
    try:
        await interaction.response.defer(ephemeral=True)
    except discord.errors.NotFound:
        await interaction.followup.send("Interaction has expired or is invalid. Please try again.", ephemeral=True)
        return
    if client.voice_clients:
        if interaction.client.voice_clients[0].is_playing():
            queue.append((interaction, url))
            await interaction.followup.send(f'{url} added to queue testplaycommand', ephemeral=True)
            return
    else:
        await play(interaction, url)
        await interaction.followup.send(f'Playing {url}', ephemeral=True)

@tree.command(name="join", description="I will join ur vc")
async def join(interaction: discord.Integration):

    await interaction.response.defer(ephemeral=True)

    voice_channel = interaction.user.voice.channel
    if interaction.client.voice_clients:
        if interaction.user.voice.channel.id == interaction.client.voice_clients[0].channel.id:
            await interaction.followup.send("I am already connected to a voice channel", ephemeral=True)
        else:
            await interaction.client.voice_clients[0].disconnect()
            vc = await voice_channel.connect()
            await interaction.followup.send(f'Joined {voice_channel}', ephemeral=True)
    else:
        vc = await voice_channel.connect()
        await interaction.followup.send(f'Joined {voice_channel}', ephemeral=True)

@tree.command(name="stop", description="I will stop playing audio")
async def stop(interaction: discord.Integration):
    await interaction.response.defer(ephemeral=True)

    if interaction.client.voice_clients:
        if interaction.client.voice_clients[0].is_playing():
            interaction.client.voice_clients[0].stop()
            await interaction.followup.send("Audio stopped", ephemeral=True)
        else:
            await interaction.followup.send("I am not playing audio", ephemeral=True)
    else:
        await interaction.followup.send("I am not connected to a voice channel", ephemeral=True)
     
@tree.command(name="disconnect", description="I will leave")
async def disconnect(interaction: discord.Integration):
    await interaction.response.defer(ephemeral=True)

    if interaction.client.voice_clients:
        if interaction.client.voice_clients[0].is_playing():
            client.voice_clients[0].stop()
            await interaction.client.voice_clients[0].disconnect()
            await interaction.followup.send("Disconnected", ephemeral=True)
        else:
            await interaction.client.voice_clients[0].disconnect()
            await interaction.followup.send("Disconnected", ephemeral=True)

    else:
        await interaction.followup.send("I am not connected to a voice channel", ephemeral=True)

@tree.command(name="mute", description="I will mute everyone in the voice channel")
@app_commands.checks.has_permissions(administrator=True)  # This line checks for admin permissions
async def mute(interaction: discord.Integration):
    await interaction.response.defer(ephemeral=True)

    if interaction.user.voice and interaction.user.voice.channel:
        channel = interaction.user.voice.channel
        for member in channel.members:
            await member.edit(mute=True)
        await interaction.followup.send("Everyone in the voice channel has been muted.", ephemeral=True)
    else:
        await interaction.followup.send("You are not in a voice channel.", ephemeral=True)

@tree.command(name="unmute", description="I will unmute everyone in the voice channel")
@app_commands.checks.has_permissions(administrator=True)  # This line checks for admin permissions
async def mute(interaction: discord.Integration):
    await interaction.response.defer(ephemeral=True)

    if interaction.user.voice and interaction.user.voice.channel:
        channel = interaction.user.voice.channel
        for member in channel.members:
            await member.edit(mute=False)
        await interaction.followup.send("Everyone in the voice channel has been muted.", ephemeral=True)
    else:
        await interaction.followup.send("You are not in a voice channel.", ephemeral=True)

@tree.command(name='move', description='Move a user to a specified voice channel.')
@app_commands.describe(member='The user to move', channel='The voice channel to move the user to')
@app_commands.checks.has_permissions(administrator=True)  # This line checks for admin permissions
async def move(interaction: discord.Interaction, member: discord.Member, channel: discord.VoiceChannel) -> None:
    await interaction.response.defer(ephemeral=True)
    
    # Check if the member is in a voice channel
    if member.voice is None:
        await interaction.followup.send(f"{member.display_name} is not in a voice channel.", ephemeral=True)
        return

    try:
        # Move the member to the specified channel
        await member.move_to(channel)
        await interaction.followup.send(f"Moved {member.display_name} to {channel.name}.")
    except discord.Forbidden:
        await interaction.followup.send("I don't have permission to move this user.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Failed to move {member.display_name}: {e}", ephemeral=True)

#@tree.command(name="xo", description="XO.")
#async def xo(interaction: discord.Integration):

@tree.command(name="skip", description="Skips the current audio")
async def skip(interaction: discord.Integration):
    await interaction.response.defer(ephemeral=True)
    if client.voice_clients:
        if interaction.client.voice_clients[0].is_playing():
            interaction.client.voice_clients[0].stop()
            await interaction.followup.send("Audio skipped", ephemeral=False)
            if queue:
                voice_client, url = queue.pop(0)
                await play(voice_client, url)
            else:
                await interaction.followup.send("Queue is empty", ephemeral=True)
        else:
            await interaction.followup.send("I am not playing audio", ephemeral=True)
    else:
        await interaction.followup.send("I am not connected to a voice channel", ephemeral=True)

@tree.command(name="show_queue", description="Shows the current queue")
async def show_queue(interaction: discord.Integration):
    await interaction.response.defer(ephemeral=True)
    embed = discord.Embed(title="queue", description="Shows the current queue!", color=0x00ff00)
    if queue:
        for i, (voice_client, url) in enumerate(queue):
            embed.add_field(name=f"{i+1}. {url}", value=f"Requested by {voice_client.user.mention}", inline=False)
    else:
        embed.description = "The queue is currently empty."
    await interaction.followup.send(embed=embed, ephemeral=True)

@tree.command(name="help", description="I Guide You Through The 1+1=0 Commands, drink water!")
async def help(interaction: discord.Integration):
    await interaction.response.defer(ephemeral=True)
    embed = discord.Embed(title="Help Commands", description="A guide through The 1+1=0 Commands, drink water!", color=0x00ff00)
    
    embed.add_field(name="/hello", value="I'll hello you back hehehe", inline=False)
    embed.add_field(name="/talk", value="I will say whatever you want me to", inline=False)
    embed.add_field(name="/announce", value="I will announce whatever you want me to", inline=False)
    embed.add_field(name="/play", value="I will play the audio of this URL", inline=False)
    embed.add_field(name="/join", value="I will join your voice channel", inline=False)
    embed.add_field(name="/stop", value="I will stop playing audio", inline=False)
    embed.add_field(name="/disconnect", value="I will leave the voice channel", inline=False)
    embed.add_field(name="/mute", value="I will mute everyone in the voice channel", inline=False)
    embed.add_field(name="/unmute", value="I will unmute everyone in the voice channel", inline=False)
    embed.add_field(name="/move", value="Move a user to a specified voice channel.", inline=False)
    embed.add_field(name="skip", value="Skips the current audio", inline=False)
    embed.add_field(name="show_queue", value="Shows the current queue", inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)


# handles incomming messages

@client.event
async def on_message(message: message) -> None:
    if message.author == client.user:
        return
    userMessage: str = str(message.content) if message.content else ""
    if not userMessage.startswith('!'):
        return
    username: str = str(message.author)
    userMessage: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{userMessage}"')
    await send_message(message, userMessage)


# main
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()