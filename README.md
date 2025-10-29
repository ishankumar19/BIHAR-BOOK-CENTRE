
# 📚 BIHAR BOOK CENTRE – Library Management System

A console-based Library Management System built using **Python** and **MySQL** to manage accounts, books, lending, and order details for a bookstore or library.

---

## 🔧 Features

- ✅ Create, update, delete **library member accounts**
- ✅ Add, view, edit, and delete **book records**
- ✅ **Lend** and **return** books
- ✅ View **lending history** per member
- ✅ **Order** new books and update deliveries
- ✅ View complete **ordering history**
- ✅ Fully menu-driven console interface
- ✅ Uses **MySQL database** for persistent data storage

---

## 🗂️ Modules

| Module          | Functionality                                   |
|-----------------|--------------------------------------------------|
| Account         | Create, view, update, delete member info        |
| Book            | Add, search, update, delete book records        |
| Lending         | Lend books, return them, view lending history   |
| Ordering        | Order books, update delivery, view orders       |

---

## 💻 Technologies Used

- **Python 3.x**
- **MySQL (via `mysql-connector-python`)**
- CLI-based interface (no external UI)
- Designed for terminal/command-line use

---

## ⚙️ Setup Instructions

1. **Install MySQL** and start your MySQL service.
2. **Install Python Dependencies**:
    ```bash
    pip install mysql-connector-python
    ```
3. **Update MySQL Credentials** in the script:
    ```python
    mycon = sql.connect(host="localhost", user="root", passwd="your_password")
    ```
4. **Run the script**:
    ```bash
    python library_management_system.py
    ```

---

## 🏗️ Database Structure

### `library_master`
| Field         | Type         |
|---------------|--------------|
| cardno        | VARCHAR(10) PRIMARY KEY |
| name_of_person| VARCHAR(30) |
| phone_no      | VARCHAR(15) |
| address       | VARCHAR(100) |
| DOB           | DATE        |

### `book`
| Field     | Type         |
|-----------|--------------|
| name      | VARCHAR(50) |
| no        | VARCHAR(5) PRIMARY KEY |
| genre     | VARCHAR(30) |
| author    | VARCHAR(50) |
| language  | VARCHAR(30) |

### `lend`
| Field         | Type         |
|---------------|--------------|
| cardno        | VARCHAR(10) |
| name_of_book  | VARCHAR(50) |
| lend_date     | DATE        |
| return_date   | DATE        |

### `order_book`
| Field         | Type         |
|---------------|--------------|
| order_no      | VARCHAR(10) PRIMARY KEY |
| book_name     | VARCHAR(50) |
| delivery_date | DATE        |
| price         | INT         |

---

---

## ✍️ Author

**Ishant kumar**  
📧 Email: [ishansingh196055@gmail.com](mailto:ishansingh196055@gmail.com)  
🌐 GitHub: [@ishankumar19](https://github.com/ishankumar19)  
🔗 LinkedIn: [Ishant Kumar](https://www.linkedin.com/in/ishant-kumar-b2b78b388/)

