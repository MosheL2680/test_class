from flask import Blueprint, request, jsonify

# Global variable to track whether functions in simp module have been called
simp_called = False

simp = Blueprint('simp', __name__)

# return sum of 2 numbers
@simp.route('/add', methods=['POST'])
def add_numbers():
    global simp_called
    simp_called = True
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is not None and num2 is not None:
        result = num1 + num2
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Please provide both numbers.'}), 400

# return sub of 2 numbers 
@simp.route('/subtract', methods=['POST'])
def subtract_numbers():
    global simp_called
    simp_called = True
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is not None and num2 is not None:
        result = num1 - num2
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Please provide both numbers.'}), 400
