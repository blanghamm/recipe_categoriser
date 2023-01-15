# Recipe Categoriser

### Setup
To get started run this command after cloning the project  
``docker-compose up -d``

To start the server and create the database tables  
``docker-compose exec app uvicorn app.main:app --reload --port 8000 --host 0.0.0.0``