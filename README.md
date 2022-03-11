# reading-buses

Basic script to get data for a bus stop using the [Reading Buses API](https://reading-opendata.r2p.com/).

# To install 

Requires: 
- Python3 
- pipenv 

Clone the repository and cd into the folder:

    git clone https://github.com/crablab/reading-buses & cd reading-buses

Install dependencies:

    pipenv install 

Export the environment variable for the API key:

    export READING_BUSES_KEY=xxx

Run the script:

    pipenv run python3 main.py

You can modify the helper script to use a different stop, or use the `reading_buses.stop` library elsewhere. 

# Contributions 

Contributions welcome if you want to add functionality or improve something you find useful 😃