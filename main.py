import revolt
import requests
import asyncio
import os

import always_on
import time


async def reconnect():
  while True:
    requests.get("https://api.render.com/deploy/srv-cnqlbhn109ks73fcbbp0?key=5QJY5VfBmLs")
    await asyncio.sleep(600)



class Client(revolt.Client):
  
  async def on_ready(self):
    print('Run  連投bot-revolt')
    await reconnect()
  


  async def on_message(self, message: revolt.Message):
    

    
      
    if message.content == "./rentou":
      print('./rentou')
      for _ in range(10):

        await message.channel.send("連投")
    if message.content == "..l":
      print('見えない連投')
      for _ in range(10):

        await message.channel.send("[](..)")
    if message.content == "./run.rentou":
      await message.channel.send("> 連投Bot - Replit")
    

    

    
    

    
    
    if message.content == "./gazou.rentou":
      print('//gazou.rentou')
      for _ in range(10):
        await message.channel.send("[](https://autumn.revolt.chat/attachments/2PlNj2OIRXFulLko2A89x4s-cIRjlvjneldZyGIPt5/027cdc8e74424ea19922161c35befd5c_high.webp)")
    if message.content == "//sasa.rentou":
      print('./sasa.rentou')
      for _ in range(10):

        await message.channel.send("笹")
    if message.content == "./emoji.rentou":
      print('./emoji.rentou')
      for _ in range(10):
        
        await message.channel.send(":01H8TTWPE28K7CY4AHGX652FBF:")
    if message.content == "./ms":
      await message.channel.send(os.environ['message'])
    if message.content == "./help.rentou":
      print('./help.rentou')
      await message.channel.send(
        '> コマンド一覧|||./rentou:「連投」というメッセージが連投します|||./gazou.rentou:画像が連投します(画像はztttas1が画像生成AIで作成したものです)|./sasa.rentou:「笹」というメッセージが連投します|||./run.rentou:起動しているかチェック出来ます|||./emoji.rentou:絵文字を連投します||||./ver.rentou:バージョンを知れます'
      )
    
    
    if message.content == "./":
      print('//senden')
      await message.channel.send("")
      
    
    
    if "[](" in message.content:
       print('空白メッセージ検知')
       
       requests.get("https://lian-tou-bot.ztttas11.repl.co/")
    if message.content == "//ver.rentou":
       await message.channel.send(os.environ['ver'])
        

    
    



async def main():
  async with revolt.utils.client_session() as session:
    client = Client(session, os.environ['Revolt-TOKEN'])
    await client.start()
    





always_on.activate()

asyncio.run(main())
