import discord

async def playXO(interaction: discord.Integration):

    # Define the initial board elements 
    a1 = ":top_left_blank_ZashyBot:"
    a2 = ":mid_left_blank_ZashyBot:"
    a3 = ":bottom_left_blank_ZashyBot:"
    b1 = ":top_mid_blank_ZashyBot:"
    b2 = ":mid_mid_blank_ZashyBot:"
    b3 = ":bottom_mid_blank_ZashyBot:"
    c1 = ":top_right_blank_ZashyBot:"
    c2 = ":mid_right_blank_ZashyBot:"
    c3 = ":bottom_right_blank_ZashyBot:"

    # Create the board representation
    board = f"{a1} {b1} {c1}\n{a2} {b2} {c2}\n{a3} {b3} {c3}"

    # Create the embed
    embed = discord.Embed(title="Tic-Tac-Toe", description=board, color=0x00ff00)

    # Send the embed as a response
    await interaction.response.send_message(embed=embed, ephemeral=False)