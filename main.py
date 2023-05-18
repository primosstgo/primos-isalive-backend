from docker import from_env as docker_env
from uvicorn import run as uvicorn_run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from components import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/containers")
def containers():
    return list(map(get_container_data, docker_env().containers.list(all=True)))

if __name__ == '__main__':
    uvicorn_run('main:app', reload=True, host='0.0.0.0', port=8003)

