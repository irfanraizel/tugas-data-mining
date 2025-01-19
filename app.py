from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Muat model yang sudah diekspor
with open('estimasi_harga_laptop_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')  # Halaman utama

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari form input
    try:
        features = [
            float(request.form['feature1']),  
            float(request.form['feature2']),
            float(request.form['feature3']),
            float(request.form['feature4']),
            float(request.form['feature5']),
        ]
        # Prediksi harga laptop
        prediction = model.predict([features])[0]
        return render_template('index.html', prediction_text=f'Perkiraan harga: Rp {prediction:,.2f}')
    except Exception as e:
        return render_template('index.html', error_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
