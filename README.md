# Project Setup

## Environment Variables
Create a `.env` file and declare your own email settings:
```
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=
```

## Database Setup
This project uses SQLite (`db.sqlite3`). Ensure your database is set up before running the project.

## Functionalities
- User can log in.
- User can register an account.
- User can reset their password via email (uses Brevo as the sender).

## Custom User Model
This project utilizes Django's built-in user model, referred to as `UserAccount`. The default Django authentication libraries are maximized for efficiency.

