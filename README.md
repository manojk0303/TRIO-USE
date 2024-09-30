# TRIO-USE App

## Overview
This is a simple command-line tool built to provide the latest BBC news, crazy jokes, and current weather reports for any city. It includes user-friendly commands to fetch and display the desired information instantly.

## Features
- Fetch trending BBC News headlines.
- Get random dad jokes to lighten your mood.
- Display current weather information for any city.
- Simple command-line interface with easy commands.

## Requirements
- Python 3.x
- `requests` module (You can install it using `pip install requests`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/manojk0303/TRIO-USE.git
    ```

2. Navigate to the project directory:
    ```bash
    cd TRIO-USE
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Once installed, you can run the tool using the following commands:

1. Run the script:
    ```bash
    python main_module.py
    ```

2. Available commands:
    ```
    feednews        - Feeds You The Trending news from BBC.
    feedjokes       - Feeds You Crazy Jokes You Ever Heard Before.
    feedweather     - Feeds You The Current Weather Report.
    help            - Provides You Brief Description Of This Cool Tool.
    exit            - Quits the tool.
    ```

## Example
Here's how you can interact with the tool:

1. To get the latest BBC news:
    ```bash
    > feednews
    ```

2. To get a random joke:
    ```bash
    > feedjokes
    ```

3. To get the current weather report for a city:
    ```bash
    > feedweather
    ```

4. To quit the application:
    ```bash
    > exit
    ```

## Notes
- The application uses the **NewsAPI** and **OpenWeatherMap** API, so ensure you have a valid API key to use these services.
- You can replace the API keys in the script as per your account.

## License
This project is open-source and available under the MIT License.

