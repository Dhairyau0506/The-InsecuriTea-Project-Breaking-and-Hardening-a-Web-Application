# The-InsecuriTea-Project-Breaking-and-Hardening-a-Web-Application
**InsecuriTea**
**Let's get to penTasting.**

InsecuriTea is a Flask-based web application built using Python and SQLite to demonstrate real-world web vulnerabilities and their fixes. The app allows users to register, log in, and manage their tea preferences.

**🚀 This project is divided into two phases:**

- Phase 1: Vulnerable application (InsecuriTea)
- Phase 2: Secure implementation (SecuriTea mode – still in development)

--------------------------------------------------

**✨ Features:**

- User registration and login system
- Tea preference dashboard
- Admin panel with user listing
- Detailed user view for admin
- SQLite database integration
- Simple HTML/CSS frontend
- Planned secure/insecure mode switch
- A Hacker's Playground: Pre-built attack payloads for hands-on exploitation practice 

--------------------------------------------------

**⚠️ Phase 1: InsecuriTea (Vulnerable Mode)**

This mode intentionally contains OWASP Top 10 vulnerabilities for learning and exploitation.

**Vulnerabilities included:**

- SQL Injection (SQLi)
- Unsafe query construction
- Allows authentication bypass
- Cross-Site Scripting (XSS)
- Unsanitized user input rendering
- Allows script execution in browser
- Insecure Direct Object Reference (IDOR)
- Direct access using user_id in URL
- No authorization checks

Let me show y'all some sample attacks:

**1. SQL Injection (SQLi) : A03: Injection**
<img width="1342" height="703" alt="image" src="https://github.com/user-attachments/assets/6e6c658e-0e80-4630-b505-cf82cc63013c" />
- Demonstrates login bypass using SQLi

**2. Cross-Site Scripting (XSS) : A03: Injection**

- Unsanitized user input rendered directly
- Stored XSS via notes field

Scenario - Stored XSS used for privilege escalation via session hijacking:
(i) Attacker creates an account and injects a script which steals cookie:
<img width="682" height="977" alt="Screenshot 2026-03-27 191548" src="https://github.com/user-attachments/assets/178eac88-1dbf-49cc-bc35-fbdea50b683c" />

(ii) Admin access the admin panel and review the details of the account created by the hacker (here: john):
<img width="1152" height="606" alt="image" src="https://github.com/user-attachments/assets/d9fd67f2-469c-4e33-8f8f-f5b6948c563b" />

--------------------------------------------------

**🛠 Tech stack:**

- Backend: Python (Flask)
- Database: SQLite
- Frontened: HTML, CSS

--------------------------------------------------

## How to Run

1. Clone the repository

```bash
git clone https://github.com/dhairya-techsec/The-InsecuriTea-Project-Breaking-and-Hardening-a-Web-Application.git
```

2. Navigate into the project folder

```bash
cd The-InsecuriTea-Project-Breaking-and-Hardening-a-Web-Application
```

3. (Optional) Create a virtual environment

```bash
python -m venv venv
```

Activate it:

- Windows:
```bash
venv\Scripts\activate
```

- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install flask
```

5. Run the application

```bash
python app.py
```

6. Open in browser

```text
http://127.0.0.1:5000
```

---

- Ensure an admin user exists before testing admin functionalities  
- You can manually insert an admin record into the database (`users.db`) if not present  
- Example: create a user with username `admin` for testing purposes  

## 🔑 Admin Access (for testing)

```text
http://127.0.0.1:5000/admin?username=admin
```


--------------------------------------------------

##🧪 Testing Notes

- The database (users.db) is created automatically on first run  
- Register a user and inject payloads to test vulnerabilities  
- Use the admin panel to trigger stored XSS and other attacks

--------------------------------------------------

## 🔐 Phase 2: SecuriTea (Secure Mode)

SecuriTea is the hardened version of the application, where all previously exploited vulnerabilities are mitigated using secure coding practices. The application supports a **toggle-based mode switch**, allowing users to dynamically switch between insecure (InsecuriTea) and secure (SecuriTea) environments.

---

### ✅ Security Improvements Implemented

#### 1. SQL Injection Prevention
- Replaced dynamic query construction with **parameterized queries**
- Prevents authentication bypass and database manipulation

**Before (Vulnerable):**
```python
"SELECT * FROM users WHERE username = '" + username + "'"
```

**After (Secure):**
```python
cursor.execute(
    "SELECT id, username FROM users WHERE username=? AND password=?",
    (username, password)
)
```

---

#### 2. Cross-Site Scripting (XSS) Prevention
- Removed unsafe rendering (`| safe`) in secure mode
- Ensured all user inputs are properly escaped before rendering

**Impact:**
- Prevents execution of malicious scripts
- Protects user sessions and browser integrity

---

#### 3. IDOR (Insecure Direct Object Reference) Fix
- Removed reliance on `user_id` from URL parameters
- Implemented **session-based access control**

**Before (Vulnerable):**
```text
/dashboard?user_id=1
```

**After (Secure):**
- User identity is derived from server-side session
- Unauthorized access to other users’ data is blocked

---

#### 4. Secure Authentication & Authorization
- Introduced **session management using Flask sessions**
- Restricted admin panel access to authenticated admin users only

**Enhancements:**
- Prevents unauthorized admin access
- Eliminates URL-based privilege escalation

---

#### 5. Admin Protection Improvements
- Prevented admin from deleting their own account
- Enforced strict role-based checks for admin functionality

---

### 🔄 Mode Switching Feature

The application includes a **live toggle system**:

<img width="1372" height="629" alt="image" src="https://github.com/user-attachments/assets/2884a07f-2790-47d5-a15d-dfe3a4621ecc" />


- 🔴 Insecure Mode → Demonstrates vulnerabilities  
- 🟢 Secure Mode → Demonstrates mitigations  

This allows:
- Side-by-side comparison of attacks vs defenses  
- Better understanding of real-world exploitation and prevention  

---

### 🎯 Key Takeaway

SecuriTea transforms the application from a vulnerable system into a **secure-by-design implementation**, demonstrating how real-world vulnerabilities can be effectively mitigated using best practices.

This dual-mode architecture makes the project both a **learning tool for attackers** and a **reference for secure development**.


--------------------------------------------------

## 👑 Admin Panel & Default Admin Account

The application includes a dedicated **Admin Panel** that allows administrative users to manage and view all registered users in the system.

---

### 🔐 Admin Panel Features

- View all registered users
- Access detailed user information
- Delete user accounts (with restrictions)
- Demonstrate privilege escalation risks (in insecure mode)

---

### 🧑‍💻 Default Admin Account Creation

To simplify testing and ensure consistent access, the application automatically creates an **admin account** during database initialization.

This is handled in the backend when the database is first set up.

**Default Admin Credentials:**

```text
Username: admin
Password: admin123
```

---

### ⚙️ How It Works

- On application startup, the database is initialized  
- The system checks whether an admin user already exists  
- If not, it automatically inserts a default admin record  

This ensures:
- Admin functionality is always accessible  
- No manual database setup is required  

---

### 🔓 Insecure Mode Behavior

- Admin access is controlled via URL parameter:
```text
/admin?username=admin
```
- No proper authentication checks  
- Vulnerable to privilege escalation  

---

### 🔐 Secure Mode Behavior

- Admin access is restricted using **session-based authentication**
- Only logged-in users with username `admin` can access the panel  
- Unauthorized users are redirected or denied access  

---

### 🛡️ Security Enhancements

- Prevented admin from deleting their own account  
- Enforced role-based access control  
- Eliminated URL-based authentication flaws  

---

### 🎯 Learning Value

This module demonstrates:
- The risks of improper authentication  
- The importance of role-based access control  
- Real-world privilege escalation scenarios and their mitigation

---

**🎯 Learning outcomes:**

- Understanding OWASP Top 10 vulnerabilities
- Hands-on exploitation of SQLi, XSS, and IDOR
- Applying secure coding practices
- Bridging development and penetration testing

--------------------------------------------------

**⚠️ Disclaimer:**

This project is intentionally vulnerable in Phase 1 and is for educational purposes only. Do not deploy it in production.

--------------------------------------------------

**👨‍💻 Author:**

Dhairya Upadhyay
Aspiring Cybersecurity & Pentesting Practitioner
