# 🍎 AI Food Inspection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)

![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)

![Gemini AI](https://img.shields.io/badge/Gemini-AI-blueviolet?style=for-the-badge)

![Computer Vision](https://img.shields.io/badge/Computer_Vision-AI-green?style=for-the-badge)

![PDF Reports](https://img.shields.io/badge/PDF-Reports-red?style=for-the-badge)

![Dashboard](https://img.shields.io/badge/Dashboard-Analytics-orange?style=for-the-badge)

</div>

---

# 📌 Overview

AI Food Inspection System is an intelligent web application that automates food quality assessment using Artificial Intelligence, Computer Vision, and Gemini AI.

The system analyzes uploaded food images and performs multiple inspections, including freshness detection, nutritional analysis, temperature assessment, and food safety evaluation.

It provides real-time insights, generates inspection reports, maintains historical records, and offers an interactive dashboard for efficient food quality monitoring.

This project is designed for food industries, restaurants, laboratories, supermarkets, and food safety management systems.

---

# 🚀 Features

## 🤖 AI-Powered Food Analysis

Analyze food images using Artificial Intelligence.

Capabilities include:

- Food identification
- Quality assessment
- Food safety analysis
- Intelligent recommendations

---

## 🥗 Freshness Detection

Determine food freshness levels.

Detect:

- Fresh food
- Moderate freshness
- Spoiled food

---

## 🧪 Nutrition Analysis

Analyze nutritional information.

Generate insights for:

- Calories
- Protein
- Carbohydrates
- Fat content
- Nutritional values

---

## 🌡️ Temperature Analysis

Evaluate temperature conditions.

Monitor:

- Safe temperature ranges
- Potential risks
- Storage conditions

---

## 🧠 Gemini AI Integration

Generate intelligent reports and recommendations using Gemini AI.

Capabilities:

- Food safety suggestions
- Quality explanations
- Risk assessments
- Improvement recommendations

---

## 📄 PDF Report Generation

Generate downloadable inspection reports.

Reports include:

- Food details
- Freshness analysis
- Nutritional analysis
- Temperature analysis
- AI recommendations

---

## 🎙️ Voice Assistance

Support voice-enabled interactions.

Features:

- Voice commands
- Speech-based navigation

---

## 📷 Webcam Support

Perform real-time food inspections using webcam input.

---

## 📊 Dashboard Analytics

Visualize inspection data.

Monitor:

- Inspection statistics
- Historical trends
- Food quality metrics

---

## 🌙 Dark Mode Support

Toggle between:

- Light mode
- Dark mode

---

## 🔐 User Authentication

Secure access with:

- User Registration
- Login System
- Admin Dashboard

---

## 🗂️ Inspection History

Store and retrieve previous inspections.

Track:

- Inspection records
- Generated reports
- User activities

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | Web Framework |
| Gemini AI | AI Analysis |
| Computer Vision | Image Processing |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Interactive UI |
| SQL | Database |
| PDF Generator | Report Generation |

---

# 📂 Project Structure

```text
AI-Food-Inspection-System/

│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── database/
│   └── schema.sql
│
├── models/
│   ├── database.py
│   └── user.py
│
├── utils/
│   ├── gemini_ai.py
│   ├── image_detector.py
│   ├── freshness_detector.py
│   ├── nutrition_analyzer.py
│   ├── temperature_analyzer.py
│   └── pdf_generator.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── voice.js
│   │   ├── webcam.js
│   │   ├── charts.js
│   │   └── darkmode.js
│   │
│   ├── images/
│   │   └── background.jpg
│   │
│   └── uploads/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── inspect.html
│   ├── history.html
│   └── admin.html
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-food-inspection-system.git

cd ai-food-inspection-system
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file.

Example:

```env
GEMINI_API_KEY=your_api_key

SECRET_KEY=your_secret_key

DATABASE_URL=your_database_url
```

---

## 5️⃣ Initialize Database

Execute the SQL schema.

```bash
database/schema.sql
```

---

# ▶️ Run the Application

Start the application using:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🔄 System Workflow

```text
Upload Food Image
          ↓

Image Processing
          ↓

Freshness Detection
          ↓

Nutrition Analysis
          ↓

Temperature Analysis
          ↓

Gemini AI Analysis
          ↓

Dashboard Visualization
          ↓

PDF Report Generation
```

---

# 📊 Dashboard Modules

### 🏠 Dashboard

- Statistics
- Analytics
- Reports

### 🔎 Food Inspection

- Upload Image
- Webcam Scan
- AI Analysis

### 📜 History

- Previous inspections
- Generated reports

### 👨‍💼 Admin Panel

- User management
- System monitoring

---

# 🎯 Use Cases

This project can be used for:

- 🍽️ Restaurants
- 🏭 Food Industries
- 🛒 Supermarkets
- 🧪 Food Laboratories
- 🏥 Hospitals
- 🏫 Research Institutions
- 🥗 Nutrition Monitoring

---

---

# 👨‍💻 Author

Singipurapu Dinesh

Feel free to explore, fork, and contribute to this project.

If you found this project useful, please consider giving it a ⭐ on GitHub.

---
