# Samaro_Round-1_Task

## Project Description

This project is designed to create a simple e-commerce platform with two main components: a Django backend for managing products and transactions, and an Angular frontend for the user interface. The goal of this project is to allow users to view products, make purchases, and capture payment details using a payment provider Stripe.

### Features

- **Product Management**: Create a Django backend that includes a Product table with three different offerings for sale.
- **User Interface**: Develop an Angular frontend with a single homepage to showcase the available products and "Buy" buttons.
- **Payment Integration**: Implement payment processing using a sandbox payment provider to capture payment status and transaction data.
- **User Notifications**: Provide real-time success notifications to users upon successful payment.

### Technologies Used

- **Django Backend**: A powerful Python web framework used for creating the backend server, managing products, and capturing transaction data.
- **Angular Frontend**: A popular TypeScript-based framework used to create a user-friendly frontend interface.
- **Stripe Payment Integration**: Stripe is employed as the primary payment provider, allowing users to make secure transactions.
- **Tailwind CSS**: A utility-first CSS framework that simplifies the styling and design of the application.
- **PostgreSQL (Psql)**: An open-source relational database management system, used to store product and transaction data.

## Usage

1. Access the frontend by opening your browser and navigating to `http://localhost:4200`.

2. The homepage will display the available products with "Buy" buttons.

3. Click the "Buy" button to initiate the payment process through Stripe.

4. Complete the payment using the sandbox payment provider.

5. The backend will capture payment status, transaction ID, and other relevant data.

6. On successful payment, the frontend will display a real-time notification with the message "Success."

[See the image](https://imgur.com/751mw1r)

Watch the video for a demonstration: https://youtu.be/GAOA2paDGY8

## Acknowledgments

- This project was created as a learning exercise and for demonstration purposes.
- Special thanks to the developers of Stripe, Tailwind CSS, PostgreSQL, Django, and Angular for their valuable tools and services.
