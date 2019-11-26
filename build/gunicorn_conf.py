import json
import multiprocessing
import os

workers_per_core_str = os.getenv("WORKERS_PER_CORE", "1")
web_concurrency_str = os.getenv("WEB_CONCURRENCY", None)
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "80")
use_loglevel = os.getenv("LOG_LEVEL", "info")
timeout_str = os.getenv("TIMEOUT", "30")

cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores
if web_concurrency_str:
    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0
else:
    web_concurrency = max(int(default_web_concurrency), 2)

# Gunicorn config variables
loglevel = use_loglevel
bind = f"{host}:{port}"
workers = web_concurrency
timeout = int(timeout_str)
keepalive = 120
errorlog = "-"

# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "timeout": timeout,
    "keepalive": keepalive,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "host": host,
    "port": port,
}

print(json.dumps(log_data))
