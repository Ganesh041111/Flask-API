from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/checkarm/<int:n>")
def checkarm(n):
    num = n

    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        result={
            "Number":n,
            "Armstrong":"Is an Armstrong number",
            "status":200
        }
        
    else:
        result={
            "Number":n,
            "Armstrong":"Is not an Armstrong number",
            "status":200
        }

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)


#flask python aws rds with aws lamda 