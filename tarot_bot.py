import cards

import discord
import configparser

client = discord.Client()

deck = cards.Deck(cards.tarot_deck)

#Import discord token from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
token = config['main']['token']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$draw'):
        try:
            drawn_card = deck.draw()
            await message.channel.send(f'You drew {drawn_card.name}.')
        except IndexError:
            await message.channel.send('Deck is out of cards!')

    if message.content.startswith('$remains'):
        await message.channel.send(f'There are {len(deck)} cards remaining.')
    
    if message.content.startswith('$reset'):
        deck.reset()
        await message.channel.send('All cards are back in the deck.')
        

print(token)
#client.run(token)