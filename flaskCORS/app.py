from flask import Flask, render_template, request
from flask_cors import CORS
from controller import Controller

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}) #setting origins to * allows everyone to access
'''
Because the web app utilizes an API, there are a lot of HTTP requests sending in and out of our app.
CORS allows those requests to move in an out of the domain without issue.
'''

#displays the weather query template of web app
@app.route("/api/")
def index():
    return render_template('index.html')

#request handler for calling up controller
@app.route('/ezw', methods=['POST', 'GET'])
def ezw():
    if request.method == 'POST':
        data = request.json
        input_location = data['location']

        ezw = Controller()

        geo_location = ezw.getLocation(input_location)
        if geo_location == None:
            address = "Unknown location"
            report_template = render_template('reports.html', weather_address=address)
            return report_template

        address = geo_location.address
        reports = ezw.getWeatherReports(data, geo_location)

        report_template = render_template('reports.html', weather_address=address, weather_reports=reports)

    return report_template


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')
