import discord,asyncio


async def playXO(interaction: discord.Integration, client):

    emoji_dict = {
    #empty 
    ":top_left_empty:": "<:top_left_empty:1292214891394105344>",
    ":top_mid_empty:": "<:top_mid_empty:1292214896636723201>",
    ":top_mid_2_empty:": "<:top_mid_2_empty:1292214895093219409>",
    ":top_right_empty:": "<:top_right_empty:1292214983110688802>",

    ":mid_left_empty:": "<:mid_left_empty:1292214876911042682>",
    ":mid_left_2_empty:": "<:mid_left_2_empty:1292214875317342329>",
    ":mid_mid_empty:": "<:mid_mid_empty:1292214884536422643>",
    ":mid_mid_2_empty:": "<:mid_mid_2_empty:1292214879335350282>",
    ":mid_mid_3_empty:": "<:mid_mid_3_empty:1292214881373913244>",
    ":mid_mid_4_empty:": "<:mid_mid_4_empty:1292214882879668306>",
    ":mid_right_empty:": "<:mid_right_empty:1292214888378400808>",
    ":mid_right_2_empty:": "<:mid_right_2_empty:1292214981537955910>",

    ":bottom_left_empty:": "<:bottom_left_empty:1292214868589543505>",
    ":bottom_mid_empty:": "<:bottom_mid_empty:1292214870049034311>",
    ":bottom_mid_2_empty:": "<:bottom_mid_2_empty:1292214873421254676>",
    ":bottom_right_empty:": "<:bottom_right_empty:1292214871487938673>",

    #empty select
    ":top_left_empty_select:": "<:top_left_empty_select:1292515287920279696>",
    ":top_mid_empty_select:": "<:top_mid_empty_select:1292515302646485052>",
    ":top_mid_2_empty_select:": "<:top_mid_2_empty_select:1292515296841695283>",
    ":top_right_empty_select:": "<:top_right_empty_select:1292515308124246016>",

    ":mid_left_empty_select:": "<:mid_left_empty_select:1292515249202921533>",
    ":mid_left_2_empty_select:": "<:mid_left_2_empty_select:1292515238570098858>",
    ":mid_mid_empty_select:": "<:mid_mid_empty_select:1292515270887477340>",
    ":mid_mid_2_empty_select:": "<:mid_mid_2_empty_select:1292515258950225992>",
    ":mid_mid_3_empty_select:": "<:mid_mid_3_empty_select:1292515263136403456>",
    ":mid_mid_4_empty_select:": "<:mid_mid_4_empty_select:1292515265778679910>",
    ":mid_right_empty_select:": "<:mid_right_empty_select:1292515282446848081>",
    ":mid_right_2_empty_select:": "<:mid_right_2_empty_select:1292515275660329041>",

    ":bottom_left_empty_select:": "<:bottom_left_empty_select:1292515201526140968>",
    ":bottom_mid_empty_select:": "<:bottom_mid_empty_select:1292515190704705576>",
    ":bottom_mid_2_empty_select:": "<:bottom_mid_2_empty_select:1292515213123518525>",
    ":bottom_right_empty_select:": "<:bottom_right_empty_select:1292515222954840125>",

    #o
    ":top_left_o:": "<:top_left_o:1292153487655833712>",
    ":top_mid_o:": "<:top_mid_o:1292153387139334256>",
    ":top_mid_2_o:": "<:top_mid_2_o:1292153385650229320>",
    ":top_right_o:": "<:top_right_o:1292153488972709908>",

    ":mid_left_o:": "<:mid_left_o:1292207194720174120>",
    ":mid_left_2_o:": "<:mid_left_2_o:1292153368902373418>",
    ":mid_mid_o:": "<:mid_mid_o:1292153378670907625>",
    ":mid_mid_2_o:": "<:mid_mid_2_o:1292207196150562857>",
    ":mid_mid_3_o:": "<:mid_mid_3_o:1292153375147950155>",
    ":mid_mid_4_o:": "<:mid_mid_4_o:1292153377136054285>",
    ":mid_right_o:": "<:mid_right_o:1292153381984665702>",
    ":mid_right_2_o:": "<:mid_right_2_o:1292153485974048778>",

    ":bottom_left_o:": "<:bottom_left_o:1292153362648662058>",
    ":bottom_mid_o:": "<:bottom_mid_o:1292153366255894589>",
    ":bottom_mid_2_o:": "<:bottom_mid_2_o:1292153364846608406>",
    ":bottom_right_o:": "<:bottom_right_o:1292153367728226354>",

    #o select
    ":top_left_o_select:": "<:top_left_o_select:1292156487891816570>",
    ":top_mid_o_select:": "<:top_mid_o_select:1292156491444523111>",
    ":top_mid_2_o_select:": "<:top_mid_2_o_select:1292156980089196657>",
    ":top_right_o_select:": "<:top_right_o_select:1292156584037716059>",

    ":mid_left_o_select:": "<:mid_left_o_select:1292207431388237856>",
    ":mid_left_2_o_select:": "<:mid_left_2_o_select:1292156471420784690>",
    ":mid_mid_o_select:": "<:mid_mid_o_select:1292156481721991248>",
    ":mid_mid_2_o_select:": "<:mid_mid_2_o_select:1292207434223583303>",
    ":mid_mid_3_o_select:": "<:mid_mid_3_o_select:1292156476596420718>",
    ":mid_mid_4_o_select:": "<:mid_mid_4_o_select:1292156479180116119>",
    ":mid_right_o_select:": "<:mid_right_o_select:1292156582624366672>",
    ":mid_right_2_o_select:": "<:mid_right_2_o_select:1292156483735392401>",

    ":bottom_left_o_select:": "<:bottom_left_o_select:1292156465863458838>",
    ":bottom_mid_o_select:": "<:bottom_mid_o_select:1292156468426051655>",
    ":bottom_mid_2_o_select:": "<:bottom_mid_2_o_select:1292156466983079988>",
    ":bottom_right_o_select:": "<:bottom_right_o_select:1292156469579350159>",

    #x
    ":top_left_x:": "<:top_left_x:1292202644722683915>",
    ":top_mid_x:": "<:top_mid_x:1292202648568594482>",
    ":top_mid_2_x:": "<:top_mid_2_x:1292202646781952041>",
    ":top_right_x:": "<:top_right_x:1292202650992902256>",

    ":mid_left_x:": "<:mid_left_x:1292202599726186566>",
    ":mid_left_2_x:": "<:mid_left_2_x:1292202597918183435>",
    ":mid_mid_x:": "<:mid_mid_x:1292202640423518301>",
    ":mid_mid_2_x:": "<:mid_mid_2_x:1292202601621749924>",
    ":mid_mid_3_x:": "<:mid_mid_3_x:1292202603119378546>",
    ":mid_mid_4_x:": "<:mid_mid_4_x:1292202638791675904>",
    ":mid_right_x:": "<:mid_right_x:1292202643086770261>",
    ":mid_right_2_x:": "<:mid_right_2_x:1292202642071879701>",

    ":bottom_left_x:": "<:bottom_left_x:1292202591660277893>",
    ":bottom_mid_x:": "<:bottom_mid_x:1292202594915061902>",
    ":bottom_mid_2_x:": "<:bottom_mid_2_x:1292202593308643368>",
    ":bottom_right_x:": "<:bottom_right_x:1292202596790042694>",

    #x select
    ":top_left_x_select:": "<:top_left_x_select:1292202733289607178>",
    ":top_mid_x_select:": "<:top_mid_x_select:1292202738427494481>",
    ":top_mid_2_x_select:": "<:top_mid_2_x_select:1292202736967876742>",
    ":top_right_x_select:": "<:top_right_x_select:1292202739828260959>",

    ":mid_left_x_select:": "<:mid_left_x_select:1292202694047694908>",
    ":mid_left_2_x_select:": "<:mid_left_2_x_select:1292202692189618248>",
    ":mid_mid_x_select:": "<:mid_mid_x_select:1292202728512295005>",
    ":mid_mid_2_x_select:": "<:mid_mid_2_x_select:1292202695716769963>",
    ":mid_mid_3_x_select:": "<:mid_mid_3_x_select:1292202697373646981>",
    ":mid_mid_4_x_select:": "<:mid_mid_4_x_select:1292202727169851483>",
    ":mid_right_x_select:": "<:mid_right_x_select:1292202731133472819>",
    ":mid_right_2_x_select:": "<:mid_right_2_x_select:1292202729871245412>",

    ":bottom_left_x_select:": "<:bottom_left_x_select:1292202686149562448>",
    ":bottom_mid_x_select:": "<:bottom_mid_x_select:1292202689240764416>",
    ":bottom_mid_2_x_select:": "<:bottom_mid_2_x_select:1292202687831609344>",
    ":bottom_right_x_select:": "<:bottom_right_x_select:1292202690784264253>",

    # home emojis
    ":home1:": "<:home1:1289957387633164299>",
    ":home2:": "<:home2:1289957389495304232>",
    ":home3:": "<:home3:1289957391047331975>",
    ":home4:": "<:home4:1289957392871719015>",
    ":home5:": "<:home5:1289957394792845353>",
    ":home6:": "<:home6:1289957397376401428>",
    ":home7:": "<:home7:1289957398634565792>",
    ":home8:": "<:home8:1289957399901241522>",
    ":home9:": "<:home9:1289963683056979998>",
    ":home10:": "<:home10:1289963684407545887>",
    ":home11:": "<:home11:1289963686278074428>",
    ":home12:": "<:home12:1289963687779762186>",
    ":home13:": "<:home13:1289960304704225290>",
    ":home14:": "<:home14:1289960306939924562>",
    ":home15:": "<:home15:1289960308777160801>",
    ":home16:": "<:home16:1289960310047772744>",

    ":homeai9:": "<:homeai9:1289957401516052532>",
    ":homeai10:": "<:homeai10:1289957407551787038>",
    ":homeai11:": "<:homeai11:1289957408952811632>",
    ":homeai12:": "<:homeai12:1289957410425016411>",

    ":homepl13:": "<:homepl13:1289963250162733097>",
    ":homepl14:": "<:homepl14:1289963251651842048>",
    ":homepl15:": "<:homepl15:1289963252859801654>",
    ":homepl16:": "<:homepl16:1289963253757116469>",
    
     # reaction emojis
    ":green_arrow_up:": "<:green_arrow_up:1377762645301792798>",
    ":green_arrow_down:": "<:green_arrow_down:1377762636443160749>",
    ":green_arrow_left:": "<:green_arrow_left:1377762634010464306>",
    ":green_arrow_right:": "<:green_arrow_right:1377762638385250529>",
    ":select_x:": "<:select_x:1377763632028450857>",
    ":select_o:": "<:select_o:1377763630421905478>",
    ":select_empty:": "<:select_empty:1377763628899500032>",
}
    # Initial board setup
    initial_board_dict = {
    "top_left": ":home1:", "top_mid": ":home2:", "top_mid_2": ":home3:", "top_right": ":home4:", 
    "mid_left": ":home5:", "mid_mid": ":home6:", "mid_mid_2": ":home7:", "mid_right": ":home8:",
    "mid_left_2": ":home9:", "mid_mid_3": ":home10:", "mid_mid_4": ":home11:", "mid_right_2": ":home12:", 
    "bottom_left": ":homepl13:", "bottom_mid": ":homepl14:", "bottom_mid_2": ":homepl15:", "bottom_right": ":homepl16:",
    }

    state= {"select_location": "homepl"}

    # game board setup
    active_board_dict = {
        "top_left": ":top_left_empty:", "top_mid": ":top_mid_empty:", "top_mid_2": ":top_mid_2_empty:", "top_right": ":top_right_empty:",
        "mid_left": ":mid_left_empty:", "mid_mid": ":mid_mid_empty_select:", "mid_mid_2": ":mid_mid_2_empty_select:", "mid_right": ":mid_right_empty:", 
        "mid_left_2": ":mid_left_2_empty:", "mid_mid_3": ":mid_mid_3_empty_select:", "mid_mid_4": ":mid_mid_4_empty_select:", "mid_right_2":":mid_right_2_empty:", 
        "bottom_left": ":bottom_left_empty:", "bottom_mid": ":bottom_mid_empty:", "bottom_mid_2": ":bottom_mid_2_empty:", "bottom_right": ":bottom_right_empty:"

    }  

    
    # made lists for squares that require more than 1 emoji
    top_mid_square = ["top_mid", "top_mid_2"]
    mid_left_square = ["mid_left", "mid_left_2"]
    mid_mid_square = ["mid_mid", "mid_mid_2", "mid_mid_3", "mid_mid_4"]
    mid_right_square = ["mid_right", "mid_right_2"]
    bottom_mid_square = ["bottom_mid", "bottom_mid_2"]
    home_ai_square = ["mid_left_2", "mid_mid_3", "mid_mid_4", "mid_mid_right_2"]
    home_player_square = ["bottom_left", "bottom_mid", "bottom_mid_2", "bottom_right"]

    
    # Function to replace the emoji name with the emoji id using the emoji dictionary
    def active_update_board(board_dict):
        # Replace text representations with custom emojis
        active_board = (emoji_dict[board_dict["top_left"]] + emoji_dict[board_dict["top_mid"]] + emoji_dict[board_dict["top_mid_2"]] + emoji_dict[board_dict["top_right"]] + "\n"  
                + emoji_dict[board_dict["mid_left"]] + emoji_dict[board_dict["mid_mid"]] + emoji_dict[board_dict["mid_mid_2"]] + emoji_dict[board_dict["mid_right"]]+ "\n" 
                + emoji_dict[board_dict["mid_left_2"]] + emoji_dict[board_dict["mid_mid_3"]] + emoji_dict[board_dict["mid_mid_4"]] + emoji_dict[board_dict["mid_right_2"]] + "\n" 
                + emoji_dict[board_dict["bottom_left"]] + emoji_dict[board_dict["bottom_mid"]] + emoji_dict[board_dict["bottom_mid_2"]] + emoji_dict[board_dict["bottom_right"]] 
            )
        return active_board

    # initial board elements id 
    board = active_update_board(initial_board_dict)
    
    # Send the embed as a response and get the message object
    await interaction.response.send_message(board, ephemeral=False)
    message = await interaction.original_response()

    # define win condition board
    win_condition_board = {
    "top_left": None, "top_mid": None, "top_right": None,
    "mid_left": None, "mid_mid": None, "mid_right": None,
    "bottom_left": None, "bottom_mid": None, "bottom_right": None
    }
    
    win_lines = [
    # Rows
    ["top_left", "top_mid", "top_right"],
    ["mid_left", "mid_mid", "mid_right"],
    ["bottom_left", "bottom_mid", "bottom_right"],
    # Columns
    ["top_left", "mid_left", "bottom_left"],
    ["top_mid", "mid_mid", "bottom_mid"],
    ["top_right", "mid_right", "bottom_right"],
    # Diagonals
    ["top_left", "mid_mid", "bottom_right"],
    ["top_right", "mid_mid", "bottom_left"],
    ]

    # checls if win condition is met
    def check_for_win():
        for line in win_lines:
            a, b, c = line
            if (
                win_condition_board[a] is not None
                and win_condition_board[a] == win_condition_board[b] == win_condition_board[c]
            ):
                return True
        return False
    
    # checks for a draw
    def check_for_draw():
        for key in win_condition_board:
            if win_condition_board[key] is None:
                return False
        return True


    #move up function
    def move_up():
        if state["select_location"] == "homepl":
            state["select_location"] = "homeai"
            for board_pos in home_player_square:
                initial_board_dict[board_pos] = initial_board_dict[board_pos].replace("pl", "")
            for board_pos in home_ai_square:
                initial_board_dict[board_pos] = home_ai_square[board_pos]

        elif state["select_location"] == "homeai":
            state["select_location"] = "homepl"
            for board_pos in home_ai_square:
                initial_board_dict[board_pos] = initial_board_dict[board_pos].replace("ai", "")
            for board_pos in home_player_square:
                initial_board_dict[board_pos] = home_player_square[board_pos]
        
        elif state["select_location"] == "top_left":
            state["select_location"] = "bottom_left"
            active_board_dict["top_left"] = active_board_dict["top_left"].replace("_select", "")
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"][:-1] + "_select:"

        elif state["select_location"] == "top_mid":
            state["select_location"] = "bottom_mid"
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"
            
        elif state["select_location"] == "top_right":
            state["select_location"] = "bottom_right"
            active_board_dict["top_right"] = active_board_dict["top_right"].replace("_select", "")
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"][:-1] + "_select:"

        elif state["select_location"] == "mid_left":
            state["select_location"] = "top_left"
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["top_left"] = active_board_dict["top_left"][:-1] + "_select:"

        elif state["select_location"] == "mid_mid":
            state["select_location"] = "top_mid"
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "mid_right":
            state["select_location"] = "top_right"
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["top_right"] = active_board_dict["top_right"][:-1] + "_select:"

        elif state["select_location"] == "bottom_left":
            state["select_location"] = "mid_left"
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"].replace("_select", "")
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "bottom_mid":
            state["select_location"] = "mid_mid"
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"
        
        elif state["select_location"] == "bottom_right":
            state["select_location"] = "mid_right"
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"].replace("_select", "")
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

    # move down function     
    def move_down():
        if state["select_location"] == "homepl":
            state["select_location"] = "homeai"
            for board_pos in home_player_square:
                initial_board_dict[board_pos] = initial_board_dict[board_pos].replace("pl", "")
            for board_pos in home_ai_square:
                initial_board_dict[board_pos] = home_ai_square[board_pos]
            
        elif state["select_location"] == "homeai":
            state["select_location"] = "homepl"
            for board_pos in home_ai_square:
                initial_board_dict[board_pos] = initial_board_dict[board_pos].replace("ai", "")
            for board_pos in home_player_square:
                initial_board_dict[board_pos] = home_player_square[board_pos]

        elif state["select_location"] == "top_left":
            state["select_location"] = "mid_left"
            active_board_dict["top_left"] = active_board_dict["top_left"].replace("_select", "")
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "top_mid":
            state["select_location"] = "mid_mid"
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "top_right":
            state["select_location"] = "mid_right"
            active_board_dict["top_right"] = active_board_dict["top_right"].replace("_select", "")
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"        

        elif state["select_location"] == "mid_left":
            state["select_location"] = "bottom_left"
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"][:-1] + "_select:"

        elif state["select_location"] == "mid_mid":
            state["select_location"] = "bottom_mid"
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "mid_right":
            state["select_location"] = "bottom_right"
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"][:-1] + "_select:"        

        elif state["select_location"] == "bottom_left":
            state["select_location"] = "top_left"
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"].replace("_select", "")
            active_board_dict["top_left"] = active_board_dict["top_left"][:-1] + "_select:"

        elif state["select_location"] == "bottom_mid":
            state["select_location"] = "top_mid"
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "bottom_right":
            state["select_location"] = "top_right"
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"].replace("_select", "")
            active_board_dict["top_right"] = active_board_dict["top_right"][:-1] + "_select:"        

    # move right function 
    def move_right():
        if state["select_location"] == "top_left":
            state["select_location"] = "top_mid"
            active_board_dict["top_left"] = active_board_dict["top_left"].replace("_select", "")
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "top_mid":
            state["select_location"] = "top_right"
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["top_right"] = active_board_dict["top_right"][:-1] + "_select:"

        elif state["select_location"] == "top_right":
            state["select_location"] = "top_left"
            active_board_dict["top_right"] = active_board_dict["top_right"].replace("_select", "")
            active_board_dict["top_left"] = active_board_dict["top_left"][:-1] + "_select:"

        elif state["select_location"] == "mid_left":
            state["select_location"] = "mid_mid"
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "mid_mid":
            state["select_location"] = "mid_right"
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "mid_right":
            state["select_location"] = "mid_left"
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "bottom_left":
            state["select_location"] = "bottom_mid"
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"].replace("_select", "")
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "bottom_mid":
            state["select_location"] = "bottom_right"
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"][:-1] + "_select:"

        elif state["select_location"] == "bottom_right":
            state["select_location"] = "bottom_left"
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"].replace("_select", "")
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"][:-1] + "_select:"
        

    # move left function
    def move_left():
        if state["select_location"] == "top_left":
            state["select_location"] = "top_right"
            active_board_dict["top_left"] = active_board_dict["top_left"].replace("_select", "")
            active_board_dict["top_right"] = active_board_dict["top_right"][:-1] + "_select:"

        elif state["select_location"] == "top_mid":
            state["select_location"] = "top_left"
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["top_left"] = active_board_dict["top_left"][:-1] + "_select:"

        elif state["select_location"] == "top_right":
            state["select_location"] = "top_mid"
            active_board_dict["top_right"] = active_board_dict["top_right"].replace("_select", "")
            for board_pos in top_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"        

        elif state["select_location"] == "mid_left":
            state["select_location"] = "mid_right"
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "mid_mid":
            state["select_location"] = "mid_left"
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_left_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"
        
        elif state["select_location"] == "mid_right":
            state["select_location"] = "mid_mid"
            for board_pos in mid_right_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            for board_pos in mid_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"

        elif state["select_location"] == "bottom_left":
            state["select_location"] = "bottom_right"
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"].replace("_select", "")
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"][:-1] + "_select:"

        elif state["select_location"] == "bottom_mid":
            state["select_location"] = "bottom_left"
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos].replace("_select", "")
            active_board_dict["bottom_left"] = active_board_dict["bottom_left"][:-1] + "_select:"

        elif state["select_location"] == "bottom_right":
            state["select_location"] = "bottom_mid"
            active_board_dict["bottom_right"] = active_board_dict["bottom_right"].replace("_select", "")
            for board_pos in bottom_mid_square:
                active_board_dict[board_pos] = active_board_dict[board_pos][:-1] + "_select:"            

    # function to handle home selection logic
    async def home_select_logic():
        if state["select_location"] == "homepl":
            await play_against_player()
        elif state["select_location"] == "homeai":
            await play_against_ai()

    # function to switch turns
    async def switch_turns(current_player, player1, player2):
            if current_player == player1:
                await message.remove_reaction(emoji_dict[":select_x:"], interaction.user)
                await message.remove_reaction(emoji_dict[":select_x:"], interaction.client.user)
                await message.add_reaction(emoji_dict[":select_o:"])
                return player2
            else:
                await message.remove_reaction(emoji_dict[":select_o:"], interaction.user)
                await message.remove_reaction(emoji_dict[":select_o:"], interaction.client.user)
                await message.add_reaction(emoji_dict[":select_x:"])
                return player1  

    # function to handle game selection logic
    async def game_select_logic(current_player, player1):
        if active_board_dict[state["select_location"]].endswith("_empty_select:"):
            print("tried to select empty square")
            if current_player == player1:
                x_or_o = "x"
            else:
                x_or_o = "o"
            
            if state["select_location"] == "top_left" or state["select_location"] == "top_right" or state["select_location"] == "bottom_left" or state["select_location"] == "bottom_right":
                active_board_dict[state["select_location"]] = active_board_dict[state["select_location"]].replace("empty", x_or_o)
            elif state["select_location"] == "top_mid":
                for board_pos in top_mid_square:
                    active_board_dict[board_pos] = active_board_dict[board_pos].replace("empty", x_or_o)
            elif state["select_location"] == "mid_left":
                for board_pos in mid_left_square:
                    active_board_dict[board_pos] = active_board_dict[board_pos].replace("empty", x_or_o)
            elif state["select_location"] == "mid_mid":
                for board_pos in mid_mid_square:
                    active_board_dict[board_pos] = active_board_dict[board_pos].replace("empty", x_or_o)
            elif state["select_location"] == "mid_right":
                for board_pos in mid_right_square:
                    active_board_dict[board_pos] = active_board_dict[board_pos].replace("empty", x_or_o)
            elif state["select_location"] == "bottom_mid":
                for board_pos in bottom_mid_square:
                    active_board_dict[board_pos] = active_board_dict[board_pos].replace("empty", x_or_o)        
            win_condition_board[state["select_location"]] = x_or_o
            return True
                
            
        else:
            await interaction.followup.send(f"{current_player.mention}, This square is already occupied! Please select another square.", ephemeral=False)
            return False

    
    # makes the user select a player and play against them xo
    async def play_against_player():
        await interaction.followup.send("Please mention the user you want to play with (e.g. @username). ", ephemeral=False)
        msg = await interaction.client.wait_for('message', check=lambda m: m.author == interaction.user and m.channel == interaction.channel)
        if not msg.mentions:
            await interaction.followup.send("You must mention a user to play with!", ephemeral=False)
            return
        player1 = interaction.user
        if player1 == msg.mentions[0]:
            await interaction.followup.send("You cannot play against yourself you silly goose!", ephemeral=False)
            return
        if client.user == msg.mentions[0]:
            await interaction.followup.send("Choose ai next time ya bot!", ephemeral=False)
            return
        player2 = msg.mentions[0]

        current_player = player1
        board = active_update_board(active_board_dict)
        await message.edit(content=board)
        state["select_location"] = "mid_mid"
        
        # Add reactions for movement and selection
        reactions = [':green_arrow_left:', ':green_arrow_up:', ':green_arrow_down:', ':green_arrow_right:', ":select_x:"]
        reactions_ids = [emoji_dict[reaction] for reaction in reactions]
        for reaction in reactions_ids:
            await message.add_reaction(reaction)

        # reaction handler
        def check(reaction, user):
            return user == current_player and str(reaction.emoji) in reactions_ids
        
        while True:

            try:
                reaction, user = await interaction.client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                break

            else:
                if str(reaction.emoji) == emoji_dict[':green_arrow_up:']:
                    move_up()
                
                elif str(reaction.emoji) == emoji_dict[':green_arrow_down:']:
                    move_down()
                
                elif str(reaction.emoji) == emoji_dict[':green_arrow_right:']:
                    move_right()
                
                elif str(reaction.emoji) == emoji_dict[':green_arrow_left:']:
                    move_left()

                elif str(reaction.emoji) == emoji_dict[':select_x:']:
                    if(await game_select_logic(current_player, player1) == True):
                        # check if the game is won or drawn
                        if(check_for_win() == True):
                            await message.clear_reactions()
                            await interaction.followup.send(f"{current_player.mention} is da winner!", ephemeral=False)
                            return

                        if check_for_draw() == True:
                            await message.clear_reactions()
                            await interaction.followup.send("The game is a draw!", ephemeral=False)  
                            return
                        current_player = await switch_turns(current_player, player1, player2)
                        reactions_ids.remove(emoji_dict[':select_x:'])
                        reactions_ids.append(emoji_dict[':select_o:'])


                elif str(reaction.emoji) == emoji_dict[':select_o:']:
                    if(await game_select_logic(current_player, player1) == True):
                        if(check_for_win() == True):
                            await message.clear_reactions()
                            await interaction.followup.send(f"{current_player.mention} is da winner!", ephemeral=False)
                            return

                        if check_for_draw() == True:
                            await message.clear_reactions()
                            await interaction.followup.send("The game is a draw!", ephemeral=False)  
                            return
                        current_player = await switch_turns(current_player, player1, player2)
                        reactions_ids.remove(emoji_dict[':select_o:'])
                        reactions_ids.append(emoji_dict[':select_x:'])  
                
                # Update the board and remove the reaction
                board = active_update_board(active_board_dict)
                await message.edit(content=board)
                await message.remove_reaction(reaction, user)

    # Function to handle playing against an AI
    def play_against_ai():
        ...

    # add reactions for home selection screen(game mode selection screen)
    home_reactions = {":green_arrow_up:", ":green_arrow_down:", ":select_empty:"}
    home_reactions_ids = [emoji_dict[reaction] for reaction in home_reactions]
    for reaction in home_reactions_ids:
        await message.add_reaction(reaction)

    # reaction handler
    def home_check(reaction, user):
        return user == interaction.user and str(reaction.emoji) in home_reactions_ids

    while True:
        try:
            reaction, user = await interaction.client.wait_for('reaction_add', timeout=60.0, check=home_check)
        except asyncio.TimeoutError:
            break

        else:
            if str(reaction.emoji) == emoji_dict[":green_arrow_up:"]:
                move_up()
            
            elif str(reaction.emoji) == emoji_dict[":green_arrow_down:"]:
                move_down()
            
            elif str(reaction.emoji) == emoji_dict[":select_empty:"]:
                for reaction in home_reactions_ids:
                    await message.remove_reaction(reaction, interaction.client.user)
                    await message.remove_reaction(reaction, interaction.user)
                await home_select_logic()
                break

         # Update the board and remove the reaction
            board = active_update_board(initial_board_dict)
            await message.edit(content=board)
            await message.remove_reaction(reaction, user)

