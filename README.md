# Even-Odd Guessing Game Web Application -  Group 8

A Flask-based web application where users can play an Even-Odd guessing game against the computer. The application stores game results in a PostgreSQL database and provides game history.

## Prerequisites

- Docker and Docker Compose
- Git

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/alicenl2/A3-SD-group8
cd A3-SD-group8
```

2. Create a `.env` file in the project root with the following variables:
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=roulette
APP_PORT=5000
```

3. Build and start the containers:
```bash
docker-compose up --build
```

The application will be available at `http://localhost:5000`

## Manual Setup

### Environment Variables

Create a `.env` file with the following variables:

```env
POSTGRES_USER=<your-db-user>
POSTGRES_PASSWORD=<your-db-password>
POSTGRES_DB=<your-db-name>
APP_PORT=<port-number>
```

### Database Setup

The application will automatically:
1. Wait for the PostgreSQL database to be ready
2. Create necessary tables
3. Start the Flask application

### Running the Application

1. Build the containers:
```bash
docker-compose build
```

2. Start the services:
```bash
docker-compose up
```

3. Stop the services:
```bash
docker-compose down
```

## Project Relevant Structure

```
.
├── app.py                  # Main Flask application
├── create_tables.py        # Database initialization script
├── Dockerfile             # Multi-stage build configuration
├── docker-compose.yml     # Service orchestration config
├── requirements.txt       # Python dependencies
├── entrypoint.sh         # Container startup script
└── templates/            # HTML templates
    ├── home.html        # Game interface
    └── results.html     # Game history display
```

## Application Features

- Even-Odd guessing game against computer
- Game history tracking
- PostgreSQL database integration
- Containerized deployment
- Error handling and logging

## Troubleshooting

### Database Connection Issues

If you encounter database connection errors:

1. Ensure PostgreSQL container is running:
```bash
docker ps
```

2. Check container logs:
```bash
docker logs roulette_db
```

3. Connect to database container:
```bash
docker exec -it roulette_db bash
psql -U user roulette
```

### Container Networking Issues

If services can't communicate:

1. Check network status:
```bash
docker network ls
docker network inspect a3-sd-group8_app_network
```

2. Ensure both services are connected to the network:
```bash
docker-compose ps
```

## Security Notes

- Never commit `.env` files to version control
- Keep Docker containers updated
- Use environment variables for sensitive data

