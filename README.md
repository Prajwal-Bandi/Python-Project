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



---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/USERNAME/REPO_NAME.git
    cd REPO_NAME
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Configuration

Edit `app/config.py` to set:

- `SQLALCHEMY_DATABASE_URI` for your SQLite DB location
- SMTP settings (`SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`)
- Email addresses (`EMAIL_FROM`, `EMAIL_TO`)
- Batch size for average age calculation (`BATCH_SIZE`)

---

## Usage

### Running the Server

```bash
python run.py
