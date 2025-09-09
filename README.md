# SnipBox – API with Django REST & JWT

SnipBox is a simple backend API for saving short text snippets with tags, built using **Django REST Framework**, **JWT Authentication**, and **PostgreSQL**. It supports CRUD operations for snippets, tag grouping, and user-based access control.

## Features

- JWT authentication (`/api/token/`)
- Create/update/delete snippets
- Group snippets with reusable tags
- Filter snippets per user
  
---

## Clone the Repository

```bash
git clone https://github.com/Ranjithr-007/Snipbox.git
cd snipbox
```

## Create env

Create a .env file in the root directory

```
snipbox/
├── snippets/           # App for snippet logic
├── snipbox/            # Main Django project
├── requirements.txt
├── .env
├── README.md

```
