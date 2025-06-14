# 🐟 QA Project – FishingBooker (Manual & Automated Testing)

**Author**: Marina Jakovljević  
**Date**: June 2025  
**Role**: Junior QA Engineer  
**Tools**: Python, Selenium, PyTest, Chrome DevTools, Markdown  
**Status**: In Progress  
**Type**: Manual & Automated Functional UI Testing (no login required)  

---

## 🌐 Website Under Test  
[https://fishingbooker.com](https://fishingbooker.com)

> ⚠️ This project is for educational purposes only. It is based on publicly available pages of the FishingBooker website. 

---

## 📁 Project Structure

* **Manual Test Cases** – written in Markdown, located at:  
  `manual/test_cases_manual.md`
* **Automated Tests** – using Page Object Model (POM) with Selenium and PyTest:
  * `base_pages/` — Page classes representing site pages  
  * `test_cases/` — Test scripts using the page classes  
* **Configuration** – PyTest config file: `conftest.py`  
* **Requirements** – Python dependencies listed in `requirements.txt`  
* **Documentation** – Project overview and instructions in this `README.md`  

---

## Technology

* **Language:** Python 3.12  
* **Automation Framework:** Selenium WebDriver, PyTest  
* **Browser:** Google Chrome (Version 137)  
* **Manual Testing Tools:** Markdown, Chrome DevTools  
* **Version Control:** Git & GitHub  
* **IDE:** PyCharm  

---

## Automated Testing (Selenium + POM)

The automation part of the project uses the Page Object Model (POM) design pattern with Selenium WebDriver and PyTest.

- `base_pages/` folder defines web pages as a Python class.  
- `test_cases/` folder includes test scripts that use the page classes.  
- Tests simulate real user flows like searching, User Logging, and clicking.

### ✅ Sample Automated Test Scenario:
- Search for a valid destination (e.g. “Belgrade”)  
- Verify charter cards appear  
- Check that prices are displayed  

---

## How to Run Automated Tests

1. Clone the repository

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run tests (e. g. `test_search.py`):

   ```bash
   pytest test_cases/test_search.py
   ```

---
