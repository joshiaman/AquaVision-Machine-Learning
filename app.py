from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('fish_species_classification_model.pkl')

# Map class labels to species names
species_mapping = {
    0: 'Bream',
    1: 'Parkki',
    2: 'Perch',
    3: 'Pike',
    4: 'Roach',
    5: 'Smelt',
    6: 'Whitefish'
}

@app.route('/')
def index():
    return render_template('fish.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the request
        data = request.get_json()
        Weight = float(data['weight'])
        Length1 = float(data['length1'])
        Length2 = float(data['length2'])
        Length3 = float(data['length3'])
        Height = float(data['height'])
        Width = float(data['width'])
        
        # Make prediction using the model
        features = [[Weight,Length1, Length2, Length3, Height, Width]]
        predicted_class = model.predict(features)[0]
        
        # Map class label to species name
        predicted_species = species_mapping[predicted_class]
        
        if predicted_species is None:
            raise ValueError('Invalid predicted class')
        
        return jsonify({'species': predicted_species})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) #, host='0.0.0.0', port=5000
