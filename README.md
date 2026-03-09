# Password Strength API

This repository contains a simple Flask-based API for analyzing and classifying the strength of passwords. The service extracts features such as length, digit count, special characters, entropy, etc., and uses a pre-trained logistic regression model to label the password strength.

## 📁 Project Structure

```
app.py
gettingPassword.py       # feature extraction logic
database? (none)
ModelOfPassword.py      # helper function for classification
label_encoder.joblib    # saved LabelEncoder
logistic_model.joblib   # trained model
scaler.joblib           # feature scaler
rquirements.txt         # Python dependencies
Procfile                # for deployment (Heroku/Gunicorn)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or newer
- `pip` package manager

### Installation
1. Clone the repository or copy the files into a directory.
2. Create and activate a virtual environment (optional but recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install the required packages:
   ```sh
   pip install -r rquirements.txt
   ```

### Running the API

Start the Flask server with:
```sh
python app.py
```
The app will listen on `http://0.0.0.0:5000` by default.

For production deployment, you can use the provided `Procfile` with Gunicorn:
```sh
gunicorn app:app
```

## 📦 API Endpoint

### `POST /analyze`
Analyze a password and return its strength label and features.

**Request JSON**:
```json
{
  "password": "yourPassword123!"
}
```

**Successful Response** (HTTP 200):
```json
{
  "strength_label": "Weak",
  "entropy": 54.0,
  "features": {
    "length": 15,
    "num_chars": 15,
    "num_digits": 3,
    "num_upper": 1,
    "num_lower": 10,
    "num_special": 1,
    "num_vowels": 4,
    "num_syllables": 4,
    "entropy": 54.0
  }
}
```

**Error Responses**:
- `400 Bad Request` if the JSON is missing or the password is empty.

## 🧠 How It Works

- `gettingPassword.extract_features()` computes numeric features from the given password, including an entropy estimate.
- The entropy is removed before passing features to the model.
- `ModelOfPassword.classify_password()` scales the features, predicts with the logistic model, and decodes the label.
- Models and transformers are loaded once at startup using `joblib`.

## 📝 Notes

- The models (`.joblib` files) must be present in the same directory as `app.py`.
- The `rquirements.txt` file contains a typo; make sure to reference it correctly if copying.

## 🛠️ Extending

You can retrain or replace the model using your own dataset. Ensure scaled features and label encoder are saved with `joblib` using the same variable names.

---

Feel free to experiment by sending requests with `curl`, Postman, or integrating into other applications!