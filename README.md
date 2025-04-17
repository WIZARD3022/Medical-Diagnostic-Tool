
# 🧠 Medical Diagnostic Tool  
**Team: ग़लती से Developer**  
_Hackathon Project_

## 🚀 Overview

The **Medical Diagnostic Tool** is an AI-powered web application developed during a hackathon to support early detection of various medical conditions using medical imaging. With an emphasis on **speed**, **simplicity**, and **offline capability**, this tool uses deep learning models for both classification and segmentation of medical images such as X-rays and MRIs — all without relying on external APIs.

## 🛠️ Features

- 🔍 **Disease Detection** – Identifies medical conditions like fractures and brain tumors.
- 🧠 **MRI Classification** – Classifies MRI brain scans into:
  - Glioma
  - Meningioma
  - Pituitary tumor
  - No Tumor
- 🖼️ **Tumor Segmentation** – Localizes tumor regions using U-Net-based segmentation.
- 📸 **MRI Validator** – Confirms whether an uploaded image is a valid MRI scan before processing.
- 🌐 **Web-Based UI** – Lightweight frontend for intuitive and responsive usage.

## 📁 Project Structure

```bash
Medical-Diagnostic-Tool/
├── classification/         # MRI classification scripts and model
├── segmentation/           # Tumor segmentation scripts and model
├── validation/             # MRI image verification logic
├── frontend/               # HTML, CSS, JS UI files
├── backend/                # Backend code and model folder
│   └── models/             # Pretrained model files
├── main.py                 # Main script (if needed)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## ⚙️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Python (TensorFlow, OpenCV)
- **Models**: CNNs for classification, U-Net for segmentation
- **No APIs Used** – Fully self-contained and offline-capable

---

## 🧩 How to Download and Run the Project

### 🔽 1. Clone the Repository

```bash
git clone https://github.com/WIZARD3022/Medical-Diagnostic-Tool.git
cd Medical-Diagnostic-Tool
```

### 💾 2. Download Pretrained Model

Download the model file from the link below:

🔗 [Download Model from MEGA](https://mega.nz/file/N6ExzRjJ#d0C0GdHaQYc-gG58vs_ts_J-G_Yu4WP2wdaZUx6C7cM)

- After downloading, place the model file in:  
  ```bash
  backend/models/
  ```

### 🟢 3. Run the Node Server

Navigate to the backend directory and run:

```bash
cd backend
npm install
node server.js
```

Or if you're using `nodemon`:

```bash
nodemon server.js
```

### 🌐 4. Open the Frontend

Just open the `frontend/index.html` file in any modern browser.

✅ You're good to go!

---

## 🌱 Future Scope

- Add more disease categories
- Extend to other imaging types (e.g., CT, PET, Ultrasound)
- Improve accuracy with more diverse datasets
- Host the app with GPU backend for faster inference

---

## 📄 License

This project is released under the [MIT License](LICENSE).

---
