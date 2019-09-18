from flask import Flask, jsonify, request
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