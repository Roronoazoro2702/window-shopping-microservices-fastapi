# Inventory and Payment Microservices

This project demonstrates a **microservices architecture** using FastAPI and Redis Streams for event-driven communication between two services: **Inventory** and **Payment**. It manages products, orders, and real-time updates to inventory and order statuses through asynchronous communication.

---

## Features

- **Inventory Service**: 
  - Manage product inventory.
  - Adjust inventory when an order is completed.
  - Handle errors by publishing refund events.

- **Payment Service**: 
  - Process orders and simulate payment confirmations.
  - Publish order completion events for inventory updates.
  - Handle refund events to update order statuses.

- **Event-Driven Communication**:
  - Uses Redis Streams for communication between services.
  - Implements consumer groups for scalable, asynchronous processing.

---

## Architecture

This project follows an **event-driven microservices architecture** with Redis as the messaging broker.

### Services

1. **Inventory Service**:
   - Manages `Product` entities.
   - Consumes events from the `order_completed` stream.
   - Publishes events to the `refund_order` stream on error.

2. **Payment Service**:
   - Manages `Order` entities.
   - Publishes events to the `order_completed` stream after processing orders.
   - Consumes events from the `refund_order` stream.

### Redis Streams

- **order_completed**: 
  - Published by the payment service after an order is completed.
  - Consumed by the inventory service to update product quantities.

- **refund_order**: 
  - Published by the inventory service if a stock update fails.
  - Consumed by the payment service to mark orders as refunded.

---

## Requirements

- Python 3.9+
- Redis server
- FastAPI
- Redis-OM
- Requests

---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Roronoazoro2702/window-shopping-microservices-fastapi.git
cd window-shopping-microservices-fastapi

