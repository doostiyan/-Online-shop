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

4. **Install Celery:**

    Celery should be included in your `requirements.txt`, but if not, you can install it manually:

    ```bash
    pip install celery
    ```

5. **Configure your database settings, RabbitMQ, and Zarinpal API keys in `settings.py`.**

6. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Start RabbitMQ Server:**

    Ensure RabbitMQ is running. You can start it with:

    ```bash
    sudo service rabbitmq-server start
    ```

8. **Start Celery Worker:**

    Start Celery with RabbitMQ as the broker:

    ```bash
    celery -A your_project_name worker -l info
    ```

9. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

10. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

11. **Visit the site:**

    Open your browser and go to `http://127.0.0.1:8000/`.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please contact us at support@example.com.
