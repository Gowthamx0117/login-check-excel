# 🔐 Flask Login & Registration with Excel Database

A beginner-friendly Flask web app that allows users to **register** and **log in**, storing their credentials in an **Excel (.xlsx)** file instead of a traditional database.

---

## 📁 Project Structure

```
login_app/
│
├── app.py
├── users.xlsx  ← (auto-created and updated)
└── templates/
    ├── login.html
    ├── register.html
    ├── success.html
    ├── failure.html
    └── register_success.html
```

---

## 🚀 Features

- ✅ Login with username and password
- ✅ Register new users
- ✅ Prevent duplicate usernames
- ✅ Append new users to Excel file
- ✅ Basic frontend using HTML templates

---

## 🛠️ Requirements

Install dependencies:

```bash
pip install flask pandas openpyxl
```

---

## 🏃 How to Run

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📘 Sample `users.xlsx` Format

| username | password |
|----------|----------|
| user1    | pass1    |
| user2    | pass2    |

*(Automatically created and updated as users register)*

---

## 💡 Next Steps

- 🔐 Add password hashing with bcrypt
- 📊 Log login attempts
- 🛢️ Migrate to SQLite or MySQL
- ☁️ Deploy using Render or Heroku

---

## 🙋‍♂️ Made By

A passionate student learning full-stack development using Flask + Excel!

---

## 📃 License

This project is open-source and free to use under the [MIT License](LICENSE).
