FROM python:3
WORKDIR /
RUN pip install requests
COPY parse_variants.py /
ENTRYPOINT ["python3", "/parse_variants.py"]
