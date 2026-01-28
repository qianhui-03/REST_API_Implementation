from flask import Flask, jsonify,request
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return jsonify({'data':'hello world'})

@app.route('/square/<int:num>',methods=['GET'])
def disp(num):
    return jsonify({'result':num **2})

@app.route('/square',methods=['POST'])
def square_post():
    data = request.get_json()
    num = data['num']
    return jsonify({'square':num**2})
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)

