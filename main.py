import keep_alive
import discord
import requests
import json
# from data_save import savetocsv
from discord.ext import commands
# import os
# import dotenv
# from dotenv import load_dotenv

# load_dotenv(os.path.join(os.getcwd(), '.env'))
stop = False
badlist = []
sent_message = ""
special_badwords = ["eek", "kentut"]
badwords = [
    "anjing", "anjng", "ajg", "anjig", "anying", "anjir", "jir", "jing",
    "jink", "jinks", "nying", "njir", "bjir", "babi", "monyet", "nyet", "asu",
    "asw", "tai", "tae", "tahi", "tolol, "
    "tolil", "idiot", "goblok", "gblg", "gblk", "gblok"
    "gebleg", "geblek", "gbleg", "brengsek", "berengsek", "laknat", "lucknut",
    "bego", "bgo", "najis"
    "tai", "eek", "kentut", "bangsat", "bgst", "bngst", "kampret", "kmpret",
    "bangke", "bngke", "bajingan", "jingan", "bajing", "bjing", "bjingan",
    "bjngn", "ngentot", "ngntot", "jancok", "jancuk", "jncok", "jncuk",
    "kontol", "kntl", "kintil", "kontil", "kntil", "ngontol", "mmk", "memek",
    "tytyd", "titit", "titid", "ass", "arse", "ashole", "bastard", "shit",
    "shite", "stfu", "fuck", "fck", "fucking", "fcking", "tf", "wtf",
    "motherfucker", "mtrfckr", "mtrfucker", "motherfckr", "bitch", "btch",
    "bitcj", "dick", "autis", "autist", "autism", "hell", "bloody"
]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  response_json = json.loads(response.text)
  quote = response_json[0]['q'] + " (" + response_json[0]['a'] + ")"
  return quote


# Python3 program to Split string into characters
def split(word):
  return [char for char in word]


########## this is where the program starts ##########
client = discord.Client()
'''class CustomHelpCommand(commands.HelpCommand):
  def __init__(self):
    super().__init__()

  async def send_bot_help(self, mapping):
    return await super().send_bot_help(mapping)
    
  async def send_cog_help(self, cog):
    return await super().send_cog_help(cog)
    
  async def send_group_help(self, group):
    return await super().send_group_help(group)
    
  async def send_command_help(self, command):
    return await super().send_command_help(command)


bot = commmands.Bot(command_prefix='.', help_command=CustomizeHelpCommand())'''


@client.event
async def on_ready():
  print("{0.user} has logged in".format(client))

  ##help command


client = commands.Bot(command_prefix="$")
# client.remove_command('help')

# @client.command(pass_context=True)
# async def help(ctx):
#   channel = ctx.message.channel
#   embed = discord.Embed()

#   embed.set_author(name='Help')
#   embed.add_field(name='generate random wise quote', value='blablabla', inline=False)
#   await client.send_message(channel, embed=embed)


@client.event
async def on_message(message):
  msg = message.content

  if message.author == client.user:
    return
  if msg.startswith('$start'):
    await message.channel.send(
        'Hello! My name is ' + str(client.user) +
        ', I am watching for badwords that u spoke, careful :)')
  if msg.startswith('$wise'):
    quote = get_quote()
    await message.channel.send(quote)
  if msg.startswith('$stop'):
    stop = True
    await message.channel.send("bot stopped")
  if msg.startswith('$start'):
    stop = False
    await message.channel.send("bot started")

  ## Split sentence
  sent_message = msg.lower()
  print(sent_message)
  sent_message_split = sent_message.split(" ")
  print(sent_message_split)
  sent_message_split_length = len(sent_message_split)
  print(sent_message_split_length)

  ## Remove multiple character in a word
  for index in range(0, sent_message_split_length):  ## jumlah katanya
    containerindex = 0
    splitindexcounter = 1

    sent_message_split_char = split(str(sent_message_split[index]))
    print(sent_message_split_char)

    split_index = len(sent_message_split_char)
    print(split_index)

    container = sent_message_split_char[containerindex]
    for splitindex in range(1, split_index):
      try:
        if sent_message_split_char[splitindexcounter] == container:
          sent_message_split_char.pop(splitindexcounter)
          splitindexcounter = splitindexcounter - 1
          containerindex = containerindex - 1
          print("popped")
        else:
          print("pass")
          pass
        containerindex += 1
        splitindexcounter += 1

        container = sent_message_split_char[containerindex]

      except:
        print("except")
        pass
    split_message = ''.join(sent_message_split_char)
    split_message = str(split_message)
    print("MSG: " + split_message)
    '''if sent_message_split in special_badwords: 
        print("BADWORD SPECIAL")
        message_author = message.author.mention
        await message.channel.send("HOY!! Badword! " + message_author)
      else:
        print("BADWORD SPECIAL NOT DETECTED")
        pass'''

    # testing
    badword_record = {}
    if stop == False:
      if split_message in badwords:
        print("BADWORD")
        message_author = message.author.mention
        await message.channel.send("HOY!! Badword! " + message_author)
        # if message_author in badword_record:
        #     print("if")
        #     # badword_record = badword_record.update({message_author: +1})
        #     badword_record[message_author] = badword_record.get(message_author, 0) + 3
        # else:
        #     print("else")
        #     # badword_record = {message_author: 1}
        #     badword_record[message_author] = badword_record.get(
        #         message_author, 0) + 3
        # print(badword_record)
        # await message.chanel.send(badword_record.get(message_author))
        # # db = savetocsv(message_author)

        # # member = message.author
        # # var = discord.utils.get(message.guild.roles, name = "muted")
        # # member.add_role(var)

        # # message.author.append(badlist)
      else:
        print("NO BADWORD")
        pass

  ### di split, klu ada huruf yg consecutively == badwords: warning *
  ### bikin $help (command list) ##DO THIS FOR THE NEXT UPDATE
  ## beri role muted kepada orang yang ngomong kasar 5 kali
  ### add DB
  ## tambahin hitung berapa kata kasar yang dikatakan per user
  ## bikin summary dari total kata kasar per orang dalam seminggu/sebulan/semenit
  ## beri warning *


keep_alive.keep_alive()
# token = os.getenv("SECRETTOKEN")
# client.run(token)
token = 'ODQxNjY2NDE1Nzg1OTM0ODU4.YJqE7g.KHkTFMSxgZaAXyct7MjClVL8ea4'
client.run(token)
