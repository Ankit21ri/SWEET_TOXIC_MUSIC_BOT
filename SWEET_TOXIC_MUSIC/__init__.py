from SWEET_TOXIC_MUSIC.core.bot import Ritik
from SWEET_TOXIC_MUSIC.core.dir import dirr
from SWEET_TOXIC_MUSIC.core.git import git
from SWEET_TOXIC_MUSIC.core.userbot import Userbot
from SWEET_TOXIC_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Ritik()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
