import json
from aiogram import F
from aiogram.types import Message

from main import dp
from app.help_command import help_command


@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        f"Hello, {message.from_user.first_name}!\n"
        "Write /help to find out about all the commands and all the available countries."
    )


@dp.message(F.text == "/help")
async def cmd_help(message: Message):
    await message.answer(help_command)


# Countries
# ----------------------------------------------------


@dp.message(F.text.lower() == "/austria")
async def AT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["AT"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["AT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/albania")
async def AL(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["AL"]["flag"]} The capital of {data["countries"]["AL"]["country"]}: {data["countries"]["AL"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["AL"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/andorra")
async def AD(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["AD"]["flag"]} The capital of {data["countries"]["AD"]["country"]}: {data["countries"]["AD"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["AD"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/belarus")
async def BY(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BY"]["flag"]} The capital of {data["countries"]["BY"]["country"]}: {data["countries"]["BY"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["BY"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/belgium")
async def BE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BE"]["flag"]} The capital of {data["countries"]["BE"]["country"]}: {data["countries"]["BE"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["BE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/bosnia")
async def BA(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BA"]["flag"]} The capital of {data["countries"]["BA"]["country"]}: {data["countries"]["BA"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["BA"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/bulgaria")
async def BG(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BG"]["flag"]} The capital of {data["countries"]["BG"]["country"]}: {data["countries"]["BG"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["BG"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/croatia")
async def HR(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["HR"]["flag"]} The capital of {data["countries"]["HR"]["country"]}: {data["countries"]["HR"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["HR"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/czechia")
async def CZ(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["CZ"]["flag"]} The capital of {data["countries"]["CZ"]["country"]}: {data["countries"]["CZ"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["CZ"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/denmark")
async def DK(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["DK"]["flag"]} The capital of {data["countries"]["DK"]["country"]}: {data["countries"]["DK"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["DK"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/estonia")
async def EE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["EE"]["flag"]} The capital of {data["countries"]["EE"]["country"]}: {data["countries"]["EE"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["EE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/finland")
async def FI(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["FI"]["flag"]} The capital of {data["countries"]["FI"]["country"]}: {data["countries"]["FI"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["FI"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/france")
async def FR(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["FR"]["flag"]} The capital of {data["countries"]["FR"]["country"]}: {data["countries"]["FR"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["FR"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/germany")
async def DE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["DE"]["flag"]} The capital of {data["countries"]["DE"]["country"]}: {data["countries"]["DE"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["DE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/greece")
async def GR(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["GR"]["flag"]} The capital of {data["countries"]["GR"]["country"]}: {data["countries"]["GR"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["GR"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/hungary")
async def HU(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["HU"]["flag"]} The capital of {data["countries"]["HU"]["country"]}: {data["countries"]["HU"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["HU"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/iceland")
async def IS(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["IS"]["flag"]} The capital of {data["countries"]["IS"]["country"]}: {data["countries"]["IS"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["IS"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/ireland")
async def IE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["IE"]["flag"]} The capital of {data["countries"]["IE"]["country"]}: {data["countries"]["IE"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["IE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/italy")
async def IT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["IT"]["flag"]} The capital of {data["countries"]["IT"]["country"]}: {data["countries"]["IT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["IT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/latvia")
async def LV(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["LV"]["flag"]} The capital of {data["countries"]["LV"]["country"]}: {data["countries"]["LV"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["LV"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/lithuania")
async def LT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["LT"]["flag"]} The capital of {data["countries"]["LT"]["country"]}: {data["countries"]["LT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["LT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/luxembourg")
async def LU(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["LU"]["flag"]} The capital of {data["countries"]["LU"]["country"]}: {data["countries"]["LU"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["LU"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/malta")
async def MT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MT"]["flag"]} The capital of {data["countries"]["MT"]["country"]}: {data["countries"]["MT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["MT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/moldova")
async def MD(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MD"]["flag"]} The capital of {data["countries"]["MD"]["country"]}: {data["countries"]["MD"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["MD"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/monaco")
async def MC(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MC"]["flag"]} The capital of {data["countries"]["MC"]["country"]}: {data["countries"]["MC"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["MC"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/montenegro")
async def ME(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["ME"]["flag"]} The capital of {data["countries"]["ME"]["country"]}: {data["countries"]["ME"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["ME"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/netherlands")
async def NL(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["NL"]["flag"]} The capital of {data["countries"]["NL"]["country"]}: {data["countries"]["NL"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["NL"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/macedonia")
async def MK(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MK"]["flag"]} The capital of {data["countries"]["MK"]["country"]}: {data["countries"]["MK"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["MK"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/norway")
async def NO(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["NO"]["flag"]} The capital of {data["countries"]["NO"]["country"]}: {data["countries"]["NO"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["NO"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/poland")
async def PL(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["PL"]["flag"]} The capital of {data["countries"]["PL"]["country"]}: {data["countries"]["PL"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["PL"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/portugal")
async def PT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["PT"]["flag"]} The capital of {data["countries"]["PT"]["country"]}: {data["countries"]["PT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["PT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/romania")
async def RO(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["RO"]["flag"]} The capital of {data["countries"]["RO"]["country"]}: {data["countries"]["RO"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["RO"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/serbia")
async def RS(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["RS"]["flag"]} The capital of {data["countries"]["RS"]["country"]}: {data["countries"]["RS"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["RS"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/slovakia")
async def SK(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["SK"]["flag"]} The capital of {data["countries"]["SK"]["country"]}: {data["countries"]["SK"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["SK"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/slovenia")
async def SI(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["SI"]["flag"]} The capital of {data["countries"]["SI"]["country"]}: {data["countries"]["SI"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["SI"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/spain")
async def ES(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["ES"]["flag"]} The capital of {data["countries"]["ES"]["country"]}: {data["countries"]["ES"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["ES"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/sweden")
async def SE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["SE"]["flag"]} The capital of {data["countries"]["SE"]["country"]}: {data["countries"]["SE"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["SE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/switzerland")
async def CH(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["CH"]["flag"]} The capital of {data["countries"]["CH"]["country"]}: {data["countries"]["CH"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["CH"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/ukraine")
async def UA(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["UA"]["flag"]} The capital of {data["countries"]["UA"]["country"]}: {data["countries"]["UA"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["UA"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/unitedkingdom")
async def GB(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["GB"]["flag"]} The capital of {data["countries"]["GB"]["country"]}: {data["countries"]["GB"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["GB"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


@dp.message(F.text.lower() == "/vatican")
async def VA(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["VA"]["flag"]} The capital of {data["countries"]["VA"]["country"]}: {data["countries"]["VA"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        f"*🏰 Here are the 5 best places to visit:*\n\n\n", parse_mode="Markdown"
    )

    for place in data["countries"]["VA"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


# ----------------------------------------------------


@dp.message()
async def echo(message: Message):
    await message.answer("I don't understand you.😔😢")
