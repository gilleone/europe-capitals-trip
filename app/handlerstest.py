from aiogram import types
from main import dp

from app.help_command import help_command
from app.countries import (
    AT,
    AL,
    AD,
    BY,
    BE,
    BA,
    BG,
    HR,
    CZ,
    DK,
    EE,
    FI,
    FR,
    DE,
    GR,
    HU,
    IS,
    IE,
    IT,
    LV,
    LT,
    LU,
    MT,
    MD,
    MC,
    ME,
    NL,
    MK,
    NO,
    PL,
    PT,
    RO,
    RS,
    SK,
    SI,
    ES,
    SE,
    CH,
    UA,
    GB,
    VA,
)

# --- commands ---


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.first_name}!\n"
        f"Write /help to find out about all the commands and all the available countries."
    )


@dp.message_handler(commands=["help"])
async def help_сommand(message: types.Message):
    await message.answer(help_command, parse_mode="Markdown")


async def send_places(message, country_data):
    response = f"*{country_data['flag']} The capital of {country_data['country']}: {country_data['capital']}*"

    await message.answer(response, parse_mode="Markdown")

    await message.answer(
        "*🏰 Here are the 5 best places to visit:*", parse_mode="Markdown"
    )

    for number, place, description, url, image_url in country_data["places"]:
        await message.answer_photo(
            image_url,
            f"{number} *Place*: {place}\n*📖 Description:* {description}\n\n🔗 The link to the map: [Link]({url})",
            parse_mode="Markdown",
        )

    await message.answer(
        "ℹ️ *Keep following my messages and you will learn about the most amazing places in the capitals of Europe!*",
        parse_mode="Markdown",
    )
    await message.answer("ℹ️ For more commands, you can use /help.")


# 🇦🇹
@dp.message_handler(commands=["Austria"])
async def Austria(message: types.Message):
    country_data = {
        "flag": "🇦🇹",
        "country": "Austria",
        "capital": "Vienna",
        "places": AT,
    }
    await send_places(message, country_data)


# 🇦🇱
@dp.message_handler(commands=["Albania"])
async def Albania(message: types.Message):
    country_data = {
        "flag": "🇦🇱",
        "country": "Austria",
        "capital": "Tirana",
        "places": AL,
    }
    await send_places(message, country_data)


# 🇦🇩
@dp.message_handler(commands=["Andorra"])
async def Andorra(message: types.Message):
    country_data = {
        "flag": "🇦🇩",
        "country": "Andorra",
        "capital": "Andorra la Vella",
        "places": AD,
    }
    await send_places(message, country_data)


# 🇧🇾
@dp.message_handler(commands=["Belarus"])
async def Belarus(message: types.Message):
    country_data = {
        "flag": "🇧🇾",
        "country": "Belarus",
        "capital": "Minsk",
        "places": BY,
    }
    await send_places(message, country_data)


# 🇧🇪
@dp.message_handler(commands=["Belgium"])
async def Belgium(message: types.Message):
    country_data = {
        "flag": "🇧🇪",
        "country": "Belgium",
        "capital": "Brussels",
        "places": BE,
    }
    await send_places(message, country_data)


# 🇧🇦
@dp.message_handler(commands=["Bosnia"])
async def BosniaAndHerzegovina(message: types.Message):
    country_data = {
        "flag": "🇧🇦",
        "country": "Bosnia and Herzegovina",
        "capital": "Sarajevo",
        "places": BA,
    }
    await send_places(message, country_data)


# 🇧🇬
@dp.message_handler(commands=["Bulgaria"])
async def Bulgaria(message: types.Message):
    country_data = {
        "flag": "🇧🇬",
        "country": "Bulgaria",
        "capital": "Sofia",
        "places": BG,
    }
    await send_places(message, country_data)


# 🇭🇷
@dp.message_handler(commands=["Croatia"])
async def Croatia(message: types.Message):
    country_data = {
        "flag": "🇭🇷",
        "country": "Croatia",
        "capital": "Zagreb",
        "places": HR,
    }
    await send_places(message, country_data)


# 🇨🇿
@dp.message_handler(commands=["Czechia"])
async def Czechia(message: types.Message):
    country_data = {
        "flag": "🇨🇿",
        "country": "Czechia",
        "capital": "Prague",
        "places": CZ,
    }
    await send_places(message, country_data)


# 🇩🇰
@dp.message_handler(commands=["Denmark"])
async def Denmark(message: types.Message):
    country_data = {
        "flag": "🇩🇰",
        "country": "Denmark",
        "capital": "Copenhagen",
        "places": DK,
    }
    await send_places(message, country_data)


