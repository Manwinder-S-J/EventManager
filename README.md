# Event Manager

## Overview
This Event Registration System is a web application built with Django server, Python, HTML, CSS, and Bootstrap.
</br>There are two types of groups:</br>
- Administrators
- Registrants(users)</br>
This project facilitates event management, allowing administrators to create, update, delete events, delete users from an event, and generate reports on users and registrations. Registrants can create accounts, register for events, and view their registration details.

## Accounts
### Admin
- **username**: admin
- **password**: Admin123

### Registrants
- **usernames**: SamS, JackB, JackS, JohnJ, Jordan, JesseJ, MIkeM, JohnD, 
- **passwords**: Idontknow123
  
## Features

### Accounts
- **Create**: New users can sign up with a validated username (email) and secure password + possibility to craete a new account
- **Login/Logout**: Both administrators and registrants can log in and out of the system.
- **Role-based Access Control**: Pages and actions are restricted based on user role and authentication status.

### Events
- **Management**: Administrators can manage events, including creating, updating, cascading deletions, removing users from events
- **Registration**: Registrants can sign up or cancel their registration for events.
- **Search**: A comprehensive search feature for registrants to find and register for events.

### Reports
- **User List**: Viewable by administrators with details including full names and roles.
- **Event List**: Both roles can view upcoming events, with administrators having additional filters for date ranges and viewing past events.
- **Registrant Events**: Registrants can view a list of events they're registered for.
- **Event Registrants**: Administrators can view a list of events along with their registrants.

## Data Model
The application uses a straightforward data model that includes Users, Groups, Events, and a many-to-many relationship for Registrations.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Manwinder-S-J/EventManager.git
```
2. Navigate to the project directory:
```bash
cd eventManager_project
```
3. Run migrations to set up the database:
```bash
python manage.py migrate
```
5. Create an admin account:(optional)
```bash
python manage.py createsuperuser
```
6. Run the server:
```bash
python manage.py runserver
```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Log in as an administrator to manage events and users.
- Register as a new user to start enrolling in available events.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open-sourced under the [MIT License](LICENSE).
