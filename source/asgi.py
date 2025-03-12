"""Quart ASGI web app."""

import asyncio
from typing import List
from hypercorn.config import Config
from hypercorn.asyncio import serve
from opentelemetry.instrumentation.asgi import OpenTelemetryMiddleware
from quart import Quart

config: Config = Config()
config.accesslog: str = '-'
config.bind: List[str] = ["0.0.0.0:8080"]
config.errorlog: str = '-'

app: Quart = Quart(__name__)
app.asgi_app = OpenTelemetryMiddleware(app.asgi_app)


@app.route('/')
async def index() -> str:
    """Index"""
    return 'Hello World'


@app.route('/health')
async def health() -> tuple:
    """Heathcheck endpoint"""
    return "OK", 200


asyncio.run(serve(app, config))
