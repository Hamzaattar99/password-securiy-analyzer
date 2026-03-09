from flask import Flask, request, jsonify
import joblib
from gettingPassword import extract_features
from ModelOfPassword import classify_password

app = Flask(__name__)

# ==========================
# تحميل المودل مرة واحدة فقط
# ==========================
model = joblib.load("logistic_model.joblib")
scaler = joblib.load("scaler.joblib")
le = joblib.load("label_encoder.joblib")

# ==========================
# API Endpoint
# ==========================
@app.route("/analyze", methods=["POST"])
def analyze_password():

    data = request.get_json()

    if not data or "password" not in data:
        return jsonify({"error": "No password provided"}), 400

    password = data["password"]

    if not password:
        return jsonify({"error": "Empty password"}), 400

    # 1️⃣ استخراج الخصائص (يشمل entropy)
    df = extract_features(password)

    # 2️⃣ حذف entropy قبل التنبؤ
    df_for_model = df.drop(columns=["entropy"])

    # 3️⃣ تصنيف كلمة المرور
    label = classify_password(df_for_model, model, scaler, le)

    # 4️⃣ تجهيز الرد
    response = {
        "strength_label": label,
        "entropy": df.iloc[0]["entropy"],
        "features": df.iloc[0].to_dict()
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 , debug=True)