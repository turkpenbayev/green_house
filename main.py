from flask import Flask, render_template, jsonify, request
from random import randint
# import Adafruit_DHT
app = Flask(__name__)
# sensor = Adafruit_DHT.DHT22
pin = 4


def turn_on_pump():
    pass


def turn_off_pump():
    pass


@app.route("/")
def main():
    # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity, temperature = randint(25, 100), randint(0, 50)
    templateData = {'temperature': temperature, 'humidity': humidity}
    return render_template('index.html', **templateData)


@app.route('/update', methods=['GET'])
def updated():
    humidity, temperature = randint(25, 100), randint(0, 50)
    data = {
        'humidity': humidity,
        'temperature': temperature
    }
    return jsonify(data)


@app.route('/watering', methods=['GET'])
def wather():

    req_status = request.args.get('status')

    if req_status == 'true':
        turn_on_pump()
        watering_status = True
    else:
        turn_off_pump()
        watering_status = False

    data = {
        'watering_status': watering_status
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
