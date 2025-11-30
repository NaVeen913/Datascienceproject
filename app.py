from flask import Flask, render_template, request
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

# create prediction pipeline object
predict_pipeline = PredictionPipeline()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_data = {
    "sepal_length (cm)": float(request.form["sepal_length"]),
    "sepal_width (cm)": float(request.form["sepal_width"]),
    "petal_length (cm)": float(request.form["petal_length"]),
    "petal_width (cm)": float(request.form["petal_width"])
}


    prediction = predict_pipeline.predict(input_data)

    return render_template("index.html", prediction_text=f"Prediction: {prediction}")

if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(debug=True, port=8080)

