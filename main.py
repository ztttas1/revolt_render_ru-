import revolt
import requests
import asyncio
import os
import random
import always_on

colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "⬛", "⬜"]


api_url = 'https://revoltbots.org/api/v1/bots/{bot_id}/stats'
api_token = 'DWXU5PU0n3F1TOGYGqjN'

headers = {
    'Authorization': f'Bot {api_token}',
    'Content-Type': 'application/json'
}
def send_server_count(server_count):
    payload = {
        'server_count': server_count
    }
    response = requests.post(headers=headers, json=payload)



class Client(revolt.Client):
  async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        statuses = [f".help | Used in {len(guilds)} servers!", f".r | Used in {len(guilds)} servers!", f".g | Used in {len(guilds)} servers!",f".c | Used in {len(guilds)} servers!"]
        while True:
            for status in statuses:
                await self.edit_status(text=status)
                await asyncio.sleep(10)
  async def on_ready(self):
    print('Run  ルーレットBOT')
    
  async def on_message(self, message: revolt.Message):
    guilds = self.servers
      
    
    if message.content == '.r':
      numbers = [random.randint(0, 9) for _ in range(3)]
      
      # 生成された乱数が全て同じかどうかチェック
      if numbers[0] == numbers[1] == numbers[2]:
          # Revoltのチャンネルに"good"と送信
          await message.channel.send(f"> Good! \n > Generated numbers: {numbers}")
          print(f"{numbers} - YES")
      else:
          # 乱数が異なる場合は、その乱数を送信
          await message.channel.send(f"> Generated numbers: {numbers}")
          print(f"{numbers} - NO")
      await self.edit_status(text=f".help | Used in {len(guilds)} servers!")
      
    if message.content == '.g':
      numbers = [random.randint(0, 9) for _ in range(10)]
      # 生成された乱数が全て同じかどうかチェック
      if numbers[0] == numbers[1] == numbers[2] == numbers[3] == numbers[4] == numbers[5] == numbers[6] == numbers[7] == numbers[8] == numbers[9]:
          # Revoltのチャンネルに"good"と送信
          await message.channel.send(f"> Good! \n > Generated numbers: {numbers}")
          print(f"{numbers} - YES")
      else:
          # 乱数が異なる場合は、その乱数を送信
          await message.channel.send(f"> Generated numbers: {numbers}")
          print(f"{numbers} - NO")
    if message.content == '.c':
      colorsR = random.sample(colors, 3)
      # 生成された乱数が全て同じかどうかチェック
      if colorsR[0] == colorsR[1] == colorsR[2]:
          # Revoltのチャンネルに"good"と送信
          await message.channel.send(f"> Good! \n > Generated colors: {colorsR}")
          print(f"{colorsR} - YES")
      else:
          # 乱数が異なる場合は、その乱数を送信
          await message.channel.send(f"> Generated colors: {colorsR}")
          print(f"{colorsR} - NO")
    if message.content == '.help':
        await message.channel.send(f"> ##  **Rouletto**\n > ### ***You can play roulette***\n > Normal mode:`.r`  \n > Hard mode:`.g` \n > Colors mode:`.c`\n> Help:`.help` \n> Bot info:`.info`\n > ##### [Invite](https://app.revolt.chat/bot/01HS541Y8H5TQMWVEQD2VK213M) |  [Vote for the bot and support it!](https://revoltbots.org/bots/01HS541Y8H5TQMWVEQD2VK213M/vote)\n> ##### Management:<@01HJQHPJKEERVFMY165QGVF6DC> | <@01HS541Y8H5TQMWVEQD2VK213M>")
    if message.content == '.info':
        await message.channel.send(f"> # Roulette Bot info\n> Used in {len(guilds)} servers") 
    if message.content == '.post':
        server_count = f"{len(guilds)}"
        send_server_count(server_count)
        await message.channel.send(f"Status code: {response.status_code}") 
      
    



async def main():
  async with revolt.utils.client_session() as session:
    client = Client(session, os.environ['R'])
    await client.start()




always_on.activate()

asyncio.run(main())
