---

# QA Test Cases – FishingBooker

**Author**: Marina Jakovljević   

This document contains a list of manually written test cases for the FishingBooker website as part of a junior QA job application. 

- Written in Markdown format
- Focused on core website features (search, filters, booking, responsive design)
- Tested using Google Chrome (Version 137.0.7151.104 / desktop & mobile view)

## Website
[https://fishingbooker.com](https://fishingbooker.com)


## File Contents
- `test_cases_manual.md`: Test cases with steps and expected results
- This file is part of a QA portfolio and demonstrates my ability to write structured manual test cases for a real-world web application.

## Test Environment
- OS: Windows 10
- Browser: Google Chrome 137.0.7151.104
- Device: Desktop & Mobile (responsive simulation via Chrome DevTools)

---

## Scope
These test cases cover the basic functionalities of the FishingBooker website for a non-logged-in user, including destination search, boat display, links, and filters.

---

- **Preconditions**: No Login Required.

---

## 📋 Test Cases

| Test Case ID | Test Name                      | Steps                                                                     | Expected Result                                | Status |
|--------------|--------------------------------|--------------------------------------------------------------|------------------------------------------------------------------|--------|
| TC001        | Search Valid Destination       | 1. Go to https://fishingbooker.com<br>2. In search input enter "Miami"<br>3. Click the search button         | List of boats in Miami appears with relevant offers             | Pass   |
| TC002        | Search Invalid Destination       | 1. Go to https://fishingbooker.com<br>2. Enter random string "asdfgh123"<br>3. Click the search button         | "No results found" message is shown or no listings displayed               | Pass   |
| TC003        | Search With Empty Field        | 1. Go to homepage<br>2. Leave the search input empty<br>3. Click the search button              | Error message or nothing happens, user stays on same page       | Pass   |
| TC004        | Click on Top Destination Card   | 1. Go to homepage<br>2. Scroll down to "Exciting fishing destinations close to you" <br>3. Click on a destination card (e.g. "Belgrade")                 | Destination details page opens with available charters            | Pass   |
| TC005        | Search with Date & Passengers (Unauthenticated User)| 1. Open the FishingBooker homepage.<br>2. In the destination field, type and select “Croatia.”<br>3. Set the date to June 18.<br>4. Set the number of people to 2 adults.<br>5. Click on "Check availability".| A list of available charters is displayed, and the total number of results (e.g., 62 available charters) is shown. | Pass   |
| TC006        | Filter Search Results by Lowest Price| 1. Open the FishingBooker homepage.<br>2. In the destination field, type and select “Croatia.”<br>3. Set the date to June 18.<br>4. Set the number of people to 2 adults.<br>5. Click on "Check availability". <br>6. From the results page, click on the "Lowest price".| Search results are updated and sorted from the lowest to the highest price. | Pass   |
| TC007        | Open the First Charter from the Filtered List| 1. Open the FishingBooker homepage.<br>2. In the destination field, type and select “Croatia.”<br>3. Set the date to June 18.<br>4. Set the number of people to 2 adults.<br>5. Click on "Check availability". <br>6. From the results page, click on the "Lowest price". <br>7. On the first charter listed (e.g. "Lonjsko Polje Lodge and Boats") click "See availability".| Charter details page opens and availability is shown for the selected date. | Pass   |
| TC008        | Verify That the Reservation Form Opens| 1. Open the FishingBooker homepage.<br>2. In the destination field, type and select “Croatia.”<br>3. Set the date to June 18.<br>4. Set the number of people to 2 adults.<br>5. Click on "Check availability". <br>6. From the results page, click on the "Lowest price". <br>7. On the first charter listed (e.g. "Lonjsko Polje Lodge and Boats") click "See availability". <br>8. On charter detail page, click on “Select your trip.” <br>9. Click on the “Reserve” button.| A reservation form opens below or in a new modal/window. | Pass   |
| TC009        | Attempt to Reserve a Trip with Empty Form (Unauthenticated User)| 1. Open the FishingBooker homepage.<br>2. In the destination field, type and select “Croatia.”<br>3. Set the date to June 18.<br>4. Set the number of people to 2 adults.<br>5. Click on "Check availability". <br>6. From the results page, click on the "Lowest price". <br>7. On the first charter listed (e.g. "Lonjsko Polje Lodge and Boats") click "See availability". <br>8. On charter detail page, click on “Select your trip.” <br>9. Click the “Reserve” button.  <br>10. Without filling in any form fields, click Continue. | Form is not submitted. Error messages are displayed indicating that required fields are empty (e.g., name, email, phone number). The user remains on the same page. | Pass   |
| TC010        | Login Attempt with Invalid Email Format| 1. Open the FishingBooker homepage.<br>2. Click on the “Log In” button. <br>3. In the Email field, enter an invalid email address (e.g., testmail.com, without @)  <br>4. Click the “Continue with email” button.  | The system displays an error message such as: "Please enter a valid email address." <br>The user is not logged in and remains on the login page.       | Pass   |
| TC011        | Sign Up Attempt with All Fields Left Empty| 1. Open the FishingBooker homepage.<br>2. Click on the “Sign Up” button. <br>3. Leave all fields (Full Name, Email, Password, etc.) empty.  <br>4. Click the “Sign Up” button.  | The system displays error messages for each required field, such as: "Full Name / Email / Password is required"<br>The account is not created.<br>The user remains on the sign-up page.      | Pass   |
| TC012        | Responsive Design on Mobile| 1. Open developer tools. <br>2. Switch to iPhone 12 Pro view. <br>3. Observe the layout. | Layout is adapted to screen; nothing overlaps or breaks visually. <br>Fonts and buttons adjust properly.| Pass   |
| TC013        | Verify hamburger menu functionality on mobile view| 1. Open developer tools. <br>2. Open the site in mobile view. <br>3. Click on the hamburger menu (three bars) in the top right corner.  <br>4. Check if menu options are displayed.  <br>5. Tap on any menu item (e.g., “Help Center”).|Menu expands on tap. <br> Menu items are visible and clickable. <br> Navigation works correctly.| Pass   |
| TC014        | Verify breadcrumb navigation on charter detail page| 1. Open any charter detail page. <br>2. Look for breadcrumb (Home > Destination > Charter name).<br>3. Click on each breadcrumb item one by one (e.g., "Croatia", "Kaštel Kambelovac", etc.). |Each breadcrumb link navigates to the correct corresponding page. <br> The current page (e.g., Fishing adventure by CUP of SEA) is not clickable (or styled as active).| Pass   |
| TC015        | Filter by Trip Type            | 1. Go to homepage  <br>2. Scroll down to "Top fishing techniques" <br>3. Click on a trip type filter (e.g. "Deep Sea Fishing")       | Results get filtered based on selected trip type                | Pass   |
| TC016        | Check Footer Links             | 1. Scroll to page bottom<br>2. Click on "About us", "Blog", or "Privacy Policy" links     | Corresponding pages open correctly in the same or new tab       | Pass   |
| TC017        | Check Social Media Icons| 1. Scroll to page bottom<br>2. Click on Social Media Icons     | Each link opens correct page in same or new tab       | Pass   |
| TC018        | Contact Support| 1. Go to footer. <br> 2. Click “Help Center”.|Contact page appears.| Pass   |
| TC019        | Verify Currency Change via Dropdown Menu| 1. Open the FishingBooker homepage.<br>2. Locate the currency selector dropdown (in the footer). <br>3. Click the dropdown and select a different currency (e.g. USD).  <br>4. Navigate to any fishing trip listing.  <br>5. Observe the price display format. | After selecting USD, all prices on the site should be displayed in USD ($). | Pass   |
| TC020        | Verify Language Change on the Website| 1. Open the FishingBooker homepage.<br>2. Locate and click on the language selector.<br>3. Select another language (e.g. Deutsch)| After selection, the interface text updates immediately to the chosen language. <br>All main site elements (menu, buttons, headings, filters) are translated.  <br> City names and place names remain unchanged as expected. | Pass   |

---

## **Top Priorities – HIGH** (critical for the basic site functionality)

| TC    | Name                          | Why it’s HIGH                                                   |
| ----- | ----------------------------- | --------------------------------------------------------------- |
| TC001 | Search Valid Destination      | Core site function – without it, the site has no purpose.       |
| TC002 | Search Invalid Destination    | Important for negative testing – system must handle no results. |
| TC003 | Search With Empty Field       | Must handle error – UX + security.                              |
| TC005 | Apply filters to search results           | Combination of multiple filters – core business.                |
| TC006 | Filter by Lowest Price        | Important for user experience and filter performance.           |
| TC009 | Attempt to Reserve Empty Form | Important for validation and preventing empty reservations.     |
| TC010 | Login with Invalid Email      | Important for security and input validation.                    |
| TC011 | Sign Up with Empty Fields     | Same – validation and security.                                 |
| TC008 | Verify Reservation Form Opens | Key step for a successful reservation.                          |

---

## **Medium Priority – MEDIUM**

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

## **Low Priority – LOW**

| TC    | Name                     |
| ----- | ------------------------ |
| TC016 | Check Footer Links       |
| TC017 | Check Social Media Icons |
| TC018 | Contact Support          |

---


📌 *Note: This test suite does not require login and simulates a basic user journey from search to booking without authentication.*

