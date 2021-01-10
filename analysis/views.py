from django.shortcuts import render
from .forms import BikeForm
import pandas as pd
import os as os

def datainputform(request):
	if request.method == 'POST':
		form = BikeForm(request.POST)
		if form.is_valid():
			hour = form.cleaned_data['hour']
			temp = form.cleaned_data['temp']
			humidity = form.cleaned_data['humidity']
			wind_speed = form.cleaned_data['wind_speed']
			visibility = form.cleaned_data['visibility']
			solar_rad = form.cleaned_data['solar_rad']
			rainfall = form.cleaned_data['rainfall']
			snowfall = form.cleaned_data['snowfall']
			season = form.cleaned_data['season']
			holiday = form.cleaned_data['holiday']
			form.save()

	form = BikeForm()

	if season == 'Winter':
		season = 0
	elif season == 'Autumn':
		season = 1
	elif season == 'Spring':
		season = 2
	elif season == 'Summer':
		season = 3

	if holiday == 'Holiday':
		holiday = 1
	elif holiday == 'No Holiday':
		holiday = 0

	pathname = (os.path.realpath(__file__))
	pathnametot = pathname[:-8] + 'Dataset_Fixed.xlsx'
	
	data_f = pd.read_excel(
		os.path.join("Data", pathnametot),
		engine='openpyxl',
	)
	#data_f = pd.read_excel(pathname + 'Dataset_Fixed.xlsx')
	data_f.columns = [c.replace(' ', '_') for c in data_f.columns]
	data_f['Seasons'].replace(['Winter','Autumn','Spring','Summer'], [0,1,2,3], inplace = True)
	data_f['Holiday'].replace(['No Holiday','Holiday'], [0,1], inplace = True)
	df_all_param = data_f[["Hour", "Temperature(°C)", "Humidity(%)", "Wind_speed_(m/s)", "Visibility_(10m)", "Solar_Radiation_(MJ/m2)", 
	             "Rainfall(mm)", "Snowfall_(cm)", "Seasons", "Holiday"]]
	X = df_all_param
	y = data_f["Rented_Bike_Count"]
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 50)
	print("Train set : ", X_train.shape)
	print("Test set : ", X_test.shape)
	#Modelisation
	from sklearn.linear_model import Lasso
	lasso_reg = Lasso(alpha=0.3264322837906803)
	#training
	lasso_reg.fit(X_train, y_train)

	#prédiction

	pred = lasso_reg.predict([[hour, temp, humidity, wind_speed, visibility, solar_rad, rainfall, snowfall, season, holiday]])

	return render(request, 'prediction.html', {'form': form, 'pred': pred})


