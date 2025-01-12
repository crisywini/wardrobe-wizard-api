FROM python:3.12.8-slim-bookworm

WORKDIR /src

COPY ./src /src
COPY run.sh /src

RUN chmod +x /src/run.sh


RUN pip install --no-cache-dir -r /src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["/src/run.sh"]

