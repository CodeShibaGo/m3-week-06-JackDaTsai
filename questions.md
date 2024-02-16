# Questions

## Q: 使用 `virtualenv` 建立虛擬環境 #116

- python -m venv .venv

## Q: python-dotenv 如何使用？ #119

Install python-dotenv
```
pip install python-dotenv
```

Create a `.env` file
```
DATABASE_URL=your_database_url
API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

Load and read variables from the `.env` file
```
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

print(database_url, api_key, secret_key)
```

## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129