# 🇪🇪
@dp.message_handler(commands=["Estonia"])
async def Estonia(message: types.Message):
    country_data = {
        "flag": "🇪🇪",
        "country": "Estonia",
        "capital": "Tallinn",
        "places": EE,
    }
    await send_places(message, country_data)


# 🇫🇮
@dp.message_handler(commands=["Finland"])
async def Finland(message: types.Message):
    country_data = {
        "flag": "🇫🇮",
        "country": "Finland",
        "capital": "Helsinki",
        "places": FI,
    }
    await send_places(message, country_data)


# 🇫🇷
@dp.message_handler(commands=["France"])
async def France(message: types.Message):
    country_data = {
        "flag": "🇫🇷",
        "country": "France",
        "capital": "Paris",
        "places": FR,
    }
    await send_places(message, country_data)


# 🇩🇪
@dp.message_handler(commands=["Germany"])
async def Germany(message: types.Message):
    country_data = {
        "flag": "🇩🇪",
        "country": "Germany",
        "capital": "Berlin",
        "places": DE,
    }
    await send_places(message, country_data)


# 🇬🇷
@dp.message_handler(commands=["Greece"])
async def Greece(message: types.Message):
    country_data = {
        "flag": "🇬🇷",
        "country": "Greece",
        "capital": "Athens",
        "places": GR,
    }
    await send_places(message, country_data)


# 🇭🇺
@dp.message_handler(commands=["Hungary"])
async def Hungary(message: types.Message):
    country_data = {
        "flag": "🇭🇺",
        "country": "Hungary",
        "capital": "Budapest",
        "places": HU,
    }
    await send_places(message, country_data)


# 🇮🇸
@dp.message_handler(commands=["Iceland"])
async def Iceland(message: types.Message):
    country_data = {
        "flag": "🇮🇸",
        "country": "Iceland",
        "capital": "Reykjavik",
        "places": IS,
    }
    await send_places(message, country_data)


# 🇮🇪
@dp.message_handler(commands=["Ireland"])
async def Ireland(message: types.Message):
    country_data = {
        "flag": "🇮🇪",
        "country": "Ireland",
        "capital": "Dublin",
        "places": IE,
    }
    await send_places(message, country_data)


# 🇮🇹
@dp.message_handler(commands=["Italy"])
async def Italy(message: types.Message):
    country_data = {
        "flag": "🇮🇹",
        "country": "Italy",
        "capital": "Rome",
        "places": IT,
    }
    await send_places(message, country_data)


# 🇱🇻
@dp.message_handler(commands=["Latvia"])
async def Latvia(message: types.Message):
    country_data = {
        "flag": "🇱🇻",
        "country": "Latvia",
        "capital": "Riga",
        "places": LV,
    }
    await send_places(message, country_data)


# 🇱🇹
@dp.message_handler(commands=["Lithuania"])
async def Lithuania(message: types.Message):
    country_data = {
        "flag": "🇱🇹",
        "country": "Lithuania",
        "capital": "Vilnius",
        "places": LT,
    }
    await send_places(message, country_data)


# 🇱🇺
@dp.message_handler(commands=["Luxembourg"])
async def Luxembourg(message: types.Message):
    country_data = {
        "flag": "🇱🇺",
        "country": "Luxembourg",
        "capital": "Luxembourg",
        "places": LU,
    }
    await send_places(message, country_data)


# 🇲🇹
@dp.message_handler(commands=["Malta"])
async def Malta(message: types.Message):
    country_data = {
        "flag": "🇲🇹",
        "country": "Malta",
        "capital": "Valletta",
        "places": MT,
    }
    await send_places(message, country_data)


# 🇲🇩
@dp.message_handler(commands=["Moldova"])
async def Moldova(message: types.Message):
    country_data = {
        "flag": "🇲🇩",
        "country": "Moldova",
        "capital": "Kishinev",
        "places": MD,
    }
    await send_places(message, country_data)


# 🇲🇨
@dp.message_handler(commands=["Monaco"])
async def Monaco(message: types.Message):
    country_data = {
        "flag": "🇲🇨",
        "country": "Monaco",
        "capital": "Monaco",
        "places": MC,
    }
    await send_places(message, country_data)


# 🇲🇪
@dp.message_handler(commands=["Montenegro"])
async def Montenegro(message: types.Message):
    country_data = {
        "flag": "🇲🇪",
        "country": "Montenegro",
        "capital": "Podgorica",
        "places": ME,
    }
    await send_places(message, country_data)


