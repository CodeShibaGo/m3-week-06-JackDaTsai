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

```
pip install Flask-SQLAlchemy pymysql
```

```
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'mysql+pymysql://root:root@localhost:3306/your_db'
```

## Q: Flask-Migrate 如何使用？ #124

```
pip install Flask-Migrate
```

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/your_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
```

```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

```
from sqlalchemy import text

query = text("SELECT * FROM users")

with app.app_context():
    result = db.session.execute(query)
    # 第 1 種方法
    print(result.fetchall())
    # 逐行列印結果
    for row in result:
        print(row)
```

## Q: 如何用土炮的方式建立 Table？ #126

```
with app.app_context(): 
    sql = text("""
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
    )
    """)
    db.session.execute(sql)
    db.session.commit()

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129

- [文件](https://werkzeug.palletsprojects.com/en/3.0.x/utils/)

```
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hash_password(password)
    
    def verify_password(self, password):
        return check_password(self.password_hash, password)
```

```
from user_model import User

new_user = User('john_doe', 's3cr3t')

print(new_user.verify_password('s3cr3t'))  # Should print True
print(new_user.verify_password('wrong_password'))  # Should print False
```
