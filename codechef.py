from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/handle/<handle>', methods=['GET'])
def handle_data(handle):
    if handle == 'favicon.ico':
        return jsonify({'success': False, 'error': 'Invalid request'})
    
    try:
        response = requests.get(f'https://www.codechef.com/users/{handle}')
        response.raise_for_status()
        page_content = response.text
        
        try:
            # Parsing the HTML
            soup = BeautifulSoup(page_content, 'html.parser')
        except Exception as e:
            return jsonify({'success': False, 'error': f'Error parsing HTML: {str(e)}', 'handle': handle})
        
        user_details = {}

        # Extracting user details
        user_details_section = soup.select_one('.user-details')
        for detail in user_details_section.find_all('li'):
            label = detail.find('label').text
            value = detail.find('span').text.strip()
            if label == 'Username:' and detail.find('span', class_='rating'):
                value = detail.find('span', class_='m-username--link').text
            elif label == 'Country:' and detail.find('img'):
                value = detail.find('span', class_='user-country-name').text
            elif label == 'CodeChef Pro Plan:' and detail.find('a'):
                value = 'Yes' if detail.find('a').text == 'View Details' else 'No'
            user_details[label] = value
        
        user_details['currentRating'] = int(soup.select_one('.rating-number').text.replace(',', '').replace('?', ''))
        
        # Remove Pro Plan from user details
        if 'CodeChef Pro Plan:' in user_details:
            del user_details['CodeChef Pro Plan:']
        
        return jsonify({'success': True, **user_details})

    except Exception as e:
        return jsonify({'response': response.status_code, 
                        'success': False, 
                        'error': f'Error fetching user data from CodeChef: {str(e)}',
                        'suggest': 'Most probably the entered username is invalid.', 
                        'handle': handle})
@app.route('/<handle>', methods=['GET'])
def redirect_to_handle(handle):
    if handle and not '.' in handle:
        return redirect(url_for('handle_data', handle=handle))
    else:
        return jsonify({'success': False, 'error': 'Invalid Endpoint. Kindly change your URL.'})

if __name__ == '__main__':
    app.run(port=8800)
