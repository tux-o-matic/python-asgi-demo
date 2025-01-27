# python-asgi-demo
Python web app demo using the Quart framework and the Hypercorn ASGI server.
The goal is to have an ASGI web app ready to be running in a container locally or in K8s.
The app starts a [single asyncio worker programmatically for Hypercorn](https://hypercorn.readthedocs.io/en/latest/how_to_guides/api_usage.html#features-caveat). 

## Local development
```shell
python3 -m venv venv
source venv/bin/activate
pip install -f requirements.txt
```

## Building the image locally
The provided Containerfile makes use of an [s2i Python 3.12 minimal image](https://github.com/sclorg/s2i-python-container/tree/master/3.12-minimal)
```shell
podman build -t python-asgi .
```

## Running the container locally
```shell
podman run -it --rm -e APP_FILE=asgi.py -p 0.0.0.0:8080:8080 python-asgi
```

## For Kubernetes
Configure these things:
- Pass an ENV of `APP_FILE=asgi.py`.
- Set HTTP probes against `/health`.
- Container port and Service should point to `8080`.