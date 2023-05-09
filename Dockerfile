FROM python:3.11

RUN mkdir -p /var/wrk
WORKDIR /var/wrk
RUN pip install pandas matplotlib geopandas ipython
