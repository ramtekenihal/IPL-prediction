from flask import Flask,render_template, request
from model import get_encoded_Team
from model import get_encoded_Venue
from model import predict
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')





@app.route('/prediction', methods=['POST', 'GET'])
def match_winner():
	if request.method == 'POST':
		team1 = request.form['Team1']
		team2 = request.form['Team2']
		team1_toss_win = request.form['Toss']
		team1_bat = request.form['Decision']
		team1_powerplay_score = request.form['Team1_score']
		team2_powerplay_score = request.form['Team2_score']
		venue = request.form['Venue']

	features = np.array([get_encoded_Team(team1),get_encoded_Team(team2),team1_toss_win,team1_powerplay_score,team2_powerplay_score,get_encoded_Venue(venue)])
	
	return render_template('outcome.html', result = predict(features.reshape(1,-1)),team1=team1,team2=team2)


if __name__ == '__main__':
	app.run(host='0.0.0.0')
