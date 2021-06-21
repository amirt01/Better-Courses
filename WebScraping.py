import requests
from bs4 import BeautifulSoup
from time import time


def progress_bar(iterable, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    """
    Credit to @Greenstick on StackOverflow for the the general setup.
    Changes: Added iteration timer
    """
    total = len(iterable)
    start_time = time()

    # Progress Bar Printing Function
    def printProgressBar(iteration):
        delta_time = (time() - start_time) / (iteration + 1)
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}, {delta_time:.2f} it/s, {iteration = }', end=print_end)

    # Initial Call
    printProgressBar(0)

    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()



all_courses_url = 'http://catalogue.uci.edu/allcourses/'

all_courses_page = requests.get(all_courses_url)
all_courses_soup = BeautifulSoup(all_courses_page.content, 'html.parser')

section_soups = []
a_to_z_index = all_courses_soup.find('div', id='atozindex')

for section in progress_bar(a_to_z_index.find_all('a', href=True)):
    section_url = all_courses_url + section['href'].split('/')[2]
    section_page = requests.get(section_url)
    section_soups.append(BeautifulSoup(section_page.content, 'html.parser'))

course_blocks = []
for section_soup in progress_bar(section_soups):
    courses = section_soup.find_all('div', class_='courseblock')
    for course in courses:
        course_blocks.append((course.find('p', class_='courseblocktitle'), course.find('div', class_='courseblockdesc')))

for course_block_title, course_block_desc in progress_bar(course_blocks):
    course_block_title_text = course_block_title.text.split(sep='.')
    section_code = course_block_title_text[0].split(sep='\xa0')
    section = ' '.join(section_code[:-1])
    code = section_code[-1]
    title = course_block_title_text[1].strip()
    try:
        units = course_block_title_text[2].split()[0]
    except IndexError:
        units = 0

    course_block_desc_children = course_block_desc.findChildren()
    description = course_block_desc_children[0].text

    prerequisites = []
    corequisites = []

    for block in course_block_desc_children:
        text = block.text
        if 'Prerequisite:' in text:  # Prerequisite
            if 'Corequisite:' in text:  # Prerequisite and Corequisite
                text = text.split(sep='\n')
                corequisites = text[0].partition(' ')[2].strip().replace('\xa0', ' ').split(sep='.')[0].split(
                    sep=' and ')
                prerequisites = text[1].partition(' ')[2].strip().replace('\xa0', ' ').split(sep='.')[0].split(
                    sep=' and ')
            else:  # just Prerequisite
                prerequisites = text.partition(' ')[2].strip().replace('\xa0', ' ').split(sep='.')[0].split(sep=' and ')
        elif 'Corequisite:' in text:  # just Corequisite
            corequisites = text.partition(' ')[2].strip().replace('\xa0', ' ').split(sep='.')[0].split(sep=' and ')

    def attempt_split(li):  # for splitting up prerequisite / corequisite strings
        if len(li) < 2:
            return li
        ret = []
        for el in li:
            if el[0] == '(' and el[-1] == ')':
                ret.append(el[1:-1].split(' or '))
            else:
                ret.append(el)
        return ret
