
## AQUAPURGE: Autonomous Water Cleaning Bot

AQUAPURGE is a fully integrated autonomous robot designed to clean water surfaces while monitoring environmental quality in real-time. Built with advanced Machine Learning (YOLOv5n), embedded systems (STM32 + FreeRTOS), and IoT technologies (Adafruit, GPS, TDS, and pH sensors), the bot offers a scalable and efficient solution to combat aquatic pollution.

> *“Bringing intelligent, scalable, and green technology to save our water bodies.”*

---

## Features

- **Trash Detection** using YOLOv5n (86% mAP@0.50)
- **Autonomous Navigation** powered by FreeRTOS and brushless motors
- **Environmental Monitoring** with TDS and pH sensors
- **Real-Time Tracking** via GPS and Adafruit Cloud
- **Remote Control Interface** using the Blynk mobile app
- **Solar-Powered & Sustainable Design**
- **Future Upgrade:** V2X communication for multi-bot coordination

---

## Project Overview

![image](https://github.com/user-attachments/assets/5dc23128-95cf-409a-bb92-3d4c5788def5)

---

## System Architecture

### 1. Hardware

- STM32 Microcontroller
- NRF2401L Transceivers
- Brushless Motors
- GPS Module
- TDS and pH Sensors
- 9.6W Solar Panel
- 3S 18650 Battery Pack (Receiver: 48Wh, Transmitter: 24Wh)

### 2. Embedded Systems

- **FreeRTOS-based Task Management**  
  Task priority: RF > Trash collection > Navigation
- **Manual Remote Control**  
  Joystick + Potentiometer via SPI to STM32
- **PID Motor Control** for precision

![image](https://github.com/user-attachments/assets/f9d4221b-727b-4695-bbb6-22cf797f898f)

### 3. IoT System

- Real-time data via Adafruit Cloud
- Socket communication for GPS, pH, and TDS data
- Blynk mobile app for monitoring and remote control

---

## Machine Learning Model

**YOLOv5n** is used for real-time trash detection:

- **Datasets:** TACO + LITR + Drinking Waste
- **Performance:** 86% mAP@0.50
- **Data Augmentation:** Rotation, flipping, color shifts, crop, blur
- **Hyperparameter Tuning:** Ray Tune

### Confusion Matrix

| Metric         | Value |
| -------------- | ----- |
| True Positive  | 87%   |
| True Negative  | 81%   |
| False Negative | 19%   |
| False Positive | 13%   |

---

## Power Analysis

| Component   | Battery Capacity | Power Use | Operating Time |
| ----------- | ---------------- | --------- | -------------- |
| Receiver    | 48Wh             | 12W       | 4 hours        |
| Transmitter | 24Wh             | 0.24W     | 100 hours      |
| Solar Panel | 9.6W             | ~4.5h to full charge (ideal conditions) | — |

---

## Repository Structure

```

AQUAPURGE/
│
├── hardware/
│   ├── stm32\_transmitter\_code/
│   ├── stm32\_receiver\_code/
│   └── PCB\_schematics/
│
├── iot/
│   ├── server\_socket.py
│   ├── blynk\_dashboard.json
│   └── adafruit\_config.py
│
├── ml\_model/
│   ├── train.py
│   ├── yolov5n\_config.yaml
│   ├── datasets/
│   └── weights/
│
├── images/
│   └── aquapurge\_bot.jpg
│
├── results/
│   └── performance\_metrics.pdf
│
├── run.sh
├── README.md
└── LICENSE

````

---

## 🛠 How to Run

### 1. Train the Model

```bash
cd ml_model
python train.py --data datasets/merged.yaml --weights yolov5n.pt
````

### 2. Flash the Embedded Code

Use STM32CubeIDE or PlatformIO to upload `main.c` to the STM32 microcontroller.

### 3. Run the IoT Server

```bash
cd iot
python server_socket.py
```

### 4. Mobile Monitoring

* Open the Blynk app.
* Load `blynk_dashboard.json`.
* Connect to your device and monitor live data.

---

## 📊 Performance Metrics

| Metric   | Value             |
| -------- | ----------------- |
| mAP\@50  | 86%               |
| Coverage | 10m radius        |
| Speed    | 0.6 m/s           |
| Water pH | Alert if < 6.5    |
| TDS      | Real-time updates |

---

## Future Work

* Full navigation autonomy with dynamic path planning
* V2X-based master-slave coordination
* Expand trash detection to more classes with YOLOv8
* Integration with municipal waste response systems

---

## IoT Execution Details

### Run All Clients & Servers

```bash
./run.sh
```

This script initializes:

* **Servers:**

  * `server_ada.py`: Handles Adafruit Cloud integration.
  * `server_blynk.py`: Manages Blynk mobile app integration.

* **Clients (auto-run in terminals):**

  * `client_tds.py`: Sends TDS sensor data.
  * `client_ph.py`: Sends pH sensor data.
  * `client_gps.py`: Sends GPS coordinates.
  * `client_ada.py`: Reads Adafruit Cloud alerts.
  * `client_pump.py`: Receives pump status from mobile.
  * `client_belt.py`: Receives belt status from mobile.

---










