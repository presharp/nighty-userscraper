# Documentation can be found at https://nighty.one/docs/#customscripts #

import asyncio

@bot.command(usage='flyscr <argument>', description='Scrapes all the members of a server using a selfbot')
async def flyscr(nighty):
    msg = nighty.message;
    await msg.delete()
    fileName = "scraped-ids-" + str(msg.guild.id) +".txt"
    f = open(fileName, "w", encoding="utf-8")
    f.write("Server: " + msg.guild.name + ", Member Count: " + str(len(nighty.message.guild.members)) + "\n")
    for m in nighty.message.guild.members:
        f.write(str(m.id) + "\n")
    f.close()
    print("Done. Check " + fileName)