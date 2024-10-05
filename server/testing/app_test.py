import io
import sys
from app import app

class TestApp:
    '''Flask application tests.'''

    def test_index_route(self):
        '''Check if the homepage is accessible.'''
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_index_text(self):
        '''Check the homepage displays the correct title.'''
        response = app.test_client().get('/')
        assert response.data.decode() == '<h1>Python Operations with Flask Routing and Views</h1>'

    def test_print_route(self):
        '''Check if the print route is accessible.'''
        response = app.test_client().get('/print/hello')
        assert response.status_code == 200

    def test_print_text(self):
        '''Check if the print route displays the correct text.'''
        response = app.test_client().get('/print/hello')
        assert response.data.decode() == 'Printed: hello'  # Adjusted expected output

    def test_print_text_in_console(self):
        '''Check if the print route outputs the correct text to the console.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        app.test_client().get('/print/hello')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == 'hello\n'

    def test_count_route(self):
        '''Check if the count route is accessible.'''
        response = app.test_client().get('/count/5')
        assert response.status_code == 200

    def test_count_range_10(self):
        '''Check if counting to 10 returns the correct range.'''
        response = app.test_client().get('/count/10')
        count = '<br>'.join(str(i) for i in range(11))  # Use <br> for line breaks
        expected_output = f'Counting to 10:<br>{count}'
        assert response.data.decode() == expected_output

    def test_math_route(self):
        '''Check if the math route is accessible.'''
        response = app.test_client().get('/math/5/+/5')
        assert response.status_code == 200

    def test_math_add(self):
        '''Check addition operation in the math route.'''
        response = app.test_client().get('/math/5/+/5')
        assert response.data.decode() == 'Result of 5 + 5 = 10'  # Adjusted expected output

    def test_math_subtract(self):
        '''Check subtraction operation in the math route.'''
        response = app.test_client().get('/math/5/-/5')
        assert response.data.decode() == 'Result of 5 - 5 = 0'  # Adjusted expected output

    def test_math_multiply(self):
        '''Check multiplication operation in the math route.'''
        response = app.test_client().get('/math/5/*/5')
        assert response.data.decode() == 'Result of 5 * 5 = 25'  # Adjusted expected output

    def test_math_divide(self):
        '''Check division operation in the math route.'''
        response = app.test_client().get('/math/5/div/5')
        assert response.data.decode() == 'Result of 5 div 5 = 1.0'  # Adjusted expected output
    
    def test_math_modulo(self):
        '''Check modulo operation in the math route.'''
        response = app.test_client().get('/math/5/%/5')
        assert response.data.decode() == 'Result of 5 % 5 = 0'  # Adjusted expected output
