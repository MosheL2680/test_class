from flask import Blueprint, request, jsonify

col = Blueprint('col', __name__)



# get 2 iterables and use python built-in function to perform custom zip operation on two iterables
def my_zip(it1, it2):
    return list(zip(it1, it2))

# Route to perform the custom zip operation
@col.route('/myzip', methods=['POST'])
def myzip_route():
    data = request.get_json()
    it1 = data.get('iterable1')
    it2 = data.get('iterable2')
    
    if it1 is not None and it2 is not None:
        # Perform custom zip operation on the provided iterables
        result = my_zip(it1, it2)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Please provide both iterables.'}), 400
