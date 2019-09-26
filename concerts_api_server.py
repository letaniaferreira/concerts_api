from flask import Flask, jsonify, request
import requests
import os
app = Flask(__name__)

tasks={
    1: {
        'time': 'evening',
        'daily': True,
        'id': 1
    },
    2: {
        'time': 'evening',
        'daily': True,
        'id': 2
    },
    3: {
        'test': "hi"
    }
}

@app.route('/performers')
def get_performers():

    bands = []
    client_id = os.environ['CLIENT_ID']
    response = requests.get('https://api.seatgeek.com/2/performers?client_id={}'.format(client_id))
    performers_dict = response.json()
    for performer in performers_dict['performers']:
        #performer does not print anything
        #print('these are the names of the bands {}'.format(performer))
        if performer['type'] == 'band':
            bands.append(performer['name'])

    return jsonify({'bands': bands})

@app.route('/')
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/task/<int:task_id>')
def get_task(task_id):
    task = tasks.get(task_id)
    return jsonify({'task':task})

@app.route('/task', methods=['POST'])
def add_task():
    num = 0
    for k, v in enumerate(tasks):
        if k > num:
            num = k
    tasks[num + 1] = {
        'time': request.json['time'],
        'daily': False
    }
    task = tasks[num + 1]
    return jsonify({'task': task}), 201


if __name__ == '__main__':
    app.run(debug=True)