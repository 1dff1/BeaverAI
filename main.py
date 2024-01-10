from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from sqltools import exists_in_table, add_record
from freeGPT import AsyncClient

API_TOKEN: str = 'API Token'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


async def set_main_menu(bot: Bot):
    menu = [
        BotCommand(command='/start',
                   description='Start'),
        BotCommand(command='/donat',
                   description='Support the beavers'),
        BotCommand(command='/help',
                   description='Help'),
        BotCommand(command='/gpt',
                   description='AI assistant')]
    await bot.set_my_commands(menu)


@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    user = message.from_user
    username = user.username
    if exists_in_table('users', ('name', username)):
        await message.answer(f'Hello {username}.')
    else:
        add_record(username, 0, 'users', 'name', 'cash')
        await message.answer(f'Hello {username}. '
                             '\nYou have successfully registered!!!')


@dp.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer('/gpt command to call the assistant.\n'
                         'For the query, write the gpt. \n'
                         'Example: /gpt write a 70-word essay')


@dp.message(Command(commands=["gpt"]))
async def gpt_command(message: Message):
    await message.answer('Wait..')
    prompt = message.text[4:]
    try:
        resp = await AsyncClient.create_completion("gpt3", prompt)
        await message.answer(resp)
    except Exception as e:
        await message.answer(e)


if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)
