# Nexus Creative Agency - Multi-Page Website Conversion

A fully responsive, multi-page web application built for a creative agency. This project demonstrates modular web design by separating structural content, universal UI styling, and back-end routing architectures.

---

## 📂 Project Architecture & File Structure

The project strictly follows standard framework structural configurations:

* **`app.py`** - The core Python/Flask back-end routing engine handling application pathways.
* 📂 **`static/`**
    * **`style.css`** - Global CSS stylesheet managing design variables, grid systems, and flexbox configurations.
* 📂 **`templates/`**
    * **`base.html`** - Master layout template containing the universal navigation bar structure.
    * **`home.html`** - Core landing page featuring the hero banner section.
    * **`about.html`** - Agency profile segment using a clean two-column flexbox layout.
    * **`services.html`** - Dynamic CSS grid containing interactive service offering cards.
    * **`gallery.html`** - Visual portfolio array arranged in an auto-fitting image wall.
    * **`contact.html`** - Client intake communication form with custom input control styling.
    * **`login.html`** / **`register.html`** - Protected portal access gateway frames.

---

## 🚀 How to Run and View the Project

This project supports two execution modes depending on your local network/environment security permissions:

### Option 1: Direct Prototype Preview (Recommended for Quick Evaluation)
To bypass local machine network loops, firewalls, or port restrictions:
1. Navigate into the `templates/` directory.
2. Double-click **`home.html`** to launch the site directly inside any modern web browser.
3. Use the top navigation bar to seamlessly move through all interactive sub-pages.

### Option 2: Live Local Flask Server Execution
To run the web app through its live Python environment:
1. Open a terminal/command prompt directly inside the root project folder.
2. Install dependencies if required: `pip install flask`
3. Execute the server engine script: `python app.py`
4. Open a web browser and navigate to the local host address provided in the terminal (typically `http://127.0.0.1:5000` or port `8080`).

---

## 🛠️ Design & Technical Features
* **Modular Templates:** Leverages template inheritance blocks to maintain UI consistency across pages without duplicating code.
* **Modern Layout Engineering:** Utilizes explicit CSS Grid and Flexbox properties for cross-device fluidity.
* **UI/UX Best Practices:** Features a glassmorphic sticky navigation blur, smooth scrolling transitions, and active button hover micro-interactions.