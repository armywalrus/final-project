# app.py to run this code run: python app.py
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def respond():
    return app.send_static_file('index.html')
    # # Retrieve the name from url parameter
    # name = request.args.get("name", None)

    # # For debugging
    # print(f"got name {name}")

    # response = {}

    # # Check if user sent a name at all
    # if not name:
    #     response["ERROR"] = "no name found, please send a name."
    # # Check if the user entered a number not a name
    # elif str(name).isdigit():
    #     response["ERROR"] = "name can't be numeric."
    # # Now the user entered a valid name
    # else:
    #     response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # # Return the response in json format
    # return jsonify(response)

if __name__ == '__main__':
    app.run()