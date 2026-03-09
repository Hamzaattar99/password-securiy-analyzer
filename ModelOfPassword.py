def classify_password(df_for_model, model, scaler, le):

    # Scaling
    features_scaled = scaler.transform(df_for_model)

    # Prediction
    pred_encoded = model.predict(features_scaled)

    # Decode label
    pred_label = le.inverse_transform(pred_encoded)

    return pred_label[0]