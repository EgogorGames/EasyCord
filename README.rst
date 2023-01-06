EasyCord | esycord
====================

.. image:: https://img.shields.io/pypi/dd/esycord.svg
   :target: https://pypi.python.org/pypi/esycord
   :alt: PyPI downloads
.. image:: https://shields.io/pypi/v/esycord.svg
   :target: https://pypi.python.org/pypi/esycord
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/esycord.svg
   :target: https://pypi.python.org/pypi/esycord
   :alt: PyPI supported Python versions

EasyCord - Python module for much easier creating discord bots on python!

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U esycord

    # Windows
    py -3 -m pip install -U esycord


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/EgogorGames/EasyCord
    $ cd esycord

Bot Example
--------------

.. code:: py

   import esycord as es
   from discord import *

   client = es.client(command_prefix="!", intents=Intents.all())
   tree = client.get_tree()

   @client.default_command(name="reply")
   async def reply(esyraction:es.Esyraction):
       await esyraction.reply("hello")

   @client.on_msg()
   async def on_msg(message:Message):
       print(message.content)

   @tree.command(name="help", description="Help menu")
   async def help(interaction : Interaction):
       await interaction.response.send_message("Help menu.\n- `!reply` - Replyes with hello message!")

   client.bot_run("TOKEN")

More examples you can find in `Examples directory <https://github.com/EgogorGames/EasyCord/tree/main/examples/>`_

Links
------

- `Discord <https://discord.com/>`_
- `Discord Developer Portal <https://discord.com/developers/>`_
- `Discord.py Documentation <https://discordpy.readthedocs.io/en/latest/index.html>`_
- `EasyCord(esycord) Documentation`
