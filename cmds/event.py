import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Event(Cog_Extension):
   
  @commands.Cog.listener()
  async def on_ready(self):
    print(">>成功開啟!<<")
    await self.bot.change_presence(
          activity=discord.Streaming(
              name="指令！選單 • 正在為正版人人人伺服器服務中",
              url="https://www.twitch.tv/raind530"))

  @commands.Cog.listener()
  async def on_member_join(self, member):
    print(f'{member} join')
    joinchannel = self.bot.get_channel(792546658554216518)
    await joinchannel.send(f'{member.mention} 加入了伺服器!')

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.content.endswith('早安'):
      await message.channel.send('早安~~祝你有個美好的一天~')
    if message.content.endswith('午安'):
      await message.channel.send('午安~~甲飽末?')      
    if message.content.endswith('晚安'):
      await message.channel.send('晚安~~祝你有個好夢！！')
    if message.content.startswith('!p'):
      await message.delete()
  
  @commands.Cog.listener()
  async def on_message_delete(self, message):
    print(datetime.datetime.now())
    print("訊息作者：" + str(message.author))
    print("訊息內容：" + str(message.content))
    print("訊息頻道：" + str(message.channel))
    print("訊息公會：" + str(message.guild))

def setup(bot):
  bot.add_cog(Event(bot))
