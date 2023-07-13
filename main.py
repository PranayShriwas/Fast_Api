from fastapi import FastAPI
from user import api as UserApi
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(UserApi.app)


register_tortoise(
    app,
    db_url="postgres://postgres:root@127.0.0.1/fastapi",
    modules={'models':['user.models']},
    generate_schemas=True,
    add_exception_handlers=True
)
