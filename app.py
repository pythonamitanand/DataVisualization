from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

# Sample data generation
def generate_sample_data():
    data = {
        'sales': {
            'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Aug'],
            'values': [500, 1800, 1400, 1100, 2100, 1000, 2000]
        },
        'users': {
            'categories': ['New', 'Active', 'Inactive', 'Current'],
            'values': [450, 800, 250, 500]
        },
        'engagement': {
            'dates': ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', '2024-02-05','2024-02-08'],
            'pageviews': [1500, 1600, 1350, 1800, 2000, 1500],
            'sessions': [800, 850, 750, 950, 1100, 1300]
        }
    }
    return data

@app.route('/')
def dashboard():
    data = generate_sample_data()
    return render_template('index.html', data=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)