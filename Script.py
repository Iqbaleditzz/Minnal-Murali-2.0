class script(object):
    START_TXT = """<b>Hello {}</b>

<i>Iam A Simple Auto Filter Bot Of @CINIMA_KALAVARA . \nI Can Provide Movies In @CINIMA_KALAVARA Don't Try to Add To Me In Your Group </i>

<b>Made With ❤ BY @IET_Updates</b>"""
    HELP_TXT = """ʜᴇʏ {}
<b>Some കാട്ടിക്കൂട്ടൽ Of My Invention 😁</b>"""
    ABOUT_TXT = """<b>🤖 ʙᴏᴛ ɴᴀᴍᴇ: <a href= https://t.me/MinnalsMuraliBot>🦸 Mɪɴɴᴀʟ Mᴜʀᴀʟɪ</a></b>
 
<b>📝 ʟᴀɴɢᴜᴀɢᴇ :</b><b> <a href= https://www.python.org/>ᴘʏᴛʜᴏɴ³</a></b> 

<b>📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ :</b><b> <a href= https://docs.pyrogram.org/>ᴘʏʀᴏɢʀᴀᴍ</a></b>

<b>📡 ʜᴏsᴛᴇᴅ ᴏɴ :</b><b> <a href= https://www.heroku.com/>ʜᴇʀᴏᴋᴜ</a></b>

<b>👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b><b> <a href= https://t.me/Iqbal_KA>Iǫʙᴀʟ ᴋ ᴀ</a></b>

<b>💡 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :</b><b> <a href= https://t.me/IET_Owner/724>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>

<b>👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :</b><b> <a href= https://t.me/IET_SUPPORT>ɪᴇᴛ sᴜᴘᴘᴏʀᴛ</a></b>

<b>📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ :</b><b> <a href= https://t.me/IET_Updates>ɪᴇᴛ ᴜᴘᴅᴀᴛᴇs</a></b>"""
    SOURCE_TXT = """<b>മിന്നൽ മുരളി</b>
<b><u>📽️ How To Create This BoT.?</u></b>

<i><a href= https://youtu.be/1ltbuCY_V6s>എങ്ങനെ ഉണ്ടാക്കാം എന്ന് അറിയാൻ ഇവിടെ ക്ലിക്ക് ചെയ്താൽ മതി.</a></i>
<b>Support channel:</b>
- <a href=https://t.me/IET_support>IET SUPPORT</a>"""
    MANUELFILTER_TXT = """<b>Auto Filter</b>
𝖭𝗈𝗍𝖾:
Auto Filter is the feature to filter and save all the files automatically from channel to group. This mostly used in group to get movies with name!

USAGE:
➢ /autofilter [on] - Enable auto filter in the chat.
➢ /autofilter [off] - Disable auto filter in the chat.

NOTE:
• Make me the admin of your channel if it's private.
• Make sure that your channel does not contains camrips, porn and fake files.
• Forward the last message to me with quotes or send me the last message link.

<b>𝖥𝗂𝗅𝗍𝖾𝗋𝗌</b>
𝖥𝗂𝗅𝗍𝖾𝗋 𝗂𝗌 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗐𝖾𝗋𝖾 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝗌𝖾𝗍 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝗋𝖾𝗉𝗅𝗂𝖾𝗌 𝖿𝗈𝗋 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗁𝖾𝗇𝖾𝗏𝖾𝗋 𝖺 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝗂𝗌 𝖿𝗈𝗎𝗇𝖽 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 
𝖭𝖮𝖳𝖤:
𝟣. 𝖻𝗈𝗍 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾 𝗂𝗇 𝗈𝗋𝖽𝖾𝗋 𝗍𝗈 𝗋𝖾𝗉𝗅𝗒 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟤. 𝗈𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟥. 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖽𝗈𝖾𝗌 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖺𝗋𝗄𝖽𝗈𝗐𝗇𝗌, 𝗆𝖾𝖽𝗂𝖺𝗌 𝖺𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌. 
𝟦. 𝖺𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝖺𝗋𝖾 𝖺𝗅𝗌𝗈 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝗐𝗂𝗍𝗁 𝖺 𝗅𝗂𝗆𝗂𝗍 𝗈𝖿 𝟨𝟦 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌. 
𝟧. 𝗍𝗁𝖾𝗋𝖾 𝖺𝗋𝖾 𝗌𝗈𝗆𝖾 𝖾𝖺𝗌𝗍𝖾𝗋 𝖾𝗀𝗀𝗌, 𝗍𝗋𝗒 𝗍𝗈 𝖿𝗂𝗇𝖽 𝗂𝗍 𝗈𝗎𝗍. 
𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:
/filter  𝗈𝗋 /add - 𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋
/filters 𝗈𝗋 /viewfilters - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍 
/stop 𝗈𝗋 /del - 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋 (𝗌𝖾𝗉𝖺𝗋𝖺𝗍𝖾 𝗄𝖾𝗒𝗐𝗈𝗋𝖽𝗌 𝗐𝗂𝗍𝗁 𝗌𝗉𝖺𝖼𝖾𝗌 𝖿𝗈𝗋 𝖽𝖾𝗅𝖾𝗍𝗂𝗇𝗀 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖺𝗍 𝖺 𝗍𝗂𝗆𝖾) 
/stopall 𝗈𝗋 /delall - 𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍 (𝖼𝗁𝖺𝗍 𝗈𝗐𝗇𝖾𝗋 𝗈𝗇𝗅𝗒)

𝖬𝖺𝖽𝖾 𝖻𝗒 @IET_UPDATES ❤️"""
    BUTTON_TXT = """Help: <b>𝖡𝗎𝗍𝗍𝗈𝗇𝗌</b>
This 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝗎𝗋𝗅 𝖺𝗇𝖽 𝖺𝗅𝖾𝗋𝗍 𝗂𝗇𝗅𝗂𝗇𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌, 𝗇𝗈𝗐 𝗅𝖾𝗍𝗌 𝗌𝖾𝖾 𝗁𝗈𝗐 𝗍𝗈 𝗂𝗆𝗉𝗅𝖾𝗆𝖾𝗇𝗍 𝗂𝗍. 
𝖭𝖡:
𝟣. 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝗍𝖾𝗇𝗍, 𝗌𝗈 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝗆𝖺𝗇𝖽𝖺𝗍𝗈𝗋𝗒. 
𝟤. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁 𝖺𝗇𝗒 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖾𝖽𝗂𝖺 𝗍𝗒𝗉𝖾. 
𝟥. 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝗌𝗁𝗈𝗎𝗅𝖽 𝖻𝖾 𝗉𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝖿𝗈𝗋𝗆𝖺𝗍𝗍𝖾𝖽 𝖺𝗌 𝖻𝖾𝗅𝗈𝗐 𝗈𝗋 𝖾𝗅𝗌𝖾 𝗋𝖾𝗌𝗎𝗅𝗍 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗆𝖺𝗅𝖿𝗈𝗋𝗆𝖾𝖽. 
𝖴𝖱𝖫 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:
- 𝗌𝗂𝗇𝗀𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/mm_seriess)
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/mm_seriess)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/mm_moviess)
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗂𝗇 𝖲𝖺𝗆𝖾 𝖱𝖺𝗐 
[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/mm_seriess)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/mm_moviess:𝗌𝖺𝗆𝖾)
𝖠𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:
[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝖺𝗅𝖾𝗋𝗍:𝗍𝗁𝗂𝗌 𝗂𝗌 𝖺𝗇 𝖺𝗅𝖾𝗋𝗍!)

 ❤️ 𝖬𝖺𝖽𝖾 𝖻𝗒 @IET_UPDATES ❤️"""
    AUTOFILTER_TXT = """<b>𝖯𝗎𝗋𝗀𝖾</b>
- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺 𝗅𝗈𝗍𝗌 𝗈𝖿 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝖺 𝗀𝗋𝗈𝗎𝗉!
    
 𝖠𝖽𝗆𝗂𝗇 
◉ /purge :- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈, 𝖳𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾

𝖬𝖺𝖽𝖾 𝖻𝗒 @IET_UPDATES ❤️"""
    CONNECTION_TXT = """<b>𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌</b>
𝖴𝗌𝖾𝖽 𝗍𝗈 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖻𝗈𝗍 𝗍𝗈 𝖯𝖬 𝗐𝗁𝗂𝖼𝗁 𝗅𝖾𝗍 𝗐𝗂𝗅𝗅 𝗒𝗈𝗎 𝗍𝗈 𝖾𝗑𝖾𝖼𝗎𝗍𝖾 𝖻𝗈𝗍𝗁 𝗇𝗈𝗋𝗆𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝗌𝗈𝗆𝖾 𝗈𝗍𝗁𝖾𝗋 𝗌𝖾𝗇𝗌𝗂𝗍𝗂𝗏𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗋𝗂𝗀𝗁𝗍 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖯𝖬 𝗍𝗁𝖺𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝖿𝗅𝖾𝖼𝗍 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉 𝗐𝗁𝗂𝖼𝗁 𝗁𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗄𝖾𝖾𝗉 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋 𝖺𝖽𝖽𝗂𝗍𝗂𝗈𝗇𝗌 𝖺𝗇𝖽 𝗈𝗍𝗁𝖾𝗋 𝗌𝗍𝗎𝖿𝖿𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖺𝗇𝖽 𝗁𝖾𝗅𝗉𝗌 𝗍𝗈 𝗉𝗋𝖾𝗏𝖾𝗇𝗍 𝖿𝗅𝗈𝗈𝖽𝗂𝗇𝗀. 
𝖭𝖮𝖳𝖤:
𝟣. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇. 
𝟤. 𝖨𝗇 𝖺 𝖼𝗁𝖺𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝗂𝗆𝗉𝗅𝗒 𝗎𝗌𝖾 𝗍𝗁𝖾 /connect 𝖿𝗈𝗋 𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇  
𝟥. 𝖨𝗇 𝖯𝖬 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝖼𝗁𝖺𝗍 𝗂𝖽 𝗋𝗂𝗀𝗁𝗍 𝖺𝖿𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽. 
𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾: 
/connect - 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖯𝖬 
/disconnect  - 𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍 
/connections - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌

𝖬𝖺𝖽𝖾 𝖻𝗒 @IET_Updates ❤️"""
    EXTRAMOD_TXT = """<b>Files Store</b>
- This module will allow you to store files on this bot and share the link !!
Command
- /link - To store one file
- /batch - To Store Batch Files More than One

Made by @IET_Updates ❤️"""
    ADMIN_TXT = """<b>𝖬𝗎𝗍𝖾:</b>

𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 Muted; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!   

<b>🔞 𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>

- /mute - 𝖬𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋 
- /tmute - 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌. 
- /unmute - 𝖴𝗇mute 𝖺 𝗎𝗌𝖾𝗋.  
𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:
- 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tmute @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁

𝖬𝖺𝖽𝖾 𝖻𝗒 @IET_UPDATES ❤️"""
    STATUS_TXT = """<b>📁 ᴛᴏᴛᴀʟ ꜰɪʟᴇs: {}</b>

<b>👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: {} 🕸️</b>
No Other Information Available here"""
    LOG_TEXT_G = """#NewGroup
 Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
 Name - {}
"""
