FROM python:3.10-slim
RUN pip install pyspark scikit-learn pandas numpy matplotlib seaborn
WORKDIR /app
COPY . .
CMD ["python","scripts/run_pipeline.py"]
