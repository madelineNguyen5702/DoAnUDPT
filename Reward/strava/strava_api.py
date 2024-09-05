from flask import Flask, render_template, jsonify
import requests
import urllib3

app = Flask(__name__)

def get_strava_activities():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    auth_url = "https://www.strava.com/oauth/token"
    activities_url = "https://www.strava.com/api/v3/athlete/activities"

    payload = {
        'client_id': "133879",
        'client_secret': '73422dc183d6184437386674098670f2bdd227b7',
        'refresh_token': 'ee814f56f7bf3118efa2a9f698c8081e70269597',
        'grant_type': "refresh_token",
        'f': 'json'
    }

    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    header = {'Authorization': 'Bearer ' + access_token}

    requests_page_num = 1
    all_activities = []

    while True:
        param = {'per_page': 200, 'page': requests_page_num}
        my_dataset = requests.get(activities_url, headers=header, params=param).json()

        if len(my_dataset) == 0:
            break

        all_activities.extend(my_dataset)
        requests_page_num += 1

    return all_activities

@app.route('/')
def index():
    activities = get_strava_activities()
    return render_template('strava.html', activities=activities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

