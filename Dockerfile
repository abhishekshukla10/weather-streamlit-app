# 1️⃣ Base image
FROM python:3.12-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy requirements first (cache-friendly)
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy app code
COPY . .

# 6️⃣ Expose Streamlit port
#EXPOSE 8501

# 7️⃣ Streamlit config for Docker
#ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# 8️⃣ Run the app
#CMD ["streamlit", "run", "app.py"]
CMD ["sh", "-c", "streamlit run app.py --server.port=$PORT --server.enableCORS=false"]
