FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || true
RUN pip install --no-cache-dir pytest

CMD ["pytest"]