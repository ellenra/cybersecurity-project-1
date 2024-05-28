# Cyber Security Base: Project I
This project is for Cyber Security Base 2024 course. This is a simple web application where users can register, login, create chats and have conversations on existing chats.
The main goal is to incorporate at least five different security flaws from the OWASP [top ten list](https://owasp.org/www-project-top-ten/) and demonstrate how to fix them.



## Installation instructions

1. Install PostgreSQL if you haven't already. If you have fuksilappari, follow [these](https://github.com/hy-tsoha/local-pg) instructions. Otherwise you can use for example [these](https://www.postgresql.org/download/) instructions.
2. Clone the repository and navigate to its root.
   
   ```
   $ git clone git@github.com:ellenra/cybersecurity-project-1.git
   $ cd cybersecurity-project-1
   ```
3. Set up a PostgreSQL database and copy the contents of the file schema.sql into the database (Make sure your PostgreSQL database server is running)
   
   ```
   $ createdb chatroom
   $ psql chatroom < schema.sql
   ```
6. Create and activate the virtual environment
   
   ```
   $ python3 -m venv venv
   $ source venv/bin/activate
   ```
7. Create .env file in the root directory and add the following
   
   ```
   DATABASE_URL=<database-url>
   SECRET_KEY=<secret-key>
    ```
9. Install dependencies
    
   ```
   $ pip install -r ./requirements.txt
   ```
11. Now you can start the application with this command
    
   ```
   $ flask run
   ```
