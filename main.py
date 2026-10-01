from flask import Flask, render_template, request
import mysql.connector

# Create the Flask application instance
app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ENTER PASSWORD", # Changed so I am not sharing my MySQL password. Please communicate if it is needed
    database="flask_assignment"
)

# Route for the Home page
@app.route("/")
def home():
    # Renders home.html from the templates folder
    return render_template("home.html")


# Route for the Contact Us page
@app.route("/contact")
def contact():
    # Renders contact.html from the templates folder
    return render_template("contact.html")


# Route for the Form page
@app.route("/form")
def form():
    # Renders form.html from the templates folder
    return render_template("form.html")


# Route that receives and processes the submitted form data (POST only)
@app.route("/submit-form", methods=["POST"])
def submit_form():
    # Read each of the 10 submitted fields using the "name" attribute
    # from the <input>/<select>/<textarea> elements in form.html
    full_name = request.form.get("full_name").strip()
    email = request.form.get("email")
    age = int(request.form.get("age"))
    city = request.form.get("city").strip()
    country = request.form.get("country").strip()
    occupation = request.form.get("occupation").strip()
    hobby = request.form.get("hobby").strip()
    programming_language = request.form.get("programming_language").strip()
    online_hours = int(request.form.get("online_hours"))
    entertainment = request.form.get("entertainment").strip() #The form has dropdown, but included strip as it shoudl not hurt and allows drop-down to be changed to text input in the future if needed.

    # Insert the submitted data into the MySQL database
    query = """    
        INSERT INTO users (full_name, email, age, city, country, occupation, hobby, programming_language, online_hours, entertainment)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor = db.cursor()
    cursor.execute(query, (    full_name,    email,    age,    city,    country,    occupation,    hobby,    programming_language,    online_hours,    entertainment))
    db.commit()

    # Print the submitted data to the terminal
    print("----- Form Submission -----")
    print(f"Full Name: {full_name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"Occupation: {occupation}")
    print(f"Hobby: {hobby}")
    print(f"Programming Language: {programming_language}")
    print(f"Online Hours: {online_hours}")
    print(f"Entertainment: {entertainment}")
    print("----------------------------")

    # Message shown back to the user in the browser
    return "Form submitted successfully! Check your terminal to see the submitted data."

@app.route("/users")
def users():
    cursor = db.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    user_rows = cursor.fetchall()
    return render_template("users.html", users=user_rows) # renamed to user_rows so the variable is distinct from the function name, added route to the Nav bar



# Start the Flask development server when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)
