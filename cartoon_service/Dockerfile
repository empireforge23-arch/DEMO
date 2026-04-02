FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py deploy.sh /app/
RUN chmod +x deploy.sh
EXPOSE 5000
CMD ["python3","app.py"]