# User Authentication System

This project implements a secure user authentication system using Python and Flask as part of a Cyber Security internship.

## Features
- User registration with password hashing (bcrypt)
- Secure login with JWT-based authentication
- Protected routes accessible only with valid tokens
- Role-based access control (user/admin)

## Technologies Used
- Python
- Flask
- bcrypt
- JWT (PyJWT)

## Security Practices
- Passwords are never stored in plain text
- Tokens are time-limited for security
- Authorization is enforced using roles
- Follows OWASP authentication best practices

## Purpose
This project was developed for educational purposes to demonstrate secure authentication mechanisms.

## Disclaimer
This is an academic implementation and not intended for production use.
