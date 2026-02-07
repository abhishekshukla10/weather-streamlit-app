# 🌤️ Weather Streamlit App (Docker + Render)

A simple and production-ready weather application built using **Streamlit**, containerized with **Docker**, and deployed on **Render**.  
The app fetches real-time weather information using the **WeatherAPI** based on the city entered by the user.

---

## 🚀 Live Demo

👉 https://weather-streamlit-app.onrender.com

---

## 📌 Features

- 🌍 Search weather by city name
- 🌡️ Displays temperature in Celsius
- 💨 Shows wind speed
- 🔐 Secure API key handling using environment variables
- 🐳 Dockerized for consistent deployment
- ☁️ Deployed as a Docker Web Service on Render

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **API**: WeatherAPI.com  
- **Containerization**: Docker  
- **Hosting**: Render  
- **Version Control**: Git & GitHub  

---

## 🏗️ Architecture Overview

### Architecture Flow

1. User accesses the application through a web browser.
2. The request is routed to a **Render Web Service**.
3. Render runs the application inside a **Docker container**.
4. The Streamlit app listens on a **dynamic port (`$PORT`)** assigned by Render.
5. The app reads the **Weather API key** from environment variables.
6. Weather data is fetched from **WeatherAPI.com**.
7. The response is rendered back to the user interface.

---

### Configuration & Secrets Handling

- **Local Development**
  - API key stored in `.env` file (ignored by GitHub)
- **Cloud Deployment (Render)**
  - API key injected via Render Environment Variables
- No secrets are hard-coded in the source code.


## 📂 Project Structure

weather-streamlit-app/
│
├── app.py # Streamlit application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── .dockerignore # Docker ignore rules
├── .gitignore # Git ignore rules
├── README.md # Project documentation


☁️ Deployment on Render

Push the code to GitHub

Create a Render Web Service

Select Environment = Docker

Add WEATHER_API_KEY as an environment variable

Deploy the service

Render automatically builds the Docker image and runs the container.


🧠 Key Learnings

Docker-based deployment with dynamic port handling

Secure environment variable management

Debugging API authentication issues

Cloud-native Streamlit deployment


👤 Author

Abhishek Shukla
GitHub: https://github.com/abhishekshukla10
