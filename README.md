# Bike Management Application

This is a Django application for managing a database of bikes, including functionalities for creating, editing, deleting, and viewing bikes.

## Project Structure

The project is divided as follows:

APP_MOTORCYCLES/
├── app_motorcycles/
│ ├── pycache/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── bikes_api/
│ ├── pycache/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── static/
│ │ ├── css/
│ │ ├── bikes.css
│ ├── templates/
│ ├── bikes_api/
│ ├── bike_form.html
│ ├── bike_list.html
├── db.sqlite3
├── manage.py


## How it Works

### Models

The `models.py` file contains the definition of the Bike model, which represents the bike data stored in the database.

### Serializers

The `serializers.py` file contains the BikeSerializer class, which converts the Bike model instances to JSON and vice versa.

### Views

The `views.py` file contains the views for handling bike-related operations, including:

- `BikeListView`: For viewing the list of bikes.
- `BikeCreateView`: For creating a new bike.
- `BikeEditView`: For editing an existing bike.
- `BikeDeleteView`: For deleting a bike.

### URLs

The `urls.py` file contains the URL patterns for the bike-related views.

### Templates

The `templates/bikes_api/` directory contains the HTML templates for the bike form and the bike list.

### Static Files

The `static/css/` directory contains the CSS files for styling the templates.

## How to Run the Project

1. **Clone the repository:**
    ```sh
    git clone [<repository-url>](https://github.com/BlackT1221/App_Motorcycles/)
    cd APP_MOTORCYCLES
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/bikes/view/` to view the list of bikes.

## Usage

- **View Bikes:**
  Visit `http://127.0.0.1:8000/bikes/view/` to see the list of bikes.

- **Add a New Bike:**
  Click on "New Bike" in the navigation bar to open the bike creation form.

- **Edit a Bike:**
  Click on "Edit" next to a bike to open the bike edit form.

- **Delete a Bike:**
  Click on "Delete" next to a bike to delete it from the database.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.
