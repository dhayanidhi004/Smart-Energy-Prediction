from flask import Flask, render_template, request, jsonify
import numpy as np
import random

app = Flask(__name__)

# 🔹 Mock prediction function (used when model is heavy)
def mock_predict(data):
    return round(sum(data) / len(data) + random.uniform(-0.5, 0.5), 2)

def generate_suggestions(value):
    tips = []
    if value > 6:
        tips.append("⚠ High energy usage detected. Reduce peak-hour consumption.")
        tips.append("💡 Consider using energy-efficient appliances.")
    elif value > 3:
        tips.append("ℹ Moderate usage. Monitor device usage patterns.")
    else:
        tips.append("✅ Energy usage is optimal. Good job!")
    return tips

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Expecting JSON data: { "input": [values] }
        data = request.json.get("input", [])
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert all inputs to float
        data = [float(x) for x in data]

        prediction = mock_predict(data)
        suggestions = generate_suggestions(prediction)

        return jsonify({
            "prediction": prediction,
            "suggestions": suggestions
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔹 Only use debug=True for local testing
if __name__ == "__main__":
    app.run(debug=True)
