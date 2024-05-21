# Meal Plan Recommendation App
Meal plan recommendation system that uses content-based filtering to recommend meals based on dietary restrictions and preferences

## Overview

The Meal Plan Recommendation App is a web application designed to help users discover meal recipes based on their nutritional preferences and ingredient requirements. Users can input desired nutritional values, specify ingredients to include or exclude, and receive customized meal recommendations.

## Features

- **Nutritional Filtering**: Customize recommendations based on calories, fat content, protein content, and other nutritional values.
- **Ingredient Inclusion**: Include specific ingredients to cater to dietary preferences.
- **Detailed Recipe Information**: View detailed nutritional information, ingredients, and cooking instructions for each recommended recipe.
- **Interactive UI**: Use a user-friendly interface powered by Streamlit to interact with the app.

## Technologies Used

- **Python**: The core programming language used for the backend and frontend logic.
- **FastAPI**: The web framework used to build the backend API.
- **Streamlit**: The framework used to build the interactive frontend UI.
- **scikit-learn**: Used for building the recommendation model.
- **Pandas**: Used for data manipulation and analysis.

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/meal-plan-recommendation-app.git
    cd meal-plan-recommendation-app
    ```

2. **Create a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare the dataset**

    Ensure you have your dataset file (`dataset.csv`) in the `Data/` directory. The CSV file should contain the necessary recipe information.

## Running the Application Locally

### Start the Backend (FastAPI)

1. **Navigate to the project directory**

    ```bash
    cd meal-plan-recommendation-app
    ```

2. **Run the FastAPI server**

    ```bash
    uvicorn main:app --reload
    ```

    The backend API will be running at `http://127.0.0.1:8000`.

### Start the Frontend (Streamlit)

1. **Open a new terminal and navigate to the project directory**

    ```bash
    cd meal-plan-recommendation-app
    ```

2. **Run the Streamlit app**

    ```bash
    streamlit run meal_recommender.py
    ```

    The frontend UI will be running at `http://localhost:8501`.

## Usage

1. Open the frontend UI in your web browser at `http://localhost:8501`.
2. Use the sliders to input your desired nutritional values.
3. Specify ingredients to include or exclude in the recommendations.
4. Click the "Generate" button to receive meal recommendations.
5. View detailed recipe information and nutritional values for each recommendation.

## Deployment

The application is deployed on Streamlit Cloud. You can access it via the following link:

[Meal Plan Recommendation App](https://meal-recommender.streamlit.app/)

## Project Structure

- `main.py`: Contains the FastAPI backend code.
- `generator.py`: Defines the `Generator` class for making API requests to the backend.
- `meal_recommender.py`: Contains the Streamlit frontend code.
- `model.py`: Defines the functions for data processing and recommendation model.
- `requirements.txt`: Lists the required Python packages.
- `Data/`: Directory containing the dataset file (`dataset.csv`).

## License

This project is licensed under the MIT License.
