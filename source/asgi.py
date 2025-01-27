"""Quart ASGI web app."""

import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from opentelemetry.instrumentation.asgi import OpenTelemetryMiddleware
from quart import Quart

config = Config()
config.accesslog = '-'
config.bind = ["0.0.0.0:8080"]
config.errorlog = '-'

app = Quart(__name__)
app.asgi_app = OpenTelemetryMiddleware(app.asgi_app)


@app.route('/')
async def index():
    """Index"""
    return 'Hello World'


@app.route('/health')
async def health():
    """Heathcheck endpoint"""
    return "OK", 200


asyncio.run(serve(app, config))
