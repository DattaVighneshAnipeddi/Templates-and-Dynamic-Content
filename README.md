
## 📌 Task 3 – Templates and Dynamic Content (Flask + Jinja2)

### 🎯 Objective

This task helps you understand how to create **dynamic web pages** using Flask templates and the Jinja2 templating engine.

You will learn:

* What templates are and why we use them
* How Jinja2 template syntax works
* How to pass data from Flask (Python) to HTML
* How to create reusable template components using **template inheritance**

---

## 📂 Project Structure

```
FlaskProject/
│
├─ app.py
└─ templates/
   ├─ base.html
   ├─ home.html
   ├─ about.html
   └─ components/
      └─ navbar.html
```

---

## 🛠 Step-by-Step Implementation

### 1️⃣ Create Templates Folder

Flask automatically looks for HTML files inside a folder named **templates**.

### 2️⃣ Create Base Template `base.html`

Contains common UI elements like:

* Bootstrap styles
* Navbar
* Footer
* Dynamic blocks (`{% block %}`)

### 3️⃣ Create Reusable Component `navbar.html`

Stored in `templates/components/` and included in the base template using:

```html
{% include "components/navbar.html" %}
```

### 4️⃣ Create Child Templates (`home.html`, `about.html`)

Extend the base layout using:

```html
{% extends "base.html" %}
```

Insert page-specific content inside:

```html
{% block content %} ... {% endblock %}
```

### 5️⃣ Pass Dynamic Data

From Flask (Python) to templates using:

```python
return render_template("home.html", username=username, skills=skills)
```

Access data inside HTML:

```html
<p>Hello, {{ username }}</p>
```

---

## 🚀 Running the Project

1️⃣ Open terminal in project folder
2️⃣ Run the Flask app:

```bash
python app.py
```

3️⃣ Open in browser:

* Home Page → [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* About Page → [http://127.0.0.1:5000/about](http://127.0.0.1:5000/about)

---

## ✨ Example Dynamic Output

* Shows user name dynamically
* Displays skills list using Jinja2 loop

```html
{% for skill in skills %}
<li>{{ skill }}</li>
{% endfor %}
```

---

## ✔ Concepts Covered

| Concept              | Status |
| -------------------- | ------ |
| Templates in Flask   | ✅      |
| Jinja2 Syntax        | ✅      |
| Passing Data to HTML | ✅      |
| Template Inheritance | ✅      |
| Reusable Components  | ✅      |

---

### 🏆 Task Completed!

This project demonstrates clean template structure and dynamic rendering using Flask. You can continue building more pages and components to make your web app richer and more interactive! 😄

---
