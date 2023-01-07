"""
EasyCord
~~~~~~~~~~~~~~~~~~~
This is cool Python Module for much easier coding DiscordBots

Info:
~~~~~~~~~~~~~~~~~~~
Developer: EgogorGames(#3733)
    .. versionadded:: 1
GitHub Repo: https://github.com/EgogorGames/EasyCord/

©EgogorGames 2022 - 2023 | Not official Discord Module!
"""

#################################
#                               #
#       E a s y C o r d         #
#                               #
#   ©EgogorGames 2022 - 2023    #
#                               #
#################################

# Discord modules import

from discord import *
from discord.ui import *
from discord.utils import *
from discord.ext import *
from discord_webhook import *

# Another modules import

from random import choice
from datetime import datetime
from inspect import signature

# Some variables

letters_and_numbers_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','8','9','0']
letters_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_str = ['1','2','3','4','5','6','7','8','9','0']
commands_w0 = []
commands_w1 = []
commands_w2 = []
commands_w3 = []
commands_w4 = []
commands_w5 = []
on_msg_func = None

# Terminal colors

P = '\033[95m'
C = '\033[96m'
DC = '\033[36m'
B = '\033[94m'
G = '\033[92m'
LG = '\033[30m'
Y = '\033[93m'
R = '\033[91m'
BOLD = '\033[1m'
UND = '\033[4m'
END = '\033[0m'

# Objects

class DefaultCommand():
    r"""
    Command object what maked special for saving command data!

    Parameters:
    -----------

    name: :class:`str` Command name.
    function_def: :class:`str` Function with command script.
    guild: :class:`Guild` Command guild.
    """
    def __init__(self, name : str, function_def : any, guild : Guild, aliases : list[str]) -> None:
        self.name = name
        self.funcd = function_def
        self.guild = guild
        self.aliases = aliases

class Esyraction():
    r"""
    Something like Interaction object what created special for default commands!
    
    Parameters:
    -----------

    message: :class:`Message` message for taking info.

    Methods:
    -----------

    :meth:`reply` - Replies to command message!
    :meth:`send` - Sends message to same chat with command message!
    """
    def __init__(self, message : Message) -> None:
        self.message = message
        self.user = message.author
        self.channel = message.channel
        self.guild = message.guild
        msg_content = message.content.split()[0]
        command = msg_content[0]
        command_np = command[1:]
        self.command = command_np
    
    async def reply(self, content : str = None, **kgwars : any) -> Message:
        """
        Replies to command message!

        Parameters:
        -----------
        content (Optional[:class:`str`])
             .. versionadded:: 1   
        tts (:class:`bool`) 
             .. versionadded:: 1   
        embed (:class:`Embed`) 
             .. versionadded:: 1   
        embeds (List[:class:`Embed`]) 
             .. versionadded:: 1   
        file (:class:`File`)
             .. versionadded:: 1   
        files (List[:class:`File`])
             .. versionadded:: 1   
        nonce (:class:`int`)
             .. versionadded:: 1   
        delete_after (:class:`float`)
             .. versionadded:: 1   
        allowed_mentions (:class:`AllowedMentions`)
             .. versionadded:: 1   
        reference (:class:`Union[Message, MessageReference, PartialMessage]`)
             .. versionadded:: 1   
        mention_author (Optional[:class:`bool`]) 
             .. versionadded:: 1   
        view (:class:`View`)
             .. versionadded:: 1   
        stickers (:class:`Sequence[Union[GuildSticker, StickerItem]]`) 
             .. versionadded:: 1   
        suppress_embeds (:class:`bool`)

        Returns:
        -----------
        :class:`Message` - Message what sended!
        """
        msg = await self.message.reply(content=content, **kgwars)
        return msg
    async def send(self, content : str = None, **kgwars : any) -> Message:
        """
        Sends message to same chat with command message!

        Parameters:
        -----------
        content (Optional[:class:`str`])
             .. versionadded:: 1   
        tts (:class:`bool`) 
             .. versionadded:: 1   
        embed (:class:`Embed`) 
             .. versionadded:: 1   
        embeds (List[:class:`Embed`]) 
             .. versionadded:: 1   
        file (:class:`File`)
             .. versionadded:: 1   
        files (List[:class:`File`])
             .. versionadded:: 1   
        nonce (:class:`int`)
             .. versionadded:: 1   
        delete_after (:class:`float`)
             .. versionadded:: 1   
        allowed_mentions (:class:`AllowedMentions`)
             .. versionadded:: 1   
        reference (:class:`Union[Message, MessageReference, PartialMessage]`)
             .. versionadded:: 1   
        mention_author (Optional[:class:`bool`]) 
             .. versionadded:: 1   
        view (:class:`View`)
             .. versionadded:: 1   
        stickers (:class:`Sequence[Union[GuildSticker, StickerItem]]`) 
             .. versionadded:: 1   
        suppress_embeds (:class:`bool`)

        Returns:
        -----------
        :class:`Message` - Message what sended!
        """
        msg = await self.channel.send(content=content, **kgwars)
        return msg
    async def delete(self, delay : float = None):
        """
        Deletes original message!

        Parameters:
        -----------

        delay: :class:`float` Delete delay.
        """
        await self.message.delete(delay=delay)

