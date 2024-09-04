import os


bind = "0.0.0.0:5000"
workers = os.environ.get("GUNICORN_WORKERS", 1)
timeout = os.environ.get("GUNICORN_TIMEOUT", 300)
threads = os.environ.get("GUNICORN_THREADS", 16)
keepalive = 24 * 60 * 60
statsd_host = os.environ.get("STATSD_EXPORTER")
statsd_prefix = os.environ.get("STATSD_PREFIX")
