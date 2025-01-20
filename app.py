from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np

app = Flask(__name__)

# Muat model yang sudah diekspor
with open('estimasi_harga_laptop_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/estimasi.html')
def estimasi():
    return render_template('estimasi.html')

@app.route('/tentang.html')
def tentang():
    return render_template('tentang.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari form input
    try:
        features = [
            float(request.form['feature1']),  # Sesuaikan dengan fitur model Anda
            float(request.form['feature2']),
            float(request.form['feature3']),
            float(request.form['feature4']),
            float(request.form['feature5']),
            # Tambahkan fitur lainnya di sini
        ]
        # Prediksi harga laptop
        prediction = model.predict([features])[0]
        return render_template('estimasi.html', prediction_text=f'Rp {prediction:,.2f}')
    except Exception as e:
        return render_template('estimasi.html', error_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)