# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21034333"))
    API_HASH = getenv("API_HASH", "c407a29c33d9ddadd47a6d0793e5c00c")
    BOT_TOKEN = getenv("BOT_TOKEN", "7185273377:AAFuEuNW1hDFs_G2vEhuGYqdD0eNUhD8ObU")
    FSUB = getenv("FSUB", "mnbots")
    CHID = int(getenv("CHID", "-1002116310726"))
    SUDO = list(map(int, getenv("SUDO", "1892771262").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Love:Love@cluster0.n5tifx9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