# 🇳🇱
@dp.message_handler(commands=["Netherlands"])
async def Netherlands(message: types.Message):
    country_data = {
        "flag": "🇳🇱",
        "country": "Netherlands",
        "capital": "Amsterdam",
        "places": NL,
    }
    await send_places(message, country_data)


# 🇲🇰
@dp.message_handler(commands=["North"])
async def Macedonia(message: types.Message):
    country_data = {
        "flag": "🇲🇰",
        "country": "North Macedonia",
        "capital": "Skopje",
        "places": MK,
    }
    await send_places(message, country_data)


# 🇳🇴
@dp.message_handler(commands=["Norway"])
async def Norway(message: types.Message):
    country_data = {
        "flag": "🇳🇴",
        "country": "Norway",
        "capital": "Oslo",
        "places": NO,
    }
    await send_places(message, country_data)


# 🇵🇱
@dp.message_handler(commands=["Poland"])
async def Poland(message: types.Message):
    country_data = {
        "flag": "🇵🇱",
        "country": "Poland",
        "capital": "Warsaw",
        "places": PL,
    }
    await send_places(message, country_data)


# 🇵🇹
@dp.message_handler(commands=["Portugal"])
async def Portugal(message: types.Message):
    country_data = {
        "flag": "🇵🇹",
        "country": "Portugal",
        "capital": "Lisbon",
        "places": PT,
    }
    await send_places(message, country_data)


# 🇷🇴
@dp.message_handler(commands=["Romania"])
async def Romania(message: types.Message):
    country_data = {
        "flag": "🇷🇴",
        "country": "Romania",
        "capital": "Bucharest",
        "places": RO,
    }
    await send_places(message, country_data)


# 🇷🇸
@dp.message_handler(commands=["Serbia"])
async def Serbia(message: types.Message):
    country_data = {
        "flag": "🇷🇸",
        "country": "Serbia",
        "capital": "Belgrade",
        "places": RS,
    }
    await send_places(message, country_data)


# 🇸🇰
@dp.message_handler(commands=["Slovakia"])
async def Slovakia(message: types.Message):
    country_data = {
        "flag": "🇸🇰",
        "country": "Slovakia",
        "capital": "Bratislava",
        "places": SK,
    }
    await send_places(message, country_data)


# 🇸🇮
@dp.message_handler(commands=["Slovenia"])
async def Slovenia(message: types.Message):
    country_data = {
        "flag": "🇸🇮",
        "country": "Slovenia",
        "capital": "Ljubljana",
        "places": SI,
    }
    await send_places(message, country_data)


# 🇪🇸
@dp.message_handler(commands=["Spain"])
async def Spain(message: types.Message):
    country_data = {
        "flag": "🇪🇸",
        "country": "Spain",
        "capital": "Madrid",
        "places": ES,
    }
    await send_places(message, country_data)


# 🇸🇪
@dp.message_handler(commands=["Sweden"])
async def Sweden(message: types.Message):
    country_data = {
        "flag": "🇸🇪",
        "country": "Sweden",
        "capital": "Stockholm",
        "places": SE,
    }
    await send_places(message, country_data)


# 🇨🇭
@dp.message_handler(commands=["Switzerland"])
async def Switzerland(message: types.Message):
    country_data = {
        "flag": "🇨🇭",
        "country": "Switzerland",
        "capital": "Bern",
        "places": CH,
    }
    await send_places(message, country_data)


# 🇺🇦
@dp.message_handler(commands=["Ukraine"])
async def Ukraine(message: types.Message):
    country_data = {
        "flag": "🇺🇦",
        "country": "Ukraine",
        "capital": "Kyiv",
        "places": UA,
    }
    await send_places(message, country_data)


# 🇬🇧
@dp.message_handler(commands=["United"])
async def GB(message: types.Message):
    country_data = {
        "flag": "🇬🇧",
        "country": "United Kingdom",
        "capital": "London",
        "places": GB,
    }
    await send_places(message, country_data)


# 🇻🇦
@dp.message_handler(commands=["Vatican"])
async def Vatican(message: types.Message):
    country_data = {
        "flag": "🇻🇦",
        "country": "Vatican",
        "capital": "Vatican",
        "places": VA,
    }
    await send_places(message, country_data)


@dp.message_handler()
async def dont_understand(message: types.Message):
    await message.reply("I don't understand you.")
