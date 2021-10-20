FROM python:3
WORKDIR .
COPY . .
RUN python3 -m pip install -r requirements.txt
CMD ["main.py"]
ENTRYPOINT ["python3"]
