## Project Name
Flask Assignment

## Project Description
A small Flask web app with a home page, a contact page, a 10-question survey form, and a users page. Form submissions are saved to a MySQL database and printed to the terminal, and the users page displays every saved submission in a table. It was built as a school project introducing Python web development with Flask and MySQL.

## Technologies
- Python
- Flask
- Jinja2
- MySQL (via mysql-connector-python)
- HTML

## How to Run
1. Install [Python](https://www.python.org) 3.10 or newer and [MySQL](https://dev.mysql.com/downloads/).
2. Clone or download this repository and open a terminal in the project folder.
3. Keep the folder structure intact: `main.py` and `requirements.txt` sit in the root folder, and the HTML files go in a `templates/` folder, which is where Flask looks for them.
4. Run `pip install -r requirements.txt` to install the dependencies.
5. In MySQL, create a database named `flask_assignment` containing a `users` table. The table needs an ID column first, followed by these ten columns in this order: `full_name`, `email`, `age`, `city`, `country`, `occupation`, `hobby`, `programming_language`, `online_hours`, and `entertainment`.
6. Open `main.py` and replace `ENTER PASSWORD` with your MySQL root password. The connection uses `localhost` and the `root` user.
7. Run `python main.py` to start the development server. The app connects to MySQL when it starts, so MySQL must already be running.
8. Open http://127.0.0.1:5000 in your browser.

## Features
- Home and Contact Us pages with a navigation bar linking all sections
- Survey form with ten questions: full name, email, age, city, country, occupation, hobby, favourite programming language, online hours per week, and entertainment preference
- Form data is submitted by POST to the `/submit-form` route, trimmed of extra spaces, saved to MySQL with a parameterized query, and printed to the terminal
- Users page that reads every row from the database and displays it in a table using a Jinja2 loop
- Jinja2 templates rendered with Flask's `render_template`

## Author
Patrick Grace — [patrickmgrace.com](https://www.patrickmgrace.com/) — GitHub: [StandardGrace](https://github.com/StandardGrace)