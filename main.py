import revolt
import requests
import asyncio
import os
import random
import always_on

colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "⬛", "⬜"]

class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):

        if message.content == '.r':
            numbers = [random.randint(0, 9) for _ in range(3)]
            user_name = message.author.name
            if numbers[0] == numbers[1] == numbers[2]:
                await message.channel.send(f"> Good! \n > Generated numbers: {numbers}\n> User:{user_name}")
                print(f"{numbers} - YES")
            else:
                await message.channel.send(f"> Generated numbers: {numbers}\n> User:{user_name}")
                print(f"{numbers} - NO")
        
        if message.content == '.g':
            user_name = message.author.name
            numbers = [random.randint(0, 9) for _ in range(10)]
            if all(n == numbers[0] for n in numbers):
                await message.channel.send(f"> Good! \n > Generated numbers: {numbers}\n> User:{user_name}")
                print(f"{numbers} - YES")
            else:
                await message.channel.send(f"> Generated numbers: {numbers}\n>User:{user_name}")
                print(f"{numbers} - NO")
        
        if message.content == '.c':
            user_name = message.author.name
            colorsR = random.sample(colors, 3)
            if colorsR[0] == colorsR[1] == colorsR[2]:
                await message.channel.send(f"> Good! \n > Generated colors: {colorsR}\n> User:{user_name}")
                print(f"{colorsR} - YES")
            else:
                await message.channel.send(f"> Generated colors: {colorsR}\n> User:{user_name}")
                print(f"{colorsR} - NO")
        
        if message.content == '.help':
            await message.channel.send(f"> ##  **Rouletto**\n > ### ***You can play roulette***\n > Normal mode:`.r`  \n > Hard mode:`.g` \n > Colors mode:`.c`\n> Help:`.help` \n> Bot info:`.info`\n > ##### [Invite](https://app.revolt.chat/bot/01HS541Y8H5TQMWVEQD2VK213M) |  [Vote for the bot and support it!](https://revoltbots.org/bots/01HS541Y8H5TQMWVEQD2VK213M/vote)\n> ##### Management:<@01HJQHPJKEERVFMY165QGVF6DC> | <@01HS541Y8H5TQMWVEQD2VK213M>")
        
        if message.content == '.info':
            await message.channel.send(f"> # Roulette Bot info\n> Used in {len(guilds)} servers")

    async def update_status(self):
        guilds = self.servers
        statuses = [
            f".help | Used in {guilds} servers!",
            f".r | Used in {guilds} servers!",
            f".g | Used in {guilds} servers!"
        ]
        while True:
            guilds = self.servers
            status = random.choice(statuses).format(len=self.servers)
            await self.edit_status(text=status)
            await asyncio.sleep(30)  # 60秒ごとにステータスを更新

async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, os.environ['R'])
        asyncio.create_task(client.update_status())  # ステータス更新タスクを開始
        await client.start()

always_on.activate()

asyncio.run(main())
