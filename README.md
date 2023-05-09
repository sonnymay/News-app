# News-app

A simple news aggregator app built with Python and Tkinter. This app allows you to search for news articles using a keyword and displays the articles with clickable links that open in your default web browser.

![News App Screenshot](screenshot.png)

## Features

- Search for news articles using a keyword
- Display article title, source, publication date, and URL
- Clickable URLs that open in your default web browser

## Installation

To run the News App, you'll need Python 3.x and the following libraries installed:

- `requests`
- `python-dotenv`

You can install these libraries using `pip`:

```bash
pip install requests python-dotenv
```

## Setup

1. Clone this repository:

```bash
git clone https://github.com/sonnymay/News-app.git
```

2. Navigate to the project directory:

```bash
cd News-app
```

3. Obtain a News API key from [NewsAPI.org](https://newsapi.org/).

4. Create a `.env` file in the project directory and add your News API key:

```
NEWS_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual News API key.

## Usage

1. Run the `news_aggregator.py` script:

```bash
python news_aggregator.py
```

2. Enter a keyword in the search box and click the "Search" button to fetch news articles.

3. Click on a URL to open the article in your default web browser.

## Contributing

If you'd like to contribute to this project, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
