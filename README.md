# Hospital Management System (HMS)

A Python Flask API for managing patient records with full CRUD, email notifications, batch age calculations, web scraping, and structured logging.

## Features

- REST API for Patient `{id, name, age, disease}` with SQLite persistence
- Email notification on patient creation (background thread)
- Batch average age calculation (threads or asyncio)
- Web scraping for hospital/disease info
- Structured JSON logging
- Centralized exception handling
- Unit tests with `pytest`
- CLI client for easy interaction

## Setup & Run

1. Clone repo and install dependencies:

```bash
pip install -r requirements.txt
