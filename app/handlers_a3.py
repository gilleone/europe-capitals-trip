import json
from aiogram import F
from aiogram.types import Message

from main_a3 import dp
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


# ----------------------------------------------------


@dp.message(F.text.lower() == "/austria")
async def AT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["AT"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["AT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/albania")
async def AL(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["AL"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["AL"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/andorra")
async def AD(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["AD"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["AD"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/belarus")
async def BY(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BY"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["BY"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/belgium")
async def BE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BE"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["BE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/bosnia")
async def BA(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BA"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["BA"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/bulgaria")
async def BG(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["BG"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["BG"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/croatia")
async def HR(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["HR"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["HR"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/czechia")
async def CZ(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["CZ"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["CZ"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/denmark")
async def DK(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["DK"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["DK"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/estonia")
async def EE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["EE"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["EE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/finland")
async def FI(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["FI"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["FI"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/france")
async def FR(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["FR"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["FR"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/germany")
async def DE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["DE"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["DE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/germany")
async def DE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["DE"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["DE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/greece")
async def GR(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["GR"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["GR"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/hungary")
async def HU(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["HU"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["HU"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/ireland")
async def IE(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["IE"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["IE"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/italy")
async def IT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["IT"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["IT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/latvia")
async def LV(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["LV"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["LV"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/lithuania")
async def LT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["LT"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["LT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/luxembourg")
async def LU(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["LU"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["LU"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/malta")
async def MT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MT"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["MT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/moldova")
async def MD(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MD"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["MD"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/monaco")
async def MC(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MC"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["MC"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/montenegro")
async def ME(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["ME"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["ME"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/netherlands")
async def NL(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["NL"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["NL"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/northmacedonia")
async def MK(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["MK"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["MK"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/norway")
async def NO(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["NO"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["NO"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/poland")
async def PL(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["PL"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["PL"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/portugal")
async def PT(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["PT"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["PT"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/romania")
async def RO(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["RO"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["RO"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/serbia")
async def RS(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["RS"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["RS"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/slovakia")
async def SK(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["SK"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["SK"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


@dp.message(F.text.lower() == "/slovenia")
async def SI(message: Message):
    with open("app/country_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    response = f'*{data["countries"]["SI"]["flag"]} The capital of {data["countries"]["AT"]["country"]}: {data["countries"]["AT"]["capital"]}*'
    await message.answer(response, parse_mode="Markdown")

    for place in data["countries"]["SI"]["places"]:
        caption = f'{place["number"]} *Place*: {place["name"]}\n*📖 Description:*{place["about"]}\n\n 🔗 The link to the map: [Link]({place["on_map"]})'
        await message.answer_photo(
            photo=place["photo"], caption=caption, parse_mode="Markdown"
        )


# ----------------------------------------------------


@dp.message()
async def echo(message: Message):
    await message.answer("Я тебя не понимаю...")
