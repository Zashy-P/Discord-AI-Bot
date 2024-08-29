import discord,os,subprocess,asyncio

intents = discord.Intents.all() 
client = discord.Client(intents=intents)

downloaded_files = []
max_files_to_keep = 2

async def play(interaction: discord.Integration, url: str):

    # Checks that it is a vlid yt url
    if not url.startswith("https://www.youtube.com/watch?v=") and not url.startswith("http://www.youtube.com/watch?v=") and not url.startswith("https://www.youtube.com/shorts/")  and not url.startswith("http://www.youtube.com/shorts/") and not url.startswith("https://youtu.be/") and not url.startswith("http://youtu.be/"):
        await interaction.followup.send("Invalid YouTube URL", ephemeral=True)
        return
    
    # Gets the vid id to name da file
    def extract_video_id(url: str) -> str:
        if "watch?v=" in url:
            return url.split('watch?v=')[-1]
        elif "/shorts/" in url:
            return url.split('/shorts/')[-1]
        elif "youtu.be/" in url:
            video_id = url.split('youtu.be/')[-1]
            video_id = video_id.split('=')[-1]
            return video_id
        else:
            return "" 
        
    video_id = extract_video_id(url)
    if not video_id:
        await interaction.followup.send("Could not extract video ID from URL", ephemeral=True)
        return

    audio_file_name = f"{video_id}.mp3"
    audio_file_path = os.path.join(os.getcwd(), audio_file_name)
    
    # Attempt to delete the oldest file if exceeding max_files_to_keep
    if len(downloaded_files) >= max_files_to_keep:
        oldest_file = downloaded_files.pop(0)  # Remove the oldest file from the list
        try:
            if os.path.exists(oldest_file):
                os.remove(oldest_file)
                print(f"Deleted old file: {oldest_file}")
        except PermissionError:
            print(f"Failed to delete {oldest_file} - file is in use.")

    async def downloadAudio(url: str, audio_file_path: str):
        download_command = f"yt-dlp -f bestaudio --extract-audio --audio-format mp3 -o \"{audio_file_path}\" {url}"
        downloaded_files.append(audio_file_path)
        process = subprocess.run(download_command, shell=True)

        if process.returncode != 0:
            await interaction.followup.send("Error downloading audio", ephemeral=True)
            return
        
    # checks if the user is not in a voice channel
    if not interaction.user.voice or not interaction.user.voice.channel:
        await interaction.followup.send("You need to be in a voice channel", ephemeral=True)
        return
    
    # checks if the bot is connected to any voice channel
    if interaction.client.voice_clients:
        # checks if the bot is in the same voice channel as the user
        if interaction.user.voice.channel.id == interaction.client.voice_clients[0].channel.id:
            await downloadAudio(url, audio_file_path)
            source = discord.FFmpegPCMAudio(audio_file_path)
            vc = interaction.client.voice_clients[0]
            vc.play(source)
        # if the bot is in a different voice channel connect to the user's vc
        else:
            await interaction.client.voice_clients[0].disconnect()
            voice_channel = interaction.user.voice.channel
            vc = await voice_channel.connect()
            await downloadAudio(url, audio_file_path)
            # play the audio
            source = discord.FFmpegPCMAudio(audio_file_path)
            vc.play(source)

    # if the bot is not connected to any voice channel
    else:
        await downloadAudio(url, audio_file_path)
        voice_channel = interaction.user.voice.channel
        vc = await voice_channel.connect()
        source = discord.FFmpegPCMAudio(audio_file_path)
        vc.play(source)
