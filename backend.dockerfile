FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


EXPOSE 80

COPY $path /app

RUN pip install -r ./backend/requirment.txt

RUN cd backend

RUN pwd

RUN ls

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]