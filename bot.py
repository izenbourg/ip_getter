import discord
from selenium import webdriver
import os
client = discord.Client()
@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	if "hello" in message.content.lower():
		 await message.channel.send('Hi!')
	elif "todays_ip" in message.content.lower():
		driver = webdriver.Chrome("C:/Users/admin/Desktop/chromedriver")
		driver.get("https://whatsmyip.com/your-ip-address")
		driver.maximize_window()
		driver.save_screenshot("screenshot.png")
		driver.close()
		file = discord.File("screenshot.png", filename="screenshot.png")
		await message.channel.send("screenshot.png", file=file)
client.run("NjA2NTkwMTI5NTkwNzYzNTYw.XUNRUw.E5_6c5MmkJWn0haPe1COcbX2JlI")
