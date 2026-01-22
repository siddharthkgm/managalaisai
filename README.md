# Function Booking Application

A Django-based application for managing function and appointment bookings.

## Features
- **User Authentication**: Sign up, Login, Logout.
- **Admin Management**: Manage Function Types and Venues via the Django Admin panel.
- **Booking System**: Users can browse function types and book appointments.
- **User Dashboard**: Users can view their booking history and status.
- **Modern UI**: Clean, responsive interface using Bootstrap 5.

## Setup Instructions

1.  **Install Dependencies**
    ```bash
    pip install django pillow
    ```

2.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

3.  **Create Superuser (for Admin Access)**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin account.

4.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

5.  **Access the Application**
    -   **Home**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    -   **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Usage Guide

### Admin
1.  Log in to the Admin Panel.
2.  Go to **Events** to add `Function Types` (e.g., Wedding, Birthday) and `Venues`.
3.  Go to **Bookings** to manage user appointments (confirm or cancel).

### User
1.  Sign up for an account.
2.  Browse available Function Types on the Home page.
3.  Click "Book Now" to schedule an appointment.
4.  View your bookings in the "My Bookings" section.
"# managalaisai" 
