from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS  # Import Flask-CORS
from db import insert_kritik, get_connection  # Import fungsi dari db.py

app = Flask(__name__)
CORS(app)


get_connection()

# Endpoint untuk menerima data kritik
@app.route('/submit', methods=['POST', 'OPTIONS'])
def submit():
    if request.method == 'OPTIONS':
        # Manual response to preflight
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5500'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    try:
        # Ambil data JSON dari request
        data = request.get_json()
        nama = data.get('nama')
        email = data.get('email')
        kritik = data.get('kritik')

        # Masukkan data ke database atau proses lainnya
        success = insert_kritik(nama, email, kritik)

        if success:
            return jsonify({"status": "success", "message": "Kritik berhasil dikirim"}), 200
            print("[DB]✅ Data berhasil dimasukkan ke database.")
        else:
            return jsonify({"status": "error", "message": "Gagal mengirim kritik"}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
