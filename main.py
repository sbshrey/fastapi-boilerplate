from fastapi import FastAPI
from db.engine import db
from routers.users import router as users

app = FastAPI()
app.include_router(users)


@app.get('startup', tags=['system'])
async def startup():
    await db.connect()


@app.get('shutdown', tags=['system'])
async def shutdown():
    await db.disconnect()


@app.get('/ping', tags=['system'])
async def ping():
    return {'ok': 'ok'}
