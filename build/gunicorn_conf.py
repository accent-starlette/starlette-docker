import json
import multiprocessing
from os import getenv


workers_per_core_str = getenv("WORKERS_PER_CORE", "1")
workers_str = getenv("WORKERS", None)
host = getenv("HOST", "0.0.0.0")
port = getenv("PORT", "80")
loglevel_str = getenv("LOG_LEVEL", "info")
timeout_str = getenv("TIMEOUT", "30")
max_requests_str = getenv("MAX_REQUESTS", "250")

workers_per_core = float(workers_per_core_str)

if workers_str:
    num_workers = int(workers_str)
    assert num_workers > 0
else:
    cores = multiprocessing.cpu_count()
    num_workers = max(int(workers_per_core * cores), 2)

# Gunicorn config variables
bind = f"{host}:{port}"
workers = num_workers
max_requests = int(max_requests_str)
timeout = int(timeout_str)
preload_app = True
loglevel = loglevel_str
accesslog = "-"
errorlog = "-"

# For debugging and testing
log_data = {
    "bind": bind,
    "workers": workers,
    "max_requests": max_requests,
    "timeout": timeout,
    "preload_app": preload_app,
    "loglevel": loglevel,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "host": host,
    "port": port,
}

print(json.dumps(log_data))
