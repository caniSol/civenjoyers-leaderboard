FROM python:3
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

ENV UV_NO_DEV=1

WORKDIR /app
RUN chmod +x entry.sh
RUN rm /app/civenjoyers_config/settings.py
RUN mv /app/civenjoyers_config/prod_settings.py /app/civenjoyers_config/settings.py
RUN uv sync --locked

EXPOSE 8000

CMD [ "/bin/bash", "entry.sh" ]
