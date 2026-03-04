# Django Blog Project

## 📌 Project Description

This project is a fully functional blogging platform developed using Django.
It was built progressively to understand Django architecture, authentication, CRUD operations, relational databases, and user interaction features.

The application allows users to register, login, create posts, comment on posts, search content, filter posts by tags, and manage their profiles.

---

## 🚀 Features Implemented

### ✅ Authentication System

* User registration
* Login and logout
* Profile viewing and editing
* Secure password hashing
* CSRF protection

---

### ✅ Blog Post Management (CRUD)

* List all posts
* View individual posts
* Create posts (authenticated users only)
* Edit posts (author only)
* Delete posts (author only)

Permissions were enforced using:

* LoginRequiredMixin
* UserPassesTestMixin

---

### ✅ Comment System

* Display comments under posts
* Authenticated users can add comments
* Authors can edit and delete their comments
* Comments linked to both Post and User

---

### ✅ Search Functionality

Users can search blog posts using:

* Post title
* Post content
* Tags

---

### ✅ Tag Filtering

* Implemented using django-taggit
* Users can click tags to view related posts
* Improves content categorization and navigation

---

### ✅ Pagination

* Limits number of posts displayed per page
* Improves performance and user experience

---

### ✅ User Profile Integration

* Posts linked to user accounts
* Comments linked to authors
* Permission control based on ownership

---

### ✅ UI Styling

* Bootstrap integrated for responsive design
* Improved navigation and form styling

---

## 🏗️ Project Structure

```
django_blog/
│
├── django_blog/              # project configuration
│   ├── settings.py
│   ├── urls.py
│
├── blog/                     # main app
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/blog/
│   └── static/
│
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository

```
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd django_blog
```

### 2️⃣ Create virtual environment (Linux/WSL)

```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install django
pip install django-taggit
```

### 4️⃣ Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start server

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 🔐 Permissions & Security

* Only authenticated users can create posts
* Only post authors can edit or delete posts
* Only comment authors can edit or delete comments
* CSRF protection enabled
* Password hashing handled by Django

---

## 🧪 Testing

The following were tested:

* Authentication workflow
* CRUD operations
* Comment permissions
* Search and tag filtering
* Pagination navigation
* Unauthorized access prevention

---

## 🚀 Deployment

Deployment preparation includes:

* Static file configuration
* Environment variable setup
* Debug disabled in production
* Allowed hosts configuration

Deployment platform may include:

* Render
* Railway
* PythonAnywhere
* Heroku

---

## 📚 Challenges Faced

* URL routing conflicts
* Permission enforcement logic
* Template inheritance issues
* Search filtering optimization
* Tag filtering integration
* Authentication redirect handling

---

## 🎯 Lessons Learned

* Django project structure and architecture
* ORM relationships and query filtering
* Class-based views usage
* Authentication and authorization
* Template inheritance
* Secure form handling
* Debugging Django errors
* Building scalable app features step-by-step

---

## 🔮 Future Improvements

* Image upload for posts
* Rich text editor
* Post likes and reactions
* Email notifications
* REST API integration
* Social authentication
* Advanced profile system

---

## 👨‍💻 Author

**DonnyTerk**

---

## ⭐ Acknowledgment

This project was developed as part of the ALX Django learning lab to practice real-world web development concepts.
