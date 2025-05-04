# UIC Computer Science Course Scraper

This project scrapes the official University of Illinois Chicago (UIC) Computer Science course catalog and extracts details such as course numbers, names, and descriptions.

##  Features

- Extracts all undergraduate CS course blocks from the UIC catalog
- Parses course number, name, and full description
- Stores the data in a structured CSV file: `Undergrad_courses.csv`

##  Technologies Used

- Python
- BeautifulSoup (for HTML parsing)
- Requests (for HTTP GET)
- CSV (for data storage)

##  Output Format

The output CSV contains:
- `Course_Number`: e.g., `CS 491`
- `Course_Name`: e.g., `Seminar`
- `Course_Description`: Full description with prerequisites and details

##  How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/uic-cs-course-scraper.git
   cd uic-cs-course-scraper
2. python scraper.py
