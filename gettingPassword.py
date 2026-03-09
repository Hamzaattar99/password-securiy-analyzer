import pandas as pd
import math




# ---------------------------
# 1. دالة استخراج خصائص كلمة المرور
# ---------------------------
def extract_features(password):
    features = {}
    features['length'] = len(password)
    features['num_chars'] = len(password)
    features['num_digits'] = sum(c.isdigit() for c in password)
    features['num_upper'] = sum(c.isupper() for c in password)
    features['num_lower'] = sum(c.islower() for c in password)
    features['num_special'] = sum(not c.isalnum() for c in password)
    features['num_vowels'] = sum(c.lower() in 'aeiou' for c in password)
    # تقريب عدد المقاطع (syllables) بطريقة بسيطة
    features['num_syllables'] = max(1, sum(c.lower() in 'aeiou' for c in password))
    
    
    
    charset_size = 0
    if features['num_lower']:
        charset_size += 26
    if features['num_upper']:
        charset_size += 26
    if features['num_digits']:
        charset_size += 10
    if features['num_special']:
        charset_size += 32

    # حساب Entropy
    if charset_size > 0:
        entropy = round(features['length'] * math.log2(charset_size), 2)
    else:
        entropy = 0.0
        
    
    features['entropy'] = entropy
    
    return pd.DataFrame([features])
