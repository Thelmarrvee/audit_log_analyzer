# 🔍 Audit Log Analyzer

A Python tool that analyzes system login logs to detect unusual or risky user activity.  
This project demonstrates IT risk detection, log parsing, and automated reporting.

---

## 📌 Features
- ✅ Detects **multiple failed login attempts** (possible brute-force attack).  
- ✅ Flags **out-of-hours logins** (before 07:00 or after 22:00).  
- ✅ Generates a **risk analysis report** in plain text.  
- ✅ Built with **Python 3.12** and designed for easy extension.  

---

## 🛠️ How It Works
1. Place your log file in the project directory (e.g., `system_logs.txt`).  
2. Run the program:  
   ```bash
   python main.py
