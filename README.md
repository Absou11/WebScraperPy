# Web Scraping with Python

This is a simple Python script that allows you to scrape and download certain file types (e.g., PDFs, JPGs, PNGs) and extract links, images, stylesheets, and script sources from a specified website. You can enter the URL of a website, and the script will perform the following tasks:

- Extract and print all the links (href) on the webpage.
- Download files of specified types (PDF, JPG, PNG) to your local directory.
- Extract and print URLs from 'a' tags, 'img' tags, 'link' tags, and 'script' tags on the webpage.

## Usage

1. Clone this repository or download the script.

2. Install the required Python packages if you haven't already. You can install them using pip:

   ```bash
   pip install requests beautifulsoup4

