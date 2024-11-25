#Stage 1
FROM python:3.9 as build

WORKDIR /app

COPY requriments.txt .

RUN pip install --no-cache-dir -r requriments.txt

EXPOSE 5000

#Stage 2

FROM python:3.9-slim

WORKDIR /app

COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

COPY . .

ENTRYPOINT ["python"]

CMD ["app.py"]
