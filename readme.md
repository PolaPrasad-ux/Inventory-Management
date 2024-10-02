# Django Redis Caching API

This project demonstrates how to use *Redis* for caching API responses and database queries in a Django application with Class-Based Views (CBVs).

## Features

- *Redis Caching*: Caches API responses and database queries to improve performance and reduce load.
- *Django CBV (Class-Based Views)*: Utilizes Django's powerful CBVs for structured and reusable code.
- *Flexible Caching*: Supports manual and automatic caching with Django's built-in cache_page decorator.
- *Custom Cache Logic*: Uses a base view class for custom caching across multiple APIs.
## Technologies

- Python 
- Django 
- Redis
- Django-Redis
- Requests (for external API requests)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-redis-caching-api.git



## Install the requirements in requirements.txt
'localhost:8000/inventory/items/'-"To retreive and post the items to inventory"

'localhost:8000/inventory/items/<int:pk>/'-"To retreive,update and delete the items to inventory for the particular item"

'localhost:8000/items/query/<str:category>/'-"To retreive the items based category we requested"

'localhost:8000/items/sort/'-"To sort the items based on their price"

tests.py file to test the APIs.

Used Redis for caching API responses for faster access.

## Authentication
JWT Authentication through Refresh and Access Tokens for the methods "GET,POST,DELETE"  by using "[IS AUTHENTICATED]" permission classes

##Logging

Logger classes for debugging, info and errors.