from flask import Flask, render_template, request, jsonify, send_from_directory
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('Model/best_model.joblib')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def serve_script():
    return send_from_directory('.', 'script.js')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Convert form data to numpy array
        features = np.array([
            int(data['uni_admssn_year']),
            int(data['gender']),
            int(data['age']),
            int(data['hsc_pass_year']),
            int(data['currnt_sem']),
            int(data['merit_scholarship']),
            int(data['use_uni_transport']),
            int(data['study_hour']),
            int(data['learning_mode']),
            int(data['has_smart_phone']),
            int(data['has_pc']),
            int(data['social_media_time']),
            int(data['english_skill']),
            int(data['avg_attendance']),
            int(data['probation']),
            int(data['suspension']),
            int(data['faculty_consultency']),
            int(data['relation_sts']),
            int(data['co_curri_act']),
            int(data['living_sts']),
            float(data['sgpa']),
            int(data['phy_disb']),
            float(data['cgpa']),
            int(data['comp_cred'])
        ]).reshape(1, -1)
        
        # Make prediction
        prediction = int(model.predict(features)[0])
        
        # Map prediction to status
        status_map = {
            0: "Probation",
            1: "Unsatisfactory",
            2: "Moderate",
            3: "Satisfactory",
            4: "Excellent"
        }
        
        status = status_map.get(prediction, f"Unknown Status ({prediction})")
        
        # Return prediction with robust mapping
        return jsonify({
            'success': True,
            'prediction': str(prediction),
            'status': status
        })
    except Exception as e:
        import traceback
        print('Prediction error:', traceback.format_exc())
        return jsonify({
            'success': False,
            'error': str(e)
        }) 