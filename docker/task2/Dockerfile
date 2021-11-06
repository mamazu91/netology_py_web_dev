FROM python
ENV PROJPATH=/crud
WORKDIR $PROJPATH
COPY ./3.2-crud/ .
RUN pip install -r stocks_products/requirements.txt
CMD ["python3","stocks_products/manage.py", "runserver", "0.0.0.0:8000"]
