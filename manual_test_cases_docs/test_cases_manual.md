# QA Test Cases – FishingBooker

**Author**: Marina Jakovljević   

This document contains a list of manually written test cases for the FishingBooker website as part of a junior QA job application. 

- Written in Markdown format  
- Focused on core website features (search, filters, booking, responsive design)   

## Website  
[https://fishingbooker.com](https://fishingbooker.com)

## File Contents  
- `test_cases_manual.md`: Test cases with steps and expected results  
- This file is part of a QA portfolio and demonstrates my ability to write structured manual test cases for a real-world web application.

## Test Environment  
- **OS**: Windows 10  
- **Browser**: Google Chrome 137.0.7151.104  
- **Device**: Desktop & Mobile (responsive simulation via Chrome DevTools)  

---

## Scope  
These test cases cover the basic functionalities of the FishingBooker website for a non-logged-in user, including destination search, boat display, links, and filters.

---

**Preconditions**: No Login Required.

---

## 📋 Test Cases

| Test Case ID | Test Name | Steps | Expected Result | Status |
|--------------|-----------|-------|------------------|--------|
| TC001 | Search Valid Destination | 1. Go to https://fishingbooker.com<br>2. Enter "Miami"<br>3. Click Search | List of boats in Miami appears | Pass |
| TC002 | Search Invalid Destination | 1. Enter "asdfgh123"<br>2. Click Search | "No results found" message shown | Pass |
| TC003 | Search With Empty Field | 1. Leave search input empty<br>2. Click Search | Error message or no action | Pass |
| TC004 | Click on Top Destination Card | 1. Scroll to “Exciting fishing destinations…”<br>2. Click destination (e.g. "Belgrade") | Destination page opens | Pass |
| TC005 | Search with Date & Passengers | 1. Enter “Croatia”<br>2. Set date: June 18<br>3. 2 adults<br>4. Click "Check availability" | List of charters with count shown | Pass |
| TC006 | Filter Search Results by Lowest Price | Same as TC005 + Click "Lowest price" | Results sorted from lowest to highest | Pass |
| TC007 | Open the First Charter | Follow TC006 + Click "See availability" | Charter detail page opens | Pass |
| TC008 | Verify Reservation Form Opens | Follow TC007 + Click “Select your trip” → “Reserve” | Reservation form opens | Pass |
| TC009 | Reserve With Empty Form | Follow TC008 + Click Continue without input | Error messages shown, no submission | Pass |
| TC010 | Login with Invalid Email | 1. Click “Log In”<br>2. Enter invalid email (e.g. testmail.com)<br>3. Click Continue | Error message shown | Pass |
| TC011 | Sign Up With Empty Fields | 1. Click “Sign Up”<br>2. Leave all fields empty<br>3. Click Sign Up | Error messages shown, no account created | Pass |
| TC012 | Responsive Design on Mobile | Use DevTools → iPhone 12 Pro view | Layout adjusts, no visual breaks | Pass |
| TC013 | Hamburger Menu Functionality | Mobile view → Tap hamburger menu → Tap item | Menu expands, items clickable, nav works | Pass |
| TC014 | Breadcrumb Navigation | Open charter page → Click breadcrumbs | Each leads to correct page, current is non-clickable | Pass |
| TC015 | Filter by Trip Type | Homepage → “Top fishing techniques” → Click a filter | Results filtered accordingly | Pass |
| TC016 | Check Footer Links | Scroll down → Click "About us", "Blog", etc. | Pages open correctly | Pass |
| TC017 | Check Social Media Icons | Click icons in footer | Social media pages open | Pass |
| TC018 | Contact Support | Footer → Click “Help Center” | Help page opens | Pass |
| TC019 | Verify Currency Change | Footer → Select USD → Open any listing | Prices shown in USD | Pass |
| TC020 | Verify Language Change | Select Deutsch from language menu | Site updates language (except place names) | Pass |

---

## 🔥 **Top Priorities – HIGH** (critical for the basic site functionality)

| TC    | Name                          | Why it’s HIGH |
| ----- | ----------------------------- | ------------- |
| TC001 | Search Valid Destination      | Core site function |
| TC002 | Search Invalid Destination    | Negative test handling |
| TC003 | Search With Empty Field       | UX + validation |
| TC005 | Apply filters to search results | Real-world scenario |
| TC006 | Filter by Lowest Price        | UX filter importance |
| TC009 | Attempt to Reserve Empty Form | Required field validation |
| TC010 | Login with Invalid Email      | Security & input validation |
| TC011 | Sign Up with Empty Fields     | Same as above |
| TC008 | Verify Reservation Form Opens | Reservation flow |

---

## 🟡 **Medium Priority – MEDIUM**

| TC    | Name                         |
| ----- | ---------------------------- |
| TC004 | Click Top Destination Card   |
| TC007 | Open First Charter           |
| TC012 | Responsive Design            |
| TC013 | Hamburger Menu Functionality |
| TC014 | Breadcrumb Navigation        |
| TC015 | Filter by Trip Type          |
| TC019 | Verify Currency Change       |
| TC020 | Verify Language Change       |

---

## 🔵 **Low Priority – LOW**

| TC    | Name                     |
| ----- | ------------------------ |
| TC016 | Check Footer Links       |
| TC017 | Check Social Media Icons |
| TC018 | Contact Support          |

---

📌 *Note: This test suite does not require login and simulates a basic user journey from search to booking without authentication.*
