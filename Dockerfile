FROM python:3.12-slim-bookworm

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies (our only requirements are only needed for running tests):
# COPY requirements.txt .
# RUN 

# Run the application:
COPY *.py .
COPY restaurants.csv .
CMD ["python", "restaurants.py"]
