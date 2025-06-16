FROM python:3.11-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

#ENV MSG="Default Message from Docker Flask"
ENV PORT=5000
EXPOSE 5000

CMD ["python3", "app.py"]
