from bs4 import BeautifulSoup
import requests
import csv

source=requests.get('https://catalog.uic.edu/ucat/course-descriptions/cs/').text

soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())
with open('Undergraduate_courses.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Course_Number', 'Course_Name', 'Course_Description'])

    for course_block in soup.find_all('div', class_='courseblock'):
        if not course_block.p or not course_block.p.strong:
            continue

        course = course_block.p.strong.text.strip()
        Course_Contents = course.split('.')

        if len(Course_Contents) < 2:
            continue

        Course_ID = Course_Contents[0].strip()
        Course_Name = Course_Contents[1].strip()

        description = course_block.find('p', class_='courseblockdesc')
        course_des = description.text.strip() if description else "No description available"

        print(Course_ID)
        print(Course_Name)
        print(course_des)
        print()

        csv_writer.writerow([Course_ID, Course_Name, course_des])
