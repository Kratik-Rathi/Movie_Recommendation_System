# Movie Recommendation System

**Live App**: https://movie-recommendation-system-adt.streamlit.app/

## Project Overview

The **Movie Recommendation System** is a beginner-friendly web application built with Streamlit that allows users to explore a collection of movies and find recommendations based on various criteria. The app provides an interactive interface to browse movies, apply filters, and search for specific titles. It also includes a manager (admin) interface to manage the movie database. Key features include:

* **Flexible Filtering** – Filter the movie list by **year**, **language**, **country**, **director**, **genre**, or **IMDb rating** to narrow down the selection.
* **Multiple Views** – View the movies in either a **grid format** (e.g. thumbnails or cards) or a **table format** for a more detailed list view.
* **Search Functionality** – Quickly **search** for movies by title to find specific movies.
* **Admin Management** – A **manager login** section allows an authorized user to log in as an admin. The manager can **add new movies** via a simple form (entering details like title, year, etc.) or **delete movies** from the database by title or ID.

This project is great for learning how to build interactive web apps with a database backend, and how to perform basic create/read/delete operations in a web interface.

## Tech Stack

The project is implemented using the following technologies:

* **Frontend**: [Streamlit](https://streamlit.io/) – Streamlit is a Python framework for creating web apps. It handles the UI components and layout for the movie browsing interface.
* **Backend**: **Python** – The core application logic is written in Python. The repository is organized into modules (`app_core` and `system_management` folders) that contain functions for querying the database, filtering data, and managing movies.
* **Database**: **PostgreSQL** – Movie data is stored in a PostgreSQL database. The database is hosted on **Supabase**, a cloud platform that provides PostgreSQL as a service. Supabase is used to store the movie records and execute SQL queries (including some stored procedures for complex operations).

## Folder Structure

The repository is organized into multiple folders, each containing part of the application's code or data. Below is an overview of the important files and directories:

* **`app.py`** – The main Streamlit application file. This is the entry point of the app. Running this file launches the Streamlit web interface.
* **`app_core/`** – Contains core application logic for the recommendation system. This likely includes modules for fetching movie data from the database, applying filters, searching, and displaying results in the Streamlit app.
* **`system_management/`** – Contains management logic for admin features. This includes functionality for manager login, and functions to create (add) a new movie or delete an existing movie by title or ID.
* **`pgadmin_movie_data/`** – Contains CSV data files for movies. These CSV files represent the movie dataset and can be used to initially populate the database. (The name hints that these might be used with PGAdmin or another tool to import data into PostgreSQL.)
* **`sql_queries/`** – Contains SQL script files to set up the database. These include the SQL commands to create the required tables and any stored procedures in the PostgreSQL database. You can run these scripts on your Supabase database (or any PostgreSQL instance) to initialize the schema.

*Other files*: The repository also contains standard configuration files like `requirements.txt` (listing Python dependencies) and potentially a `config.py` or `db_utils.py` for database connection utilities.

## Database Setup

Before running the application, you need to set up the PostgreSQL database with the required tables and procedures:

1. **Create the Database Schema**: On Supabase (or your PostgreSQL server), create a new database (if not already created). Then use the SQL scripts provided in the `sql_queries/` folder to create the necessary tables and stored procedures. In Supabase, you can open the **SQL Editor**, copy the contents of each `.sql` file, and run them. Make sure to execute the table creation scripts first (to create tables like movies, etc.) and then any scripts for stored procedures or additional setup.
2. **Database Credentials**: Once your database is set up, gather the connection details (host, port, database name, username, password). In this project, Streamlit uses a secrets file to store these sensitive credentials.
3. **Streamlit Secrets**: Create a file `.streamlit/secrets.toml` in the project directory (next to `app.py`). This file will hold your database connection info so that the app can connect to the PostgreSQL database. Use the following format in **`secrets.toml`**:

```toml
[postgres]
host = "your-supabase-host-url"      # e.g. "db.abcd1234.supabase.co"
port = 5432                         # the port for PostgreSQL, usually 5432
user = "your-db-user"               # e.g. "postgres"
password = "your-db-password"       # your database user's password
database = "your-db-name"           # the name of the database (e.g. "postgres")
```

Make sure to replace the values with your actual Supabase project’s credentials. In Supabase, you can find these in the project settings (the host will be something like `xxxxxxxx.supabase.co`, and the default port is 5432 for Postgres).

4. **Test the Connection**: (Optional) You might want to test that your database is accessible using these credentials. The Streamlit app will use this information to connect and run queries.

## Running the Project Locally

To run the Movie Recommendation System on your local machine, follow these steps:

1. **Clone the repository**: Clone this GitHub repo to your local system using git or by downloading the ZIP.

   ```bash
   git clone https://github.com/Kratik-Rathi/Movie_Recommendation_System.git
   ```

   Then navigate into the project directory:

   ```bash
   cd Movie_Recommendation_System
   ```
2. **Install dependencies**: Make sure you have **Python 3** installed. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This will install Streamlit and any other libraries listed in `requirements.txt` (such as database drivers like `psycopg2` for PostgreSQL).
3. **Add configuration**: Ensure you have created the `.streamlit/secrets.toml` file as described in the *Database Setup* section above, with your database connection details. This is necessary for the app to connect to the database.
4. **Run the Streamlit app**: Use the Streamlit CLI to run the application:

   ```bash
   streamlit run app.py
   ```

   After running this command, Streamlit will start a local web server. It will usually open a new browser window (or you can navigate to the URL it provides, typically `http://localhost:8501`) to view the app.
5. **Using the app**: In your browser, you should now see the Movie Recommendation System interface. You can use the sidebar or provided controls to filter movies by year, language, etc., switch between grid or table views, and search by title. If you have set up the manager login credentials (see below, in Deployment or code configuration), you can also test logging in as the manager to add/delete movies.

## Deployment

You can deploy this Streamlit app to the cloud so that others can access it via a URL. One convenient option is to use **Streamlit Cloud** (Streamlit's own hosting service):

1. **Push code to GitHub**: Ensure that your latest code is committed and pushed to a GitHub repository (if you have forked or made changes, push them to your GitHub account). In this case, if you're using the original repository and have access, it's already on GitHub.
2. **Sign up for Streamlit Cloud**: Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with your GitHub account.
3. **Create a new app**: Click on **"New App"** on Streamlit Cloud. Connect your GitHub repo by selecting the repository (e.g., `Kratik-Rathi/Movie_Recommendation_System`) and branch (e.g., `main`). Streamlit will detect the `app.py` file automatically as the entry point.
4. **Set up Secrets on Streamlit Cloud**: In the app settings on Streamlit Cloud, you'll need to configure the same database secrets that you used in your local `secrets.toml`. Streamlit Cloud provides a Secrets management section where you can copy-paste the content of your `secrets.toml` (under the `[postgres]` section) or input the fields (host, port, etc.) individually. This will ensure the deployed app can connect to your Supabase/PostgreSQL database.
5. **Deploy the app**: After linking the repo and setting secrets, click **"Deploy"**. Streamlit Cloud will build the app (install dependencies from `requirements.txt`) and launch it. Once deployed, you'll get a shareable URL (like `https://<your-app-name>.streamlit.app`) where the Movie Recommendation System is live.
6. **Manager Login Credentials**: If your app requires a specific manager username/password, make sure those are configured. This might be done via environment variables or stored in the database. (For example, you might have an admin table in the database or a simple check in the code.) On Streamlit Cloud, you could set environment variables or additional secrets if needed for the admin credentials. Then you can log in through the deployed app’s manager login to manage movies.

Deploying on Streamlit Cloud is free for small apps and makes it easy to share the application without users needing to run anything locally.

## License

This project is open source and is released under a license *(to be specified)*. You can include details about the license here. For example, you might choose the MIT License, Apache License 2.0, etc. Make sure to add a `LICENSE` file in the repository if you decide on a license.

*Placeholder: \[License Name] License – e.g., "This project is licensed under the MIT License."*

## Credits

**Creator**: This project was created and is maintained by *Kratik Rathi*. If you have any questions or suggestions, feel free to reach out or open an issue.

**Acknowledgements**: The development was made possible by the following tools and services:

* [**Supabase**](https://supabase.com/) – for providing a hosted PostgreSQL database and convenient management interface.
* [**Streamlit**](https://streamlit.io/) – for the easy-to-use web application framework in Python that powers the frontend.
* **PostgreSQL** – as the robust open-source relational database for storing movie data.

Special thanks to the open-source community for providing tutorials and guidance on building recommendation systems. This project is an educational exercise and a demonstration of how to build a simple movie recommendation/dashboard system with modern tools. Enjoy using the app, and happy movie searching!