class client(Client):
    r"""
    This is the client!
    
    Methods:
    -----------
    :meth:`crun` - Runs client(Connecting bot to discord)!
         .. versionadded:: 1   
    :meth:`get_tree` - Returns :class:`app_commands.CommandTree` !
    """
    def __init__(self, intents : Intents = Intents.all(), command_prefix : str = "!", delete_command_message : bool = False) -> None:
        super().__init__(intents=intents)
        self.synced = False
        self.prefix = command_prefix
        self.del_cmd_msg = delete_command_message
        global ctree
        ctree = app_commands.CommandTree(self)
    def set_prefix(self, prefix : str = "!") -> str:
        """
        Changes prefix to another

        Parameters:
        -----------

        prefix: :class:`str` New prefix.
        """
        self.prefix = prefix
        return self.prefix
    async def playing(self, name: str, status : Status = Status.online) -> None:
        """
        Changes status to playing.

        Parameters:
        -----------

        name: :class:`str` Status name.
        status: Optional(:class:`Status`) Bot status.
        """
        await self.change_presence(activity=Game(name=name), status=status)
    async def watching(self, name: str, status : Status = Status.online) -> None:
        """
        Changes status to watching.

        Parameters:
        -----------

        name: :class:`str` Status name.
        status: Optional(:class:`Status`) Bot status.
        """
        await self.change_presence(activity=Activity(type=ActivityType.watching, name=name), status=status)
    async def listening(self, name: str, status : Status = Status.online) -> None:
        """
        Changes status to listening.

        Parameters:
        -----------

        name: :class:`str` Status name.
        status: Optional(:class:`Status`) Bot status.
        """
        await self.change_presence(activity=Activity(type=ActivityType.listening, name=name), status=status)
    async def streaming(self, name: str, url : str = "https://twich.tv/unknown/") -> None:
        """
        Changes status to streaming.

        Parameters:
        -----------

        name: :class:`str` Status name.
        url: Optional(:class:`str`) Stream twich url.
        """
        await self.change_presence(activity=Streaming(name=name, url=url))
    async def custom_status(self, name: str, status : Status = Status.online, emoji : str = None) -> None:
        """
        Changes status to custom.

        Parameters:
        -----------

        name: :class:`str` Status name.
        status: Optional(:class:`Status`) Bot status.
        emoji: Optional(:class:`str`) Custom status emoji.
        """
        await self.change_presence(activity=Activity(type=ActivityType.custom, name=name, emoji=emoji), status=status)
    def default_command(self, name : str, aliases : list[str] = [], guild : Guild = None):
        """
        A decorator that creates default command from a regular function.

        Parameters:
        -----------

        name: :class:`str` Command name.
        guild: Optional(:class:`Guild`) Command guild.
        """
        def decorator(func):
            func_args = str(signature(func))
            func_args_lst = func_args[1:len(func_args) - 1].split()
            func_arg_len = 0
            for farg in func_args_lst:
                if farg[int(len(farg) - 1)] == ":":
                    pass
                else:
                    func_arg_len = func_arg_len + 1
            func_arg_len = func_arg_len - 1
            cmd = DefaultCommand(name, func, guild, aliases)
            if func_arg_len == 0:
                commands_w0.append(cmd)
            elif func_arg_len == 1:
                commands_w1.append(cmd)
            elif func_arg_len == 2:
                commands_w2.append(cmd)
            elif func_arg_len == 3:
                commands_w3.append(cmd)
            elif func_arg_len == 4:
                commands_w4.append(cmd)
            elif func_arg_len == 5:
                commands_w5.append(cmd)
            else:
                raise Exception(f"In command '{name}' used more than 5 arguments now this unsupported!")
            return func
        return decorator
    def on_msg(self):
        """
        A decorator that creates event on message.
        """
        def decorator(func):
            global on_msg_func
            on_msg_func = func
            return func
        return decorator
    def on_loading(self):
        """
        A decorator that creates event on loading.
        """
        def decorator(func):
            global on_loading_func
            on_loading_func = func
            return func
        return decorator
    def on_login(self):
        """
        A decorator that creates event on login.
        """
        def decorator(func):
            global on_login_func
            on_login_func = func
            return func
        return decorator
    def bot_run(self, token : str) -> None:
        """
        This method runs :class:`client`!
        
        Parameters:
        -----------
        
        token: :class:`str` Bot token.
        """
        dev.log(f"Client and Module runned", "log", "LOG")
        self.run(token)
    async def on_message(self, message:Message):
        
        if message.content != "":
            #commands

            msg_content = message.content.split()
            command = msg_content[0]
            msg_command_prefix = command[0]

            if msg_command_prefix == self.prefix:
                command_np = command[1:]
                HAS_PERMS = True

                """commands_wALL = []
                commands_wALL.extend(commands_w0)
                commands_wALL.extend(commands_w1)
                commands_wALL.extend(commands_w2)
                commands_wALL.extend(commands_w3)
                commands_wALL.extend(commands_w4)
                commands_wALL.extend(commands_w5)
                print(commands_wALL)
                for cmd_wa in commands_wALL:
                    if command_np == cmd_wa.name:
                        if cmd_wa.permissions != []:
                            HAS_PERMS = False
                            for perm in cmd_wa.permissions:
                                if perm == message.author.guild_permissions:
                                    HAS_PERMS = True
                    else:
                        for alias in cmd_wa.aliases:
                            if command_np == alias:
                                if cmd_wa.permissions != []:
                                    HAS_PERMS = False
                                    for perm in cmd_wa.permissions:
                                        if perm == message.author.guild_permissions:
                                            HAS_PERMS = True"""


                if HAS_PERMS == True:
                    arg_count = len(msg_content) - 1
                    #commands with no arg

                    for cmd_w0 in commands_w0:
                        if command_np == cmd_w0.name:
                            if cmd_w0.guild == None:
                                await cmd_w0.funcd(Esyraction(message))
                            else:
                                if message.guild == cmd_w0.guild:
                                    await cmd_w0.funcd(Esyraction(message))
                        else:
                            for alias in cmd_w0.aliases:
                                if command_np == alias:
                                    if cmd_w0.guild == None:
                                        await cmd_w0.funcd(Esyraction(message))
                                    else:
                                        if message.guild == cmd_w0.guild:
                                            await cmd_w0.funcd(Esyraction(message))

                    ###
                    if arg_count >= 1:
                        arg1 = calculate.type(msg_content[1]).arg
                        #commands with 1 arg
                        
                        for cmd_w1 in commands_w1:
                            if command_np == cmd_w1.name:
                                if cmd_w1.guild == None:
                                    await cmd_w1.funcd(Esyraction(message), arg1)
                                else:
                                    if message.guild == cmd_w1.guild:
                                        await cmd_w1.funcd(Esyraction(message), arg1)
                            else:
                                for alias in cmd_w1.aliases:
                                    if command_np == alias:
                                        if cmd_w1.guild == None:
                                            await cmd_w1.funcd(Esyraction(message), arg1)
                                        else:
                                            if message.guild == cmd_w1.guild:
                                                await cmd_w1.funcd(Esyraction(message), arg1)

                        ###
                        if arg_count >= 2:
                            arg2 = calculate.type(msg_content[2]).arg
                            #commands with 2 arg
                            
                            for cmd_w2 in commands_w2:
                                if command_np == cmd_w2.name:
                                    if cmd_w2.guild == None:
                                        await cmd_w2.funcd(Esyraction(message), arg1, arg2)
                                    else:
                                        if message.guild == cmd_w2.guild:
                                            await cmd_w2.funcd(Esyraction(message), arg1, arg2)
                                else:
                                    for alias in cmd_w2.aliases:
                                        if command_np == alias:
                                            if cmd_w2.guild == None:
                                                await cmd_w2.funcd(Esyraction(message), arg1, arg2)
                                            else:
                                                if message.guild == cmd_w2.guild:
                                                    await cmd_w2.funcd(Esyraction(message), arg1, arg2)

                            ###
                            if arg_count >= 3:
                                arg3 = calculate.type(msg_content[3]).arg
                                #commands with 3 arg
                                
                                for cmd_w3 in commands_w3:
                                    if command_np == cmd_w3.name:
                                        if cmd_w3.guild == None:
                                            await cmd_w2.funcd(Esyraction(message), arg1, arg2, arg3)
                                        else:
                                            if message.guild == cmd_w3.guild:
                                                await cmd_w3.funcd(Esyraction(message), arg1, arg2, arg3)
                                    else:
                                        for alias in cmd_w3.aliases:
                                            if command_np == alias:
                                                if cmd_w3.guild == None:
                                                    await cmd_w3.funcd(Esyraction(message), arg1, arg2, arg3)
                                                else:
                                                    if message.guild == cmd_w3.guild:
                                                        await cmd_w3.funcd(Esyraction(message), arg1, arg2, arg3)

                                ###
                                if arg_count >= 4:
                                    arg4 = calculate.type(msg_content[4]).arg
                                    #commands with 4 arg
                                    
                                    for cmd_w4 in commands_w4:
                                        if command_np == cmd_w4.name:
                                            if cmd_w4.guild == None:
                                                await cmd_w4.funcd(Esyraction(message), arg1, arg2, arg3, arg4)
                                            else:
                                                if message.guild == cmd_w4.guild:
                                                    await cmd_w4.funcd(Esyraction(message), arg1, arg2, arg3, arg4)
                                        else:
                                            for alias in cmd_w4.aliases:
                                                if command_np == alias:
                                                    if cmd_w4.guild == None:
                                                        await cmd_w4.funcd(Esyraction(message), arg1, arg2, arg3, arg4)
                                                    else:
                                                        if message.guild == cmd_w4.guild:
                                                            await cmd_w4.funcd(Esyraction(message), arg1, arg2, arg3, arg4)

                                    ###
                                    if arg_count >= 5:
                                        arg5 = calculate.type(msg_content[5]).arg
                                        #commands with 5 arg

                                        for cmd_w5 in commands_w5:
                                            if command_np == cmd_w5.name:
                                                if cmd_w5.guild == None:
                                                    await cmd_w5.funcd(Esyraction(message), arg1, arg2, arg3, arg4, arg5)
                                                else:
                                                    if message.guild == cmd_w5.guild:
                                                        await cmd_w5.funcd(Esyraction(message), arg1, arg2, arg3, arg4, arg5)
                                            else:
                                                for alias in cmd_w5.aliases:
                                                    if command_np == alias:
                                                        if cmd_w5.guild == None:
                                                            await cmd_w5.funcd(Esyraction(message), arg1, arg2, arg3, arg4, arg5)
                                                        else:
                                                            if message.guild == cmd_w5.guild:
                                                                await cmd_w5.funcd(Esyraction(message), arg1, arg2, arg3, arg4, arg5)
                else:
                    print("NOPERMS")
                if self.del_cmd_msg == True:
                    try:
                        await message.delete()
                    except NotFound:
                        pass
        # Message event

        if on_msg_func != None:
            await on_msg_func(message)                
                            ###
    async def on_ready(self):
        global ctree

        if on_loading_func != None:
            await on_loading_func()

        await self.wait_until_ready()
        if not self.synced:
            await ctree.sync()
            self.synced = True
            dev.log(f"We have logged in as {self.user}.", "login", "LOGIN")
            if on_login_func != None:
                await on_login_func()


    def get_tree(self):
        """
        Returns :class:`app_commands.CommandTree`!
        
        Returns:
        -----------
        :class:`app_commands.CommandTree` - Command tree for slash commands/context menu!
        """
        global ctree
        return ctree

