# Customer Management 

[In progress 🚧]

This is project for customer management, developed using Python and a layered architecture (Bronze, Silver, Gold) to organize and process data efficiently. The main goal is to create a robust pipeline for managing and analyzing customer information.

## Technologies Used

- **Python 3.12**
- **Streamlit**: For building user interfaces and data visualization.
- **Pandas**: For data manipulation and analysis.
- **Poetry**: For dependency and virtual environment management.
- **SQLAlchemy**: For database connection and querying.

## Layered Architecture

The project follows a layered architecture to process data incrementally and organize it into different refinement levels:

### Bronze Layer:
- Responsible for extracting raw data from the database.
- Converts data into DataFrames for further processing.

### Silver Layer:
- Processes data from the Bronze Layer, performing cleaning and validation.
- Adds structure and organization to the data.

### Gold Layer:
- Applies final transformations and enrichments.
- Data is ready for analysis or visualization.

## How to Run the Project
    Clone the repository:

        git clone <REPOSITORY_URL>
        cd customer-management

## Install dependencies with Poetry:
    -> poetry shell
    -> poetry install

## Set up the environment:
Create a .env file with the necessary database connection details.

    Example .env file:
        -> DATABASE_URL=postgresql://user:password@host:port/database

## Run the pipeline:
    Use the app.py file to execute the pipeline or visualize the data with Streamlit:
        -> streamlit run app.py

## Next Steps
- Create visualizations and reports in Streamlit.
- Improve homepage and data visualization.
- Create page to create and manage customers.
- Write tests for the pipeline.
