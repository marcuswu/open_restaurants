FROM python:3.12-slim-bookworm

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies (our only requirements are only needed for running tests):
# COPY requirements.txt .
# RUN 

# copy the application
COPY *.py .
COPY restaurants.csv .

# Expose the server port
EXPOSE 8000

# Container safety -- don't run as root
RUN useradd app
USER app

# Run the application:
CMD ["python", "server.py"]
