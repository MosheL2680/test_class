from flask import Blueprint, request, jsonify
from .simp import simp_called

comp = Blueprint('comp', __name__)



# Function to calculate the sum of digits in a number
def sum_of_digits(number):
    # Convert the number to a string and run a loop through each digit,
    return sum(int(digit) for digit in str(number) if digit.isdigit())#(ignoring non-numeric characters)

# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string and compare it to its reverse
    return str(number) == str(number)[::-1]




# Route to return the sum of digits, using the function above
@comp.route('/sumofdigits', methods=['POST'])
def sum_of_digits_route():
        data = request.get_json()
        num = data.get('number')
        if num is not None:
            result = sum_of_digits(num)
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Please provide a number.'}), 400
# Route to check if a number is a palindrome, using the function from
@comp.route('/ispal', methods=['POST'])
def is_palindrome_route():
        data = request.get_json()
        num = data.get('number')
        if num is not None:
            result = is_palindrome(num)
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Please provide a number.'}), 400
