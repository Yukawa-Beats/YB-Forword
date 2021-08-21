import os
from config import Config

class Translation(object):
  START_TXT = """<b>ഹായ്🙋🏻‍♂️ {}!!</b>

<b>ഞാൻ ഒരു ഓട്ടോ ഫയൽ ഫോർവേഡ് ബോട്ട് ആണ്..🥳

എന്നെ ഉണ്ടാക്കിയത് @chekuthan_0405 ആണ്😎

ഒരു പബ്ലിക് ചാനലിലെ ഫയല്സിനെ നിങ്ങളുടെ ചാനലിലേക്ക് ഓട്ടോമാറ്റിക് ആയി ഫോർവേഡ് ചെയ്യാൻ സാധിക്കും🤩

For More Details Hit 👉 /help

Join This Channel 👉 @ybdemochannel</b>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Follow These Steps!!</b>

<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>

<b>• Then give admin permission in your personal telegram channel</b>

<b>• Then send any message In your personal telegram channel</b>

<b>• Then use /run command in your bot</b>

<b><u>Available Command</b></u>

* /start - <b>Bot Alive</b>

* /help - <b>more help</b>

* /run - <b>start forward</b>

* /about - <b>About Me</b>"""
  ABOUT_TXT = """<b><u>📃My Info</b></u>

<b>🤖Name :</b> <code>Auto Forward Bot</code>

<b>👨‍🎓Credit :</b> <code>Dark Angel And Yukawa Beats</code>

<b>🎙️Language :</b> <code>Python3</code>

<b>📚Lybrary :</b> <code>Pyrogram v1.2.9</code>

<b>🛑Server :</b> <code>Heroku</code>

<b>📱Build :</b><code>V0.1</code>"""
