FROM python:3.12-slim-bookworm

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies (if we had any):
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Run the application:
COPY *.py .
COPY restaurants.csv .
CMD ["python", "restaurants.py"]
