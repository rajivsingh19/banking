Simple Banking System

Overview

This is a simple banking system built using Streamlit and PostgreSQL with SQLAlchemy as the ORM. It allows users to sign up, log in, deposit, and withdraw money while maintaining session-based authentication.

Features

User Authentication: Signup and Login functionality.

Balance Management: Users can check their balance, deposit, and withdraw funds.

Session State: Users remain logged in until they choose to log out.

Database Integration: Uses PostgreSQL as the database backend.

Requirements

Ensure you have the following installed:

Python 3.8+

PostgreSQL

Required Python libraries (listed below)

Installation

Clone the repository

  git clone https://github.com/rajivsingh19/banking
  cd banking

Install dependencies

  pip install -r requirements.txt

Configure PostgreSQL Database
Ensure PostgreSQL is running and update the DATABASE_URL in the script:

DATABASE_URL = "postgresql://postgres:root@localhost:5432/banking"

Create the database banking if it doesn’t exist:

CREATE DATABASE banking;

Run the Application

  streamlit run app.py

Usage

Signup: Create a new user account.

Login: Use the registered credentials to log in.

Deposit & Withdraw: Enter an amount to deposit or withdraw funds.

Logout: Click the "Logout" button to exit the session.

Technology Stack

Frontend: Streamlit

Backend: SQLAlchemy with PostgreSQL

Authentication: Session state in Streamlit

Future Enhancements

Implement password hashing for better security.

Add transaction history tracking.

Integrate email notifications for transactions.

Enhance UI with better styling.

Contributing

Feel free to fork this repository and contribute by submitting pull requests.

License

This project is licensed under the MIT License.