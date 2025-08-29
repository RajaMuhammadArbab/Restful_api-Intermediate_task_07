# 📝 Blog API (Django + DRF)

A RESTful API built with **Django REST Framework** demonstrating relational data handling with **Users → Posts → Comments** and **Posts ↔ Tags**.  

Supports nested resources, pagination, search, ordering, and filtering.  

---

## 🚀 Setup Instructions

1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/blog-api.git
   cd blog-api
   ```

2. Create & activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```bash
   python manage.py migrate
   ```

5. Create superuser (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server
   ```bash
   python manage.py runserver
   ```

Server will run on: `http://127.0.0.1:8000/`

---

## 📌 API Endpoints

### 🔹 Users
- **GET** `/api/users/` → List all users
- **GET** `/api/users/{id}/` → Get user with their posts

---

### 🔹 Posts
- **GET** `/api/posts/` → List all posts (supports pagination, search, ordering, filtering)
- **POST** `/api/posts/` → Create new post (requires user)
- **GET** `/api/posts/{id}/` → Retrieve single post with comments & author

---

### 🔹 Comments
- **POST** `/api/posts/{id}/comments/` → Add a comment to a post
- **GET** `/api/posts/{id}/comments/` → List comments for a post

---

### 🔹 Tags
- **GET** `/api/tags/` → List tags
- **POST** `/api/tags/` → Create new tag
- **GET** `/api/tags/{id}/` → Retrieve posts with a tag

---

## ⚡ Bonus Features

### 🔹 Pagination
```http
GET /api/posts/?page=2
```

### 🔹 Search
```http
GET /api/posts/?search=django
```

### 🔹 Ordering
```http
GET /api/posts/?ordering=-created_at
GET /api/posts/?ordering=title
```

### 🔹 Filtering
```http
GET /api/posts/?tags__name=django
```

---

## 📌 Sample Requests & Responses

### 1. Get All Posts
**Request**
```http
GET /api/posts/
```
**Response**
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "My First Post",
      "content": "Hello World",
      "user": {
        "id": 1,
        "username": "admin"
      },
      "tags": [{"id": 1, "name": "django"}],
      "comments": []
    },
    {
      "id": 2,
      "title": "API with DRF",
      "content": "Learning Django REST Framework",
      "user": {
        "id": 2,
        "username": "john"
      },
      "tags": [{"id": 2, "name": "rest"}],
      "comments": [
        {
          "id": 1,
          "content": "Great post!",
          "user": {"id": 3, "username": "alice"}
        }
      ]
    }
  ]
}
```

---

### 2. Create Post
**Request**
```http
POST /api/posts/
Content-Type: application/json

{
  "title": "New Blog Post",
  "content": "This is my blog post content.",
  "user": 1,
  "tags": [1, 2]
}
```

**Response**
```json
{
  "id": 3,
  "title": "New Blog Post",
  "content": "This is my blog post content.",
  "user": {"id": 1, "username": "admin"},
  "tags": [
    {"id": 1, "name": "django"},
    {"id": 2, "name": "rest"}
  ],
  "comments": []
}
```

---

### 3. Add Comment to Post
**Request**
```http
POST /api/posts/1/comments/
Content-Type: application/json

{
  "content": "Nice article!",
  "user": 2
}
```

**Response**
```json
{
  "id": 2,
  "content": "Nice article!",
  "user": {"id": 2, "username": "john"}
}
```

---

### 4. Filter Posts by Tag
**Request**
```http
GET /api/posts/?tags__name=django
```

**Response**
```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "title": "My First Post",
      "content": "Hello World",
      "tags": [{"id": 1, "name": "django"}],
      "user": {"id": 1, "username": "admin"},
      "comments": []
    }
  ]
}
```

---

## PROJECT-DEMO ##

## 1 ##
<img width="1395" height="707" alt="1" src="https://github.com/user-attachments/assets/a40f51cb-1f4c-41b1-9f3b-4b8131c2314a" />
## 2 ##
<img width="1384" height="770" alt="2" src="https://github.com/user-attachments/assets/df12df5f-09c0-445d-86cd-7915f41e17cd" />
## 3 ##
<img width="1378" height="489" alt="3" src="https://github.com/user-attachments/assets/4022147b-6507-407e-a82d-775f998086e9" />
## 4 ##
<img width="1456" height="883" alt="4" src="https://github.com/user-attachments/assets/1230b1ac-17b4-4353-a7da-d015fc3f07e3" />
## 5 ## 
<img width="1444" height="901" alt="5" src="https://github.com/user-attachments/assets/551853c5-14e4-4d38-8429-d4a07bf05514" />
## 6 ##
<img width="1426" height="739" alt="6" src="https://github.com/user-attachments/assets/941b7892-9666-444c-a516-fb649c2f78b9" />
## 7 ## 
<img width="1449" height="887" alt="7" src="https://github.com/user-attachments/assets/c8587935-bbdb-4ae3-9916-c91c372d36e0" />
## 8 ## 
<img width="1448" height="532" alt="8" src="https://github.com/user-attachments/assets/036b60bc-175e-4cab-a9c9-5d5deb229080" />
## 9 ## 
<img width="1439" height="505" alt="9" src="https://github.com/user-attachments/assets/d89e38e1-9955-4bc6-9a8b-5bda483ecada" />
## 10 ## 
<img width="1441" height="563" alt="10" src="https://github.com/user-attachments/assets/a3a5a339-d951-4121-a362-61f26587f22c" />
## 11 ## 
<img width="1439" height="863" alt="11" src="https://github.com/user-attachments/assets/e665459b-c887-4191-920f-8af30982877e" />
## 12 ##
<img width="1441" height="800" alt="12" src="https://github.com/user-attachments/assets/8d881108-4793-4288-84d4-bb2a86672abe" />
## 13 ## 
<img width="1439" height="825" alt="13" src="https://github.com/user-attachments/assets/855a3465-500d-45b7-ab27-e1ef52f39117" />
## 14 ##
<img width="1443" height="811" alt="15" src="https://github.com/user-attachments/assets/7865afdb-2471-4719-a41a-ed7fced6d320" />
## 15 ## 
<img width="1438" height="843" alt="16" src="https://github.com/user-attachments/assets/400530fd-71ac-4651-b904-70db0f1de726" />
## 16 ## 
<img width="1439" height="808" alt="17" src="https://github.com/user-attachments/assets/ca352880-2bb6-4e56-b2f9-8b26e932b382" />
## 17 ##
<img width="1445" height="804" alt="18" src="https://github.com/user-attachments/assets/f3c4dbf0-3fe3-4a29-9587-29caf65c7662" />
