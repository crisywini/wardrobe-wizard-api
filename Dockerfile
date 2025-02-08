FROM python:3.12.8-slim-bookworm

WORKDIR /app


COPY src/ /app/src/
COPY run.sh /app/
COPY __init__.py /app/

RUN chmod +x /app/run.sh

RUN pip install --no-cache-dir -r /app/src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "/app/run.sh"]

