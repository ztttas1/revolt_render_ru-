import revolt
import requests
import asyncio
import os
import random
import always_on



async def reconnect():
  while True:
    requests.get("https://lian-tou-bot.ztttas11.repl.co/")
    await asyncio.sleep(60)



async def on_message(self, message: revolt.Message):
    

    
      
    
    if message.content == '.r':
      numbers = [random.randint(0, 9) for _ in range(3)]

      # 生成された乱数が全て同じかどうかチェック
      if numbers[0] == numbers[1] == numbers[2]:
          # Revoltのチャンネルに"good"と送信
          await message.channel.send(f"good! {numbers}")
          print(f"{numbers} - YES")
      else:
          # 乱数が異なる場合は、その乱数を送信
          await message.channel.send(f"Generated numbers: {numbers}")
          print(f"{numbers} - NO")
    
    



async def main():
  async with revolt.utils.client_session() as session:
    client = Client(session, os.environ['Revolt-TOKEN'])
    await client.start()
    





always_on.activate()

asyncio.run(main())
