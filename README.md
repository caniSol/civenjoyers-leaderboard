# A leaderboard for our regular CIV 6 games
0% AI included, everything is coded by my hand as exercise. I'm definitely not a designer, so the CSS is kinda garbage.

# Security notice
Currently there are no security measures implemented for SSL or HTTPS, the app is intended to be run behind a reverse proxy which takes care of these things.

# Installation
The repo is supposed to be built as a docker image.

## Variables
These environment variables have to be set: 
"DJANGO_SUPERUSER_PASSWORD"
"SECRET_KEY"

## Database
The project uses a local sqlite DB, you have to provide a docker volume or bind mount for the /app/data directory inside the container.

# Open TODOs
- [ ] User registration and Login
- [ ] Permissions system
- [ ] Page for users to submit new games and players
- [ ] Fix standings (higher place with more wind when even in elo, same place when both is identical)
- [ ] Option to use Postgres just for educational purposes
