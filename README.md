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
git clone https://github.com/Dhairyau0506/The-InsecuriTea-Project-Breaking-and-Hardening-a-Web-Application.git
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

**🔐 Phase 2: SecuriTea (Secure Mode – still in development)**

This mode focuses on fixing all vulnerabilities using secure coding practices.

**Planned security improvements:**

- Parameterized queries (prevent SQLi)
- Output escaping (prevent XSS)
- Proper authentication and authorization (prevent IDOR)
- Password hashing instead of plaintext storage
- Input validation and sanitization

--------------------------------------------------

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
