<?php
header("Content-Type: application/json");

// ضع هنا كلمة المرور التي تريد اختبارها
$password = "MyTestPassword123!";

// رابط Python API (Flask)
$python_api_url = "http://127.0.0.1:5000/analyze"; // تأكد أنه نفس الرابط الذي يشغل Flask

// تجهيز البيانات للإرسال
$data = json_encode([
    "password" => $password
]);

// تهيئة cURL
$ch = curl_init($python_api_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/json"]);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

// تنفيذ الطلب
$response = curl_exec($ch);

if (curl_errno($ch)) {
    echo json_encode([
        "error" => "Python API connection failed",
        "message" => curl_error($ch)
    ]);
    curl_close($ch);
    exit;
}

curl_close($ch);

// تحويل الرد من JSON إلى مصفوفة PHP
$decoded = json_decode($response, true);

// طباعة النتيجة بشكل منسق
echo json_encode([
    "success" => true,
    "api_response" => $decoded
], JSON_PRETTY_PRINT);