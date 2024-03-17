FROM python:3.10.12

RUN apt-get update && apt-get install -y texlive
# RUN conda update -n base -c defaults conda

COPY .. /app
WORKDIR /app
RUN pip install alexlatexgen

CMD ["python", "test2_2.py"]