class Arg():
    r"""
    This is object from `easycord` library.
        .. versionadded:: 1
    This object used for saving Agruments(DiscordObjects)!
    
    Parameters:
    -----------
    arg: :class:`Any` Argument(DiscordObject)!
        .. versionadded:: 1
    type: :class:`str` Type of Argument(DiscordObject)!
    """
    def __init__(self, arg : any, type : str) -> None:
        self.arg = arg
        self.type = type
    
    def __repr__(self) -> str:
        return self.arg

# Code

class create():
    r"""
    Special class for easy creating Discord Objects!

    Methods:
    -----------
    :meth:`view` - Creates view with buttons!
    """
    def view(buttons : list[Button]) -> View:
        """
        Creates :class:`View` with buttons!

        Parameters:
        -----------
        
        buttons: :class:`list[str]` Buttons.
        """
        view = View()
        for btn in buttons:
            view.add_item(btn)
        return view

class dev():
    r"""
    Special class for developers what want more cool developer features!

    Methods:
    -----------
    
    :meth:`log` - Sends log to console!
    """
    def log(log : str, log_tag : str = "log", log_type : str = "LOG") -> None:
        """
        Sends log to console.

        Parameters:
        -----------
        
        log: :class:`str` Log text.
            .. versionadded:: 1
        log_tag: :class:`str` Log type(`easycord.{log_tag}`).
            .. versionadded:: 1
        log_type: :class:`str` Log type.

        Returns:
        -----------
        :class:`View` - View with buttons!
        """
        dtime = str(datetime.now())
        time = dtime[:int(len(dtime) - 7)]
        spaces = "".join(" " for i in range(9 - len(log_type)))
        print(f"{BOLD}{LG}{time} {B}{log_type}{spaces}{END}{P}easycord.{log_tag}{END} {log}")

