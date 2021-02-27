import discord
from discord.ext import commands
import random
import json
from core.classes import Cog_Extension
import urllib.parse, urllib.request, re

with open('正版.json', 'r', encoding='utf8') as botfild:
   data = json.load(botfild)

class Main(Cog_Extension):

  @commands.command()
  async def 延遲(self, ctx):
    await ctx.send(f'{round(self.bot.latency*1000)} ms')
  
  @commands.command()
  async def 占卜(self, ctx, *占卜內容):
    random_ctx_lucky = random.choice(data['lucky'])
    await ctx.send(f'{占卜內容}的結果：**||{random_ctx_lucky}||**')

  @commands.command()
  async def 頻道(self, ctx, *結果):
    query_string = urllib.parse.urlencode({'search_query': 結果})
    url = urllib.request.urlopen('https://www.youtube.com/results?' + query_string + '&sp=EgIQAg%253D%253D')
    search_results = re.findall(r'/channel(.{50})', url.read().decode())
    await ctx.send('頻道在這裡~，可能會查不到~' + 'https://www.youtube.com/channel' + search_results[1])
  
  @commands.command()
  async def 抽獎(self, ctx, 獎品, 人數, 時間):
    embed=discord.Embed(title="抽獎囉！！", url="https://www.youtube.com/channel/UCLhOduQMWBTnaEPUv7FTiow", description="按下底下表情符號吧！！！", color=0xff0000)
    embed.set_author(name="正版人人人-bot", icon_url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.add_field(name="獎品", value=f"{獎品}", inline=False)
    embed.add_field(name="人數", value=f"{人數}人", inline=False)
    embed.add_field(name="剩餘時間", value=f"在{時間}時開抽！！", inline=False)
    embed.add_field(name="------------------------------", value="||分隔線||", inline=False)
    embed.set_footer(text="製作人：正版人人人#8958")
    print(f'{獎品}, {人數}, {時間}')
    await ctx.message.delete()
    message = await ctx.send(embed=embed)
    await message.add_reaction('✅')
  
  @commands.has_permissions(administrator=True)
  @commands.command()
  async def 刪除訊息(self, ctx, 數量:int):
    await ctx.channel.purge(limit=數量+1)

def setup(bot):
  bot.add_cog(Main(bot))
