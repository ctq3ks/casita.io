## Casita

This Django web application is designed to assist salon professionals in delivering their services to clients at their homes or businesses. Whether you're a hairstylist, makeup artist, nail technician, or any other beauty professional, this app can help streamline your booking, scheduling, and service delivery process.

## Overview

The Professional Services Concierge app aims to provide a user-friendly platform for both salon professionals and their clients. Salon professionals can create profiles, list their services, set their availability, and accept bookings from clients. Clients, on the other hand, can search for professionals, view their portfolios, and book appointments based on their availability.

## Setup

### Prerequisites

Before you can run the app locally, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Virtualenv (optional but recommended)
- PostgreSQL (or another database of your choice)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ctq3ks/casita.io.git
   ```

2. Navigate to the project directory:

   ```bash
   cd casita.io
   ```

3. Create and activate a virtual environment (recommended):

   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

4. Create a PostgreSQL database for the app and update the database settings in `psc/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Running the App

Now that you've completed the setup, you can run the app locally:

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. Open your web browser and go to `http://localhost:8000` to access the app.

---
