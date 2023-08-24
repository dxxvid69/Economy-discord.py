import discord
from discord.ext import commands

# Configurations
initial_balance = 100
work_earnings = 50
beg_earnings = 10

bot = commands.Bot(command_prefix='!')

# Simulated database for user balances
user_balances = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start(ctx):
    if ctx.author.id not in user_balances:
        user_balances[ctx.author.id] = initial_balance
        await ctx.send(f"Welcome, {ctx.author.name}! You've started with {initial_balance} credits.")

@bot.command()
async def work(ctx):
    if ctx.author.id in user_balances:
        user_balances[ctx.author.id] += work_earnings
        await ctx.send(f"You worked hard and earned {work_earnings} credits. Your balance: {user_balances[ctx.author.id]}")
    else:
        await ctx.send("You haven't started yet. Use `!start` to begin.")

@bot.command()
async def beg(ctx):
    if ctx.author.id in user_balances:
        user_balances[ctx.author.id] += beg_earnings
        await ctx.send(f"You begged and received {beg_earnings} credits. Your balance: {user_balances[ctx.author.id]}")
    else:
        await ctx.send("You haven't started yet. Use `!start` to begin.")

shop_items = {
    'item1': 25,
    'item2': 50,
    'item3': 75
}

@bot.command()
async def shop(ctx):
    shop_list = "\n".join([f"{item}: {price} credits" for item, price in shop_items.items()])
    await ctx.send(f"Available items in the shop:\n{shop_list}")

@bot.command()
async def buy(ctx, item: str):
    if ctx.author.id in user_balances:
        if item in shop_items:
            price = shop_items[item]
            if user_balances[ctx.author.id] >= price:
                user_balances[ctx.author.id] -= price
                await ctx.send(f"You bought {item} for {price} credits. Your balance: {user_balances[ctx.author.id]}")
            else:
                await ctx.send("You don't have enough credits to buy this item.")
        else:
            await ctx.send("Item not found in the shop.")
    else:
        await ctx.send("You haven't started yet. Use `!start` to begin.")

# Replace 'YOUR_TOKEN' with your actual bot token
bot.run('YOUR_TOKEN')
