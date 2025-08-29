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

