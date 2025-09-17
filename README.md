# 🧩 Software Design Principles with Python

This repository demonstrates how to apply **software design principles
(SOLID, DRY, KISS)** in Python through a simple **Order Processing
System**.\
It also includes **automated tests with pytest** and a **CI/CD workflow
with GitHub Actions**. 🚀

------------------------------------------------------------------------

## 📂 Project Structure

    software-design-principles-python/
    ├─ order.py          # Core classes (Order, Repository, EmailService)
    ├─ tests/
    │   └─ test_order.py # Unit tests with pytest
    ├─ requirements.txt  # Dependencies
    └─ .github/
       └─ workflows/
          └─ ci.yml      # GitHub Actions for CI/CD

------------------------------------------------------------------------

## ⚙️ Setup Instructions

1.  📥 **Clone the repo**\

``` bash
git clone https://github.com/your-username/software-design-principles-python.git
cd software-design-principles-python
```

2.  🐍 **Create a virtual environment (optional but recommended)**\

``` bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

3.  📦 **Install dependencies**\

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Usage

Run the **order system** example:

``` bash
python order.py
```

Expected output:

    💾 Saving order with total 15 to database...
    📧 Email sent for order total: 15

------------------------------------------------------------------------

## 🧪 Running Tests

We use **pytest** to test our design. Run:

``` bash
pytest
```

Output should show all tests passing ✅

------------------------------------------------------------------------

## 🤖 CI/CD Automation

This project includes a **GitHub Actions workflow** (`ci.yml`) that
automatically:\
1. 🏗️ Installs dependencies\
2. 🧪 Runs pytest on every push/pull request\
3. ✅ Ensures code quality before merging

