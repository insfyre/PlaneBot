from discord.ext import commands
import os
import random
import csv
bot = commands.Bot(command_prefix='!')

bot.planeList = []

#CSV reading code modified from https://www.geeksforgeeks.org/reading-rows-from-a-csv-file-in-python/
with open('planeDatabase.csv') as file_obj:
      
    # Create reader object by passing the file object to reader method
    reader_obj = csv.DictReader(file_obj)
      
    # Iterate over each row in the csv file using reader object
    # Objective is to create list of dictionaries
    for row in reader_obj:
        bot.planeList.append(row)

#outputs randomly chosen make, model, and Wikipedia article of a plane
@bot.command()
async def plane(ctx):
  p=random.choice(bot.planeList)
  #print('{Make} {Model} {Wikipedia}'.format(**p))
  await ctx.send('{Make} {Model} {Wikipedia}'.format(**p))

password = os.environ['password']
bot.run(password)