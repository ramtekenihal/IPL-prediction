import numpy as np 
import pandas as pd 
# from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def predict(features):
	#training data
	ipl_data = pd.read_csv('iplmldata.csv')

	#features
	X = ipl_data.drop('team1_win',axis=1)

	#target
	y = ipl_data['team1_win']

	#splitting data

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

	# C=1 and gamma=0.0001 obtain from GridSearchCV on SVC
	
	svc = SVC(C=1,gamma=0.0001)

	svc.fit(X_train,y_train)

	predictions = svc.predict(features)

	return predictions






encoded_venue ={
    'Rajiv Gandhi International Stadium, Uppal':22,
    'Maharashtra Cricket Association Stadium':16,
    'Saurashtra Cricket Association Stadium':24,
    'Holkar Cricket Stadium':11,
    'M. Chinnaswamy Stadium':14,
    'Wankhede Stadium':33,
    'Eden Gardens':7,
    'Feroz Shah Kotla Ground':8,
    'Punjab Cricket Association IS Bindra Stadium, Mohali':21,
    'Green Park':9,
    'Sawai Mansingh Stadium':25,
    'MA Chidambaram Stadium, Chepauk':15,
    'Dr DY Patil Sports Academy':4,
    'Newlands':19,
    "St George's Park":29,
    'Kingsmead':13,
    'SuperSport Park':31,
    'Buffalo Park':2,
    'New Wanderers Stadium':18,
    'De Beers Diamond Oval':3,
    'OUTsurance Oval':20,
    'Brabourne Stadium':1,
    'Sardar Patel Stadium, Motera':23,
    'Barabati Stadium':0,
    'Vidarbha Cricket Association Stadium, Jamtha':32,
    'Himachal Pradesh Cricket Association Stadium':10,
    'Nehru Stadium':17,
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':5,
    'Subrata Roy Sahara Stadium':30,
    'Shaheed Veer Narayan Singh International Stadium':26,
    'JSCA International Stadium Complex':12,
    'Sheikh Zayed Stadium':28,
    'Sharjah Cricket Stadium':27,
    'Dubai International Cricket Stadium':6
    
}


encoded_Teams= {
    'SRH':13,
    'MI':8, 
    'GL':4, 
    'RPS':11, 
    'RCB':10, 
    'KKR':5, 
    'DD':2, 
    'KXIP':7, 
    'CSK':0, 
    'RR':12,
    'DC':1, 
    'KTK':6, 
    'PW':9, 
    'Delhi Capitals':3
    
}

def get_encoded_Team(val):
	return encoded_Teams.get(val)

def get_encoded_Venue(val):
	return encoded_venue.get(val)
