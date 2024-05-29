from flask import Flask, request, jsonify
import random 

app = Flask(__name__)

@app.get("/")
def index():
    print("This is an index page")
    return "This is an index page!"

@app.get("/generate-random-data")
def generate_random_data():
    criteria = request.args.getlist('criteria')
    if len(criteria) == 0:
        return { "error": "No criteria is provided." }, 400
    generated_data = {}
    for c in criteria:
        if c == "numbers":
            no_numbers = request.args.get('no_numbers')
            if no_numbers is None:
                return { "error": "No desired number of generated numbers is provided." }, 400
            no_numbers = int(no_numbers)
            generated_data['numbers'] = []
            for _ in range(no_numbers):
                generated_data['numbers'].append(random.randint(1, 100))
        elif c == "names":
            names = ["Mike", "Ellen", "Cory", "Jasmine", "Todd"]
            no_names = request.args.get('no_names')
            if no_names is None:
                return { "error": "No desired number of generated names is provided." }, 400
            no_names = int(no_names)
            generated_data['names'] = random.choices(names, k=no_names)
        
    return generated_data


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=50000, debug=True)