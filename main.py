import revolt
import requests
import asyncio
import os
import random
import always_on

class Client(revolt.Client):

  async def on_ready(self):
    print('Run  ルーレットBOT')
    await reconnect()
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

      with open('roulette_log.txt', 'a') as f:
        f.write(f'User ID: {user_id}, Numbers: {numbers}\n')
    if message.content == '.g':
      numbers = [random.randint(0, 9) for _ in range(10)]

      # 生成された乱数が全て同じかどうかチェック
      if numbers[0] == numbers[1] == numbers[2] == numbers[3] == numbers[4] == numbers[5] == numbers[6] == numbers[7] == numbers[8] == numbers[9]:
          # Revoltのチャンネルに"good"と送信
          await message.channel.send(f"good! {numbers}")
          print(f"{numbers} - YES")
      else:
          # 乱数が異なる場合は、その乱数を送信
          await message.channel.send(f"Generated numbers: {numbers}")
          print(f"{numbers} - NO")
      
      with open('roulette_log.txt', 'a') as f:
        f.write(f'User ID: {user_id}, Numbers: {numbers}\n')
    



async def main():
  async with revolt.utils.client_session() as session:
    client = Client(session, os.environ['Revolt-TOKEN'])
    await client.start()
    

