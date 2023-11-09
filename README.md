# Dash App with SQL Server Integration

## Overview

This repository contains a Dash web application that plots graphs using data stored in a SQL Server database. By following the steps below, you can easily set up and run the app.

## Prerequisites

Before running the app, make sure you have the following:

1. Python installed on your machine.
2. SQL Server installed and running.
3. Database credentials for your SQL Server.

## Setup

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Create a `.env` file in the root directory of the project and add your SQL Server database credentials in the following format:

```
server = server_name
database = database name
username = user name
password = password
```

3. Open the `callbacks.py` file and update the database table name and column names according to your database schema.



## Running the App

1. Open a terminal and navigate to the project directory.

```bash
cd your-repository
```

2. Run the `main.py` file.

```bash
python main.py
```

3. The app will provide you with a URL. Open the URL in your web browser to access the Dash application.

## Usage

Once the app is running, you can interact with the web interface to visualize data from your SQL Server database. Explore the different features and customize the app according to your needs.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and contributions are highly appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
