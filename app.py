from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_strong_password(password):
    """
    Validates if the password is strong.
    A strong password must:
    - Be at least 8 characters long
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one digit
    - Contain at least one special character
    """
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return True
    return False

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if not is_strong_password(password):
        return jsonify({"error": "Password is not strong enough. It must be at least 8 characters long, "
                                 "contain an uppercase letter, a lowercase letter, a digit, and a special character."}), 400

    # Simulate user creation (e.g., save to database)
    # In a real application, you would hash the password before saving it
    return jsonify({"message": f"User {username} signed up successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)