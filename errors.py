from flask import jsonify

def not_found_error(message):
    response = jsonify({'error': 'Not Found', 'message': message})
    response.status_code = 404
    return response

def bad_request_error(message):
    response = jsonify({'error': 'Bad Request', 'message': message})
    response.status_code = 400
    return response

def unauthorized_error(message):
    response = jsonify({'error': 'Unauthorized', 'message': message})
    response.status_code = 401
    return response

def internal_server_error(message):
    response = jsonify({'error': 'Internal Server Error', 'message': message})
    response.status_code = 500
    return response
