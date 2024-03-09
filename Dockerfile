FROM python:3.12

WORKDIR /src

ADD ./ /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 

ENTRYPOINT ["hypercorn", "main:app"]

HEALTHCHECK --interval=5m --timeout=3s \
    CMD curl -f http://localhost:8000/ || exit 1
