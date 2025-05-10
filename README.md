---

# AQUAPURGE: Autonomous Water Cleaning Bot

AQUAPURGE is a fully integrated autonomous robot designed to clean water surfaces while monitoring environmental quality in real-time. Built with advanced Machine Learning (YOLOv5n), embedded systems (STM32 + FreeRTOS), and IoT technologies (Adafruit + GPS + TDS + pH sensors), the bot offers a scalable and efficient solution to combat aquatic pollution.

---

## 🌊 Features

* **Trash Detection** using YOLOv5n (86% mAP\@0.50)
* **Autonomous Navigation** powered by FreeRTOS and brushless motors
* **Environmental Monitoring** via TDS and pH sensors
* **Real-Time Tracking** with GPS and Adafruit Cloud
* **Remote Control Interface** via Blynk mobile app
* **Solar-Powered & Sustainable**
* **Planned Future Upgrade:** V2X communication for multi-bot coordination

---

## Project Overview

![AQUAPURGE Bot](./images/aquapurge_bot.jpg)

> *“Bringing intelligent, scalable and green technology to save our water bodies.”*

---

## System Architecture

### 1. **Hardware**

* STM32 Microcontroller
* NRF2401L Transceivers
* Brushless Motors
* GPS Module
* TDS and pH Sensors
* Solar Panel (9.6W)
* 3S 18650 Battery Pack (Receiver: 48Wh, Transmitter: 24Wh)

### 2. **Embedded Systems**

* **RTOS Integration:** Prioritized control (RF > Trash collection > Navigation)
* **Manual Remote Control:** Joystick + Potentiometer via SPI to STM32
* **PID Motor Control** for smooth navigation

### 3. **IoT System**

* **Real-time tracking & monitoring** using Adafruit Cloud
* **Socket communication** for GPS, pH, and TDS data
* **Mobile App (Blynk)** to remotely monitor and control the bot

---

## Machine Learning Model

### YOLOv5n for Trash Detection:

* Combined datasets: **TACO + LITR+Drinking Waste**
* Achieved **86% mAP\@50**
* Data Augmentations:

  * Rotation, flipping, color shifts, crop, blur
* Hyperparameter tuning with **Ray Tune**

### Confusion Matrix:

| Metric         | Value |
| -------------- | ----- |
| True Positive  | 87%   |
| True Negative  | 81%   |
| False Negative | 19%   |
| False Positive | 13%   |

---

## Power Analysis

| Component   | Battery Capacity | Power Use                                | Operating Time |
| ----------- | ---------------- | ---------------------------------------- | -------------- |
| Receiver    | 48Wh             | 12W                                      | 4 hours        |
| Transmitter | 24Wh             | 0.24W                                    | 100 hours      |
| Solar Panel | 9.6W             | \~4.5h to full charge (ideal conditions) |                |

---

## Repository Structure

```
AQUAPURGE/
│
├── hardware/
│   ├── stm32_transmitter_code/
│   ├── stm32_receiver_code/
│   └── PCB_schematics/
│
├── iot/
│   ├── server_socket.py
│   ├── blynk_dashboard.json
│   └── adafruit_config.py
│
├── ml_model/
│   ├── train.py
│   ├── yolov5n_config.yaml
│   ├── datasets/
│   └── weights/
│
├── images/
│   └── aquapurge_bot.jpg
│
├── results/
│   └── performance_metrics.pdf
│
├── README.md
└── LICENSE
```

---

## How to Run

1. **Train the Model**

   ```bash
   cd ml_model
   python train.py --data datasets/merged.yaml --weights yolov5n.pt
   ```

2. **Upload Embedded Code**

   * Flash `main.c` to STM32 using STM32CubeIDE or PlatformIO.

3. **Run IoT Server**

   ```bash
   cd iot
   python server_socket.py
   ```

4. **Monitor on Mobile**

   * Open the Blynk app.
   * Load `blynk_dashboard.json` and connect to device.

---

## Performance

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
* Master-slave coordination using V2X
* Expanded trash class detection with YOLOv8
* Integration with municipal response systems

---


