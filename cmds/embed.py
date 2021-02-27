import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):

  @commands.command()
  async def 選單(self, ctx):
    embed=discord.Embed(title="我的頻道", url="https://www.youtube.com/channel/UCLhOduQMWBTnaEPUv7FTiow", description="今天起開始訂閱吧!!", color=0x00ff00)
    embed.set_author(name="正版人人人-bot", icon_url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.add_field(name="文字", value="輸入後可查看文字選單", inline=False)
    embed.add_field(name="指令", value="輸入後可查看指令選單", inline=False)
    embed.add_field(name="遊戲", value="輸入後可查看遊戲選單", inline=False)
    embed.add_field(name="------------------------------", value="||分隔線||", inline=False)
    embed.add_field(name="所有指令一律加上`指令！`", value="要記得歐!!", inline=False)
    embed.set_footer(text="製作人：正版人人人#8958")
    await ctx.send(embed=embed)

  @commands.command()
  async def 文字(self, ctx):
    embed=discord.Embed(title="文字選單", url="https://www.youtube.com/channel/UCLhOduQMWBTnaEPUv7FTiow", description="輸入文字即可觸發", color=0x00ff00)
    embed.set_author(name="正版人人人-bot", icon_url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.add_field(name="早上說早安", value="只要在隨便一個頻道輸入`早安`，機器人就會回你`早安~~祝你有個美好的一天~`歐！！", inline=False)
    embed.add_field(name="中午說午安", value="只要在隨便一個頻道輸入`午安`，機器人就會回你`午安~~甲飽末?`", inline=False)
    embed.add_field(name="晚上說晚安", value="只要在隨便一個頻道輸入`晚安`，機器人就會回你`晚安~~祝你有個好夢！！`歐！！", inline=False)
    embed.add_field(name="打個招呼吧",value="只要在隨便一個頻道輸入`hihi`，機器人就會回你`你好呀!`歐！！",inline=False)
    embed.add_field(name="------------------------------", value="||分隔線||", inline=False)
    embed.add_field(name="此區指令不須加上`指令！`", value="直接打就好了!!", inline=False)
    embed.set_footer(text="製作人：正版人人人#8958")
    await ctx.send(embed=embed)

  @commands.command()
  async def 指令(self, ctx):
    embed=discord.Embed(title="指令選單", url="https://www.youtube.com/channel/UCLhOduQMWBTnaEPUv7FTiow", description="所有指令", color=0x00ff00)
    embed.set_author(name="正版人人人-bot", icon_url="https://i.imgur.com/srUnOPV.png")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.add_field(name="選單", value="輸入後可查看機器人選單", inline=False)
    embed.add_field(name="延遲", value="輸入後可查看機器人延遲(單位為毫秒)", inline=False)
    embed.add_field(name="頻道", value="輸入後可查詢YT頻道(有些人可能查不到)", inline=False)
    embed.add_field(name="------------------------------", value="||分隔線||", inline=False)
    embed.add_field(name="所有指令一律加上`指令！`", value="要記得歐!!", inline=False)
    embed.set_footer(text="製作人：正版人人人#8958")
    await ctx.send(embed=embed)

  @commands.command()
  async def 遊戲(self, ctx):
    embed=discord.Embed(title="我的頻道", url="https://www.youtube.com/channel/UCLhOduQMWBTnaEPUv7FTiow", description="所有遊戲", color=0x00ff00)
    embed.set_author(name="正版人人人-bot", icon_url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/a-/AOh14GirH9ZIhJ8I_Qy9On0HciggtIpehx7MRXJUWe6d=s600-k-no-rp-mo")
    embed.add_field(name="比大小", value="輸入後隨機獲得`1~50`內其中一個數，可與朋友比數字大小", inline=False)
    embed.add_field(name="占卜 (你要占卜的東西)", value="輸入後隨機獲得`大吉、中吉、小吉、末吉、吉、凶、大凶`其中一個評價(結果僅供參考，不要去買大樂透)", inline=False)
    embed.add_field(name="------------------------------", value="||分隔線||", inline=False)
    embed.add_field(name="所有指令一律加上`指令！`", value="要記得歐!!", inline=False)
    embed.set_footer(text="製作人：正版人人人#8958")
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(React(bot))