class calculate():
    r"""
    Special class to calculate smth.
    
    Methods:
    -----------
    
    :meth:`type` - Returns Argument(DiscordObject) from :class:`str`!
    """
    def type(argument: str, guild : Guild = None) -> Arg:
        """
        Returns Argument(DiscordObject) from :class:`str`!
        
        Parameters:
        -----------
        
        argument: :class:`str` String what will be converted to Argument(DiscordObject)!
            .. versionadded:: 1
        guild: :class:`Guild`(Optional) Guild what tied to argumet!
        
        Returns:
        -----------
        
        :class:`Arg` - Argument(DiscordObject) from :class:`str`
        """
        arg = str(argument)
        mention_len = len(arg)
        if arg[0] == '<' and arg[-1] == '>':
            if arg[1] == '@':
                if arg[2] != '&':
                    if guild == None:
                        arg_type = "Member"
                        membr_id = int(arg[2:(mention_len - 1)])
                        membr = get(guild.members, id=membr_id)
                        if membr == None:
                            arg_type = 'User'
                            user_id = int(arg[2:(mention_len - 1)])
                            user = client.get_user(user_id)
                            if user == None:
                                raise NameError("User not founded!")
                            else:
                                return Arg(user, arg_type)
                    else:
                        arg_type = "Member"
                        membr_id = int(arg[2:(mention_len - 1)])
                        membr = get(guild.members, id=membr_id)
                        if user == None:
                            arg_type = 'User'
                            user_id = int(arg[2:(mention_len - 1)])
                            user = client.get_user(user_id)
                            if user == None:
                                raise NameError("User not founded!")
                            else:
                                return Arg(user, arg_type)
                        else:
                            return Arg(user, arg_type)
                else:
                    if guild == None:
                        arg_type = 'Role'
                        role_id = int(arg[3:(mention_len - 1)])
                        role = None
                        for guilde in client.guilds:
                            rolee = get(guilde.roles, id=role_id)
                            if rolee != None:
                                role = rolee
                        if role == None:
                            raise NameError("Role not founded!")
                        else:
                            return Arg(role, arg_type)
                    else:
                        arg_type = 'Role'
                        role_id = int(arg[3:(mention_len - 1)])
                        role = get(guild.roles, id=role_id)
                        if role == None:
                            raise NameError("Role not founded!")
                        else:
                            return Arg(role, arg_type)
            if arg[1] == '#':
                arg_type = 'Channel'
                mention_len = len(arg)
                channel_id = int(arg[2:(mention_len - 1)])
                channel = client.get_channel(channel_id)
                if channel == None:
                    raise NameError("Channel not founded!")
                else:
                    return Arg(channel, arg_type)
        else:
            if arg.lower() != "true" and arg.lower() != "false":
                num_count = 0
                let_count = 0
                for arg_num in arg:
                    for numb in numbers_str:
                        if arg_num == numb:
                            num_count = num_count + 1
                for arg_let in arg:
                    for let in letters_str:
                        if arg_let == let:
                            let_count = let_count + 1
                if let_count == 0:
                    arg_type = 'int'
                    an_arg = int(arg)
                else:
                    arg_type = 'str'
                    an_arg = str(arg)
            else:
                arg_type = "bool"
                if arg.lower() == "true":
                    an_arg = True
                elif arg.lower() == "false":
                    an_arg = False
            return Arg(an_arg, arg_type)