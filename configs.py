from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "24314601"))
    API_HASH = getenv("API_HASH", "ede341e2d490a0fad5469866dedf8a95")
    BOT_TOKEN = getenv("BOT_TOKEN", "7368957242:AAHC46iuv8l1x_aFy-HdDZO8vkbfEW-7g-w")
    FSUB = getenv("FSUB", "CinepleX1")
    CHID = int(getenv("CHID", "1001877433573"))
    SUDO = list(map(int, getenv("SUDO", "640617767").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://22duddududdu:22duddududdu@cluster0.acjczor.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
