from fastapi import FastAPI
from user import api as UserAPI
from tortoise.contrib.fastapi import register_tortoise
import uvicorn

app = FastAPI()
app.include_router(UserAPI.app)

register_tortoise(
    app,
    db_url="postgres://postgres:root@127.0.0.1/fastapi",
    modules={'models': ['user.models']},
    generate_schemas=True,
    add_exception_handlers=True
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
