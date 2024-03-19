# AquaVision: Fish Species Prediction

AquaVision is a machine learning project that predicts the species of a fish based on its weight, length measurements, height, and width. It utilizes a Random Forest Classifier model trained on a dataset containing information about various fish species.

## Dataset

The dataset used for training the model can be found [here](https://www.kaggle.com/aungpyaeap/fish-market). It contains the following columns:

- Species: The species of the fish.
- Weight: The weight of the fish (in grams).
- Length1: Length measurement 1 (in cm).
- Length2: Length measurement 2 (in cm).
- Length3: Length measurement 3 (in cm).
- Height: The height of the fish (in cm).
- Width: The width of the fish (in cm).

## Model

The trained machine learning model is a Random Forest Classifier, which is capable of predicting the species of a fish based on the provided features. The model has been serialized and saved as a pickle (.pkl) file for easy deployment and use. You can find the model file [here](link_to_model_pkl_file).

## Flask App

The Flask web application provides a user-friendly interface for predicting the species of a fish. Users can input the weight, length measurements, height, and width of a fish into the form, and the app will make predictions using the trained model.

### Usage

To use the Flask app locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask app by executing `python app.py` in the terminal.
4. Access the app in your web browser at `http://localhost:5000`.


Feel free to contribute to the project by forking the repository and submitting pull requests.

