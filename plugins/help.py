Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@bayuwicita 
bayuwicita
/
Force
Public
forked from Jigarvarma2005/ForceSub_Bot
Code
Pull requests
1
Actions
Projects
Wiki
Security
Insights
Settings
Force
/
plugins
/
help.py
in
master
 

Tabs

8

No wrap
1
import logging
2
import os
3
from Config import Messages as tr
4
from Config import Config as C
5
from pyrogram import Client, filters
6
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
7
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
8
UPDATES_CHANNEL = C.UPDATES_CHANNEL
9
logging.basicConfig(level=logging.INFO)
10
​
11
@Client.on_message(filters.incoming & filters.command(['start']) & filters.private)
12
async def _start(client, message):
13
    update_channel = UPDATES_CHANNEL
14
    if update_channel:
15
        try:
16
            user = await client.get_chat_member(update_channel, message.chat.id)
17
            if user.status == "kicked":
18
               await client.send_message(
19
                   chat_id=message.chat.id,
20
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/UniversalBotsSupport).",
21
                   parse_mode="markdown",
22
                   disable_web_page_preview=True
23
               )
24
               return
25
        except UserNotParticipant:
26
            await client.send_message(
27
                chat_id=message.chat.id,
28
                text="**Please Join My Updates Channel to use this Bot!**",
29
                reply_markup=InlineKeyboardMarkup(
30
                    [
31
                        [
32
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}")
33
                        ]
34
                    ]
35
                ),
36
                parse_mode="markdown"
37
            )
38
            return
39
        except Exception:
40
            await client.send_message(message.chat.id,
41
                text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
42
                reply_markup=InlineKeyboardMarkup(
43
                    [
44
                        [
45
                           InlineKeyboardButton("Join Updates Channel", url="https://t.me/overdepressive"),
46
                           InlineKeyboardButton("Support Group", url="https://t.me/overdepressive")
47
                      ],
48
                     [
49
                           InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://t.me/dreamfound")
50
                     ]
51
                 ]
52
             ),
53
        parse_mode="markdown",
54
        reply_to_message_id=message.message_id
55
        )
56
            return
@bayuwicita
Commit changes
Commit summary
Create help.py
Optional extended description
Add an optional extended description…
 Commit directly to the master branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
