import os
import re
import sys
import time
import requests
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
BOT_TOKEN = 'your_bot_token'

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>Hello {m.from_user.mention} 👋\n\n➨ I am Txt to Video Uploader Bot.\n\n➨ Bot Made By THE BOY\n\n➨ For Use Me Send /BOYS Command.\n\n➨ And Follow Few Steps.\n\n➨ Use /stop Command For Stopping Ongoing Process.</b>")

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**BAND**💗", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["BOYS"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('𝗦𝗘𝗡𝗗 𝗧𝗫𝗧')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("**👩‍🎓𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗳𝗶𝗹𝗲 𝗶𝗻𝗽𝘂𝘁.**")
        os.remove(x)
        return

    await editable.edit(f"**𝗧𝗼𝘁𝗮𝗹 𝗟𝗶𝗻𝗸𝘀 𝗙𝗼𝘂𝗻𝗱 𝗔𝗿𝗲🔗🔗** **{len(links)}**\n\n**𝗦𝗲𝗻𝗱 𝗙𝗿𝗼𝗺 𝗪𝗵𝗲𝗿𝗲 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗜𝗻𝗶𝘁𝗶𝗮𝗹 𝗜𝘀** **𝟭**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝗡𝗼𝘄 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗬𝗼𝘂𝗿 𝗕𝗮𝘁𝗰𝗵 𝗡𝗮𝗺𝗲**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit("**𝗘𝗡𝗧𝗘𝗥 𝗥𝗘𝗦𝗢𝗟𝗨𝗧𝗜𝗢𝗡📸**\n𝟭𝟰𝟰,𝟮𝟰𝟬,𝟯𝟲𝟬,𝟰𝟴𝟬,𝟳𝟮𝟬,𝟭𝟬𝟴𝟬 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗵𝗼𝗼𝘀𝗲 𝗾𝘂𝗮𝗹𝗶𝘁𝘆")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"

    await editable.edit("𝗡𝗼𝘄 𝗘𝗻𝘁𝗲𝗿 𝗔 𝗖𝗮𝗽𝘁𝗶𝗼𝗻 𝗧𝗼 𝗔𝗱𝗱 𝗖𝗮𝗽𝘁𝗶𝗼𝗻 𝗢𝗻 𝗬𝗼𝘂𝗿 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗙𝗶𝗹𝗲\n\n𝗘𝗴 » THE BOYS")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)

    await editable.edit("𝗡𝗼𝘄 𝗦𝗲𝗻𝗱 𝗧𝗵𝗲 𝗧𝗵𝘂𝗺𝗯 𝗨𝗿𝗹\n\n𝗢𝗿 𝗜𝗳 𝗗𝗼𝗻'𝘁 𝗪𝗮𝗻𝘁 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗦𝗲𝗻𝗱 = 𝗻𝗼")
    input6 = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        os.system(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    count = int(raw_text) if len(links) > 1 else 1

    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9'}).json()['url']

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            elif "webvideos.classplusapp" in url:
                cmd = f'yt-dlp --add-header "referer:https://web.classplusapp.com/" --add-header "x-cdn-tag:empty" -f "{ytf}" "{url}" -o "{name}.mp4"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'**[📽️] 𝗩𝗶𝗱_𝗜𝗗 :** {str(count).zfill(3)}.\n\n**❤️‍🔥𝗧𝗶𝘁𝗹𝗲** » {name1}.THE BOYS.mkv\n\n\n**📚𝗕𝗮𝘁𝗰𝗵 𝗡𝗮𝗺𝗲** » **{raw_text0}**\n\n\n**📥 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆** » **{raw_text3}**'
                cc1 = f'**[📁] 𝗣𝗱𝗳_𝗜𝗗 :** {str(count).zfill(3)}.\n\n**💗𝗧𝗶𝘁𝗹𝗲** » {name1}.THE BOYS.pdf\n\n\n**📚𝗕𝗮𝘁𝗰𝗵 𝗡𝗮𝗺𝗲** » **{raw_text0}**\n\n\n**📥 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆** » **{raw_text3}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                        count += 1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⬇️𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆⬇️... »**\n\n**📝Name »**`{name}\n\n❄Quality » {raw_text2}`\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(f"**downloading Interrupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`")
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**😎✅𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗗𝗼𝗻𝗲✅😎 Mission complete**")

bot.run()
