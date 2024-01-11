# BeaverAI RU
# Телеграм-бот с помощником на искусственном интеллекте

Это скрипт на языке Python, который создает телеграм-бота с помощником на искусственном интеллекте с использованием библиотеки `aiogram`. Бот реагирует на различные команды и взаимодействует с базой данных SQL и языковой моделью искусственного интеллекта.

## Подготовка

Перед запуском скрипта убедитесь, что у вас есть:

- Установленный Python на вашем компьютере
- Установленные необходимые библиотеки (`aiogram`, `sqltools` и `freeGPT`)
- Токен API вашего телеграм-бота

## Установка

1. Клонируйте репозиторий:

   ```
   git clone https://github.com/1dff1/BeaverAI
   ```

2. Установите необходимые библиотеки:

   ```
   pip install aiogram freeGPT
   ```

3. Замените `'Your API Token'` в скрипте на фактический токен API вашего телеграм-бота.

## Использование

Чтобы использовать телеграм-бота с помощником на искусственном интеллекте, выполните следующие шаги:

1. Запустите скрипт:

   ```
   python main.py
   ```

2. Начните разговор с ботом в Telegram.

3. Используйте следующие команды для взаимодействия с ботом:

   - `/start`: Начать разговор и зарегистрироваться как пользователь.
   - `/help`: Получить помощь по использованию помощника на искусственном интеллекте.
   - `/gpt`: Вызвать помощника на искусственном интеллекте и предоставить запрос.

## Функциональность

### Команда /start

Команда `/start` используется для начала разговора с ботом. Если вы уже зарегистрированы как пользователь, бот приветствует вас сообщением. В противном случае он регистрирует вас как нового пользователя в базе данных SQL и отправляет сообщение о успешной регистрации.

### Команда /help

Команда `/help` предоставляет информацию о том, как использовать помощника на искусственном интеллекте. Она объясняет, что команда `/gpt` используется для вызова помощника и приводит пример структуры запроса.

### Команда /gpt

Команда `/gpt` используется для вызова помощника на искусственном интеллекте и предоставления запроса. Когда вы отправляете команду, за которой следует ваш запрос, бот отправляет сообщение "Подождите.." и затем генерирует ответ с помощью языковой модели искусственного интеллекта. Ответ отправляется вам.

## Настройка

Вы можете настроить команды бота и ответы, изменяя код в скрипте. Вы можете добавлять или удалять команды, изменять сообщения-ответы и настраивать поведение бота в соответствии с вашими требованиями.

## Зависимости

- Библиотека `sqltools`: [https://github.com/1dff1/sqltools](https://github.com/1dff1/sqltools)

---

Этот README предоставляет обзор скрипта телеграм-бота с помощником на искусственном интеллекте. Для получения более подробной информации обратитесь к комментариям в коде и документации используемых библиотек.


# BeaverAI EN
# Telegram bot with an artificial intelligence assistant

This is a Python script that creates a telegram bot with an artificial intelligence assistant using the aiogram library. The bot responds to various commands and interacts with the SQL database and the artificial intelligence language model.

## Preparation

Before running the script, make sure that you have:

- Python installed on your computer
- Installed necessary libraries (`aiogram', `sqltools` and `freeGPT')
- API token of your telegram bot

## Installation

1. Clone the repository:

```
git clone https://github.com/1dff1/BeaverAI
```

2. Install the necessary libraries:

```
pip install aiogram freeGPT
```

3. Replace the `Your API Token" in the script with the actual API token of your telegram bot.

## Usage

To use a telegram bot with an artificial intelligence assistant, follow these steps:

1. Run the script:

```
python main.py
```

2. Start a conversation with the bot in Telegram.

3. Use the following commands to interact with the bot:

- `/start': Start a conversation and register as a user.
- `/help`: Get help using an artificial intelligence assistant.
- `/gpt`: Call an artificial intelligence assistant and provide a request.

## Functionality

### Command /start

The '/start` command is used to start a conversation with the bot. If you are already registered as a user, the bot greets you with a message. Otherwise, it registers you as a new user in the SQL database and sends a successful registration message.

### Command /help

The '/help` command provides information on how to use an artificial intelligence assistant. She explains that the `/gpt` command is used to call the assistant and gives an example of the request structure.

### Command /gpt

The `/gpt` command is used to call an artificial intelligence assistant and provide a request. When you send a command followed by your request, the bot sends a message "Wait.." and then generates a response using an artificial intelligence language model. The response is sent to you.

## Setting up

You can customize the bot's commands and responses by changing the code in the script. You can add or remove commands, change response messages, and customize the behavior of the bot according to your requirements.

## Dependencies

- The `sqltools' library: [https://github.com/1dff1/sqltools ](https://github.com/1dff1/sqltools )

---

This README provides an overview of the telegram bot script with an artificial intelligence assistant. For more information, refer to the comments in the code and documentation of the libraries used.
