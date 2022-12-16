import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5871159415:AAEmdLPpLY_8maR5xPCMCR3GIVg9-tFBqVs")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "overdepressive")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://wlsokvlw:iXaEM2r2BjhK5GcOXGm2qJWotsCjChR0@floppy.db.elephantsql.com/wlsokvlw")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", "24515526" )
  API_HASH = os.environ.get("API_HASH", "482182f8ab9dd82fb9144a0f68eeb817")
  # Sudo users( goto @JVToolsBot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1947738686").split()))
  SUDO_USERS.append(1947738686)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
  
      SC_MSG = "**Halo [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Halo [{}](tg://user?id={})\n\nAgar dapat menggunakan NekoPoi Bot\nanda diharuskan untuk bergabung di channel NekoPoi terlebih dahulu.\nJika sudah bergabung klik /start**"
