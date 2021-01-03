FROM python:3.9-buster

# set work directory
WORKDIR /app

# copy source
COPY . .

# run uvicorn
CMD ["uvicorn", "main:app", "--reload"]