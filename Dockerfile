FROM python:3.7
ADD try1.py .
RUN pip install numpy
CMD ["python","./try1.py"]