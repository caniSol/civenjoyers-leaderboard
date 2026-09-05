uv run python manage.py migrate
uv run python manage.py makemigrations elo
uv run python manage.py migrate
uv run python manage.py createsuperuser --noinput --username admin --email noreply@example.com
uv run python manage.py collectstatic --noinput
uv run python -m uvicorn civenjoyers_config.asgi:application --host 0.0.0.0 --log-level debug
