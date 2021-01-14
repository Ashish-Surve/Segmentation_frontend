FROM python:3.8-slim

ENV GIT_PYTHON_REFRESH=quiet
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]