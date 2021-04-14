FROM python:3.8-alpine

WORKDIR /usr/src/app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY maze.py .
COPY simulator.py .
COPY api.py .

CMD [ "python", "./simulator.py" ]