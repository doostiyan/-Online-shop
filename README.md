# Online Shop

An e-commerce platform built with Django and templates, offering a user-friendly shopping experience with a focus on performance and ease of use. The platform includes features like a session-based shopping cart, OTP-based mobile registration, and image uploading with Celery and RabbitMQ.

## Features

- **Built with Django & Templates:** Developed using Django with a clean and efficient template-based front-end.
- **Session-Based Shopping Cart:** Add products to your cart and manage them easily without the need for user registration.
- **Mobile Registration with OTP:** Secure sign-up and login process using mobile numbers and OTP codes.
- **Image Uploads with Celery & RabbitMQ:** Asynchronous image uploading handled by Celery, with RabbitMQ as the message broker to enhance performance and reliability.
- **Zarinpal Payment Gateway:** Integrated with Zarinpal for secure and reliable payment processing.
- **Product Catalog:** Browse a wide range of products with detailed descriptions and images.
- **Search & Filter:** Easily find products using search and filter options.
- **Responsive Design:** Fully responsive layout for a great user experience on any device.

## Getting Started

### Prerequisites

- Python 3.10+
- Django 4.0+
- Celery
- RabbitMQ (for Celery broker)
- Virtualenv (optional but recommended)
- PostgreSQL (or any other preferred database)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/doostiyan/-Online-shop
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your database settings, RabbitMQ, and Zarinpal API keys in `settings.py`.**

5. **Apply the migrations:**

    ```bash
    python manage.py migrate
