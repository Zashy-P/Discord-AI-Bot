import discord,asyncio

async def playXO(interaction: discord.Integration):
    
    emoji_dict = {
    ":top_left_blank:": "<:top_left_blank:1289363116521422939>",
    ":mid_left_blank:": "<:mid_left_blank:1289363112251756625>",
    ":bottom_left_blank:": "<:bottom_left_blank:1289363108179218514>",
    ":top_mid_blank:": "<:top_mid_blank:1289363118090223656>",
    ":mid_mid_blank:": "<:mid_mid_blank:1289363115078844447>",
    ":bottom_mid_blank:": "<:bottom_mid_blank:1289363109470933022>",
    ":top_right_blank:": "<:top_right_blank:1289363119453507595>",
    ":mid_right_blank:": "<:mid_right_blank:1289363113577152543>",
    ":bottom_right_blank:": "<:bottom_right_blank:1289363110905512087>",

    ":top_left_blank_select:": "<:top_left_blank_select",
    ":mid_left_blank_select:": "<:mid_left_blank_select",
    ":bottom_left_blank_select:": "<:bottom_left_blank_select",
    ":top_mid_blank_select:": ":top_mid_blank_select:",
    ":mid_mid_blank_select:": ":mid_mid_blank_select:",
    ":bottom_mid_blank_select:": ":bottom_mid_blank_select:",
    ":top_right_blank_select:": "<:top_right_blank_select",
    ":mid_right_blank_select:": "<:mid_right_blank_select",
    ":bottom_right_blank_select:": "<:bottom_right_blank_select"
    
}
    # Define the initial board elements
    board_list = [
        ":top_left_blank:", ":mid_left_blank:", ":bottom_left_blank:",
        ":top_mid_blank:", ":mid_mid_blank_select:", ":bottom_mid_blank:", 
        ":top_right_blank:", ":mid_right_blank:", ":bottom_right_blank:"
]   
    
    # Function to replace the emoji name with the corresponding emoji id using the emoji dictionary
    def update_board(board_list):
        # Replace text representations with custom emojis
        board = emoji_dict[board_list[0]] + emoji_dict[board_list[3]] + emoji_dict[board_list[6]] + "\n"  + emoji_dict[board_list[1]] + emoji_dict[board_list[4]] + emoji_dict[board_list[7]] + "\n" + emoji_dict[board_list[2]] + emoji_dict[board_list[5]] + emoji_dict[board_list[8]] + "\n" "(React Within 60 Seconds)"
        return board

    # initial board elements id 
    board = update_board(board_list)

    # Create the embed
    embed = discord.Embed(title="Tic-Tac-Toe ", description=board, color=0x00ff00)
    
    # Send the embed as a response and get the message object
    await interaction.response.send_message(embed=embed, ephemeral=False)
    message = await interaction.original_response()

    # Add reactions for movement
    reactions = ['⬅️', '⬆️', '⬇️', '➡️']
    for reaction in reactions:
        await message.add_reaction(reaction)

    # Define the reaction handler
    def check(reaction, user):
        return user == interaction.user and str(reaction.emoji) in reactions
    
    def moveUp():
        for i in board_list:
            index = board_list.index(i)
            if i.endswith("_select:"):
                if i == ":top_left_blank_select:" or i == ":top_mid_blank_select:" or i == ":top_right_blank_select:": 
                    board_list[index] = i.replace("_select", "")
                    board_list[index + 2] = board_list[index + 2][:-1] + "_select:"
                    break                           
                else:
                    board_list[index] = i.replace("_select", "")
                    board_list[index - 1] = board_list[index - 1][:-1] + "_select:"
                    break
    def moveDown():
        for i in board_list:
            index = board_list.index(i)
            if i.endswith("_select:"):
                if i == ":bottom_left_blank_select:" or i == ":bottom_mid_blank_select:" or i == ":bottom_right_blank_select:": 
                    board_list[index] = i.replace("_select", "")
                    board_list[index - 2] = board_list[index - 2][:-1] + "_select:"
                    break                           
                else:
                    board_list[index] = i.replace("_select", "")
                    board_list[index + 1] = board_list[index + 1][:-1] + "_select:"
                    break
    
    def moveRight():
        for i in board_list:
            index = board_list.index(i)
            if i.endswith("_select:"):
                if i == ":top_right_blank_select:" or i == ":mid_right_blank_select:" or i == ":bottom_right_blank_select:": 
                    board_list[index] = i.replace("_select", "")
                    board_list[index - 6] = board_list[index - 6][:-1] + "_select:"
                    break                           
                else:
                    board_list[index] = i.replace("_select", "")
                    board_list[index + 3] = board_list[index + 3][:-1] + "_select:"
                    break

    def moveLeft():
        for i in board_list:
            index = board_list.index(i)
            if i.endswith("_select:"):
                if i == ":top_left_blank_select:" or i == ":mid_left_blank_select:" or i == ":bottom_left_blank_select:": 
                    board_list[index] = i.replace("_select", "")
                    board_list[index + 6] = board_list[index + 6][:-1] + "_select:"
                    break                           
                else:
                    board_list[index] = i.replace("_select", "")
                    board_list[index - 3] = board_list[index - 3][:-1] + "_select:"
                    break
    
    
    while True:

        try:
            reaction, user = await interaction.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            break

        else:
            if str(reaction.emoji) == '⬆️':
                moveUp()
            
            elif str(reaction.emoji) == '⬇️':
                moveDown()
            
            elif str(reaction.emoji) == '➡️':
                moveRight()
            
            elif str(reaction.emoji) == '⬅️':
                moveLeft()

            # Update the board and remove the reaction
            board = update_board(board_list)
            embed.description = board
            await message.edit(embed=embed)
            await message.remove_reaction(reaction, user)