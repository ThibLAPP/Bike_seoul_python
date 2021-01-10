import pandas as pd

def predicted():
	data_f = pd.read_excel(r"C:/Users/user/Documents/Thibault/boulot/ESILV/2020-2021/S1/Python for data/API/bike_seoul/analysis/Dataset_Fixed.csv")
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
	lasso_reg = Lasso(alpha=0.1)
	#training
	lasso_reg.fit(X_train, y_train)

	#prédiction
	pred = lasso_reg.predict([[14,20,50,3,2000,2,0,10,0,1]])
	return pred