from flask import Flask, render_template, request
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

curr_year = 2020
scaler = MinMaxScaler()
poly = PolynomialFeatures(degree=2)
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Taking the input from user
        year = int(request.form['year'])
        kms_driven = float(request.form['kms_driven'])
        present_price = float(request.form['present_price'])
        owners = request.form['owners']
        fuel_type = request.form['fuel_type']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']

        # Preprocessing the categorical input
        fuel_type_petrol = 0
        fuel_type_diesel = 0
        seller_type_individual = 0
        transmission_manual = 0
        if fuel_type == 'Diesel':
            fuel_type_diesel = 1
        if fuel_type == 'Petrol':
            fuel_type_petrol = 1
        if seller_type == 'Individual':
            seller_type_individual = 1
        if transmission == 'Manual':
            transmission_manual = 1

        # Preprocessing the numerical input
        num_years = curr_year - year
        num_years = np.log(num_years)
        num_years = scaler.fit_transform(np.array([num_years]).reshape(-1, 1))
        present_price = np.log(present_price)
        present_price = scaler.fit_transform(np.array([present_price]).reshape(-1, 1))
        kms_driven = np.log(kms_driven)
        kms_driven = scaler.fit_transform(np.array([kms_driven]).reshape(-1, 1))

        ip = np.array([present_price[0][0], kms_driven[0][0], owners, fuel_type_diesel, fuel_type_petrol, seller_type_individual, transmission_manual, num_years[0][0]])
        ip = poly.fit_transform([ip])
        op = model.predict(ip)

        return render_template('index.html', output_text='You can sell your car for {} lakhs'.format(round(op[0], 2)))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
