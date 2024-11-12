# Hot-Fenix-Band-Website

Welcome to the **Hot Fenix** music band website project! This is a Django-based web application dedicated to a fictional band, showcasing their music, tour dates, and latest news. It features user authentication, exclusive access to certain sections, and a visually appealing front-end created with Bootstrap.

---

## Table of Contents

1. [Project Description](#project-description)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [Credits](#credits)
5. [License](#license)
6. [Contribution Guidelines](#contribution-guidelines)

---

## Project Description

The **Hot Fenix** website was created to represent a fictional band’s online presence. This project showcases essential web development skills, including Django, user authentication, Bootstrap-based design, and restricted content areas. Key features include:
- A homepage with a 'Listen Now' button leading to a login page.
- User login and registration.
- A blog section highlighting world tour dates, destinations, and Grammy Awards news.
- Restricted content, such as a "More Music Coming Soon!" page available to logged-in users only.
- Integrated social media icons and responsive design.

---

## Installation Instructions

To run this project locally, ensure you have the following installed:
- Python 3.x
- Django
- Git

Follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Hot-Fenix-Band-Website.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd Hot-Fenix-Band-Website
    ```

3. Install dependencies (consider using a virtual environment):
    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

6. Open a web browser and go to `http://127.0.0.1:8000` to view the website.

---

## Usage Instructions

1. **Homepage**: The landing page showcases the Hot Fenix band with a 'Listen Now' button.
   - **Login Requirement**: Users must log in to access restricted sections of the website.

2. **Login and Registration**: Users can create an account or log in to gain access to exclusive content.
   - After logging in, users are redirected to a "More Music Coming Soon!" page with social media icons and a background image.

3. **Blog**: Check out the latest tour dates, destinations, and band achievements, including Grammy Awards news.

![Homepage Screenshot](path/to/homepage_screenshot.png)
![Login Page Screenshot](path/to/login_screenshot.png)

---

## Credits

- **Developer**: [Bennedict Mahlawule](https://github.com/bennedixt)
- **Framework**: [Django](https://www.djangoproject.com/)
- **UI Library**: [Bootstrap](https://getbootstrap.com/)

Special thanks to online Django and Bootstrap communities for documentation and tutorials.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as you see fit.

---

## Contribution Guidelines

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
