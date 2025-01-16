import ssl
import urllib.request
from html.parser import HTMLParser

class MyHTMLTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.table_data = []
        self.current_row = []
        self.current_cell = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        elif tag == 'tr' and self.in_table:
            self.in_row = True
            self.current_row = []
        elif tag in ('td', 'th') and self.in_row:
            self.in_cell = True
            self.current_cell = ''

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        elif tag == 'tr' and self.in_row:
            self.in_row = False
            self.table_data.append(self.current_row)
        elif tag in ('td', 'th') and self.in_cell:
            self.in_cell = False
            self.current_row.append(self.current_cell.strip())

    def handle_data(self, data):
        if self.in_cell:
            self.current_cell += data

def extract_table_from_html(url):
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=context) as res:
        html = res.read().decode('utf-8')

    parser = MyHTMLTableParser()
    parser.feed(html)

    return parser.table_data

def print_grid_of_characters(table_data):
    data = table_data[1:]
    grid = {}
    for x, char, y in data:
        x, y = int(x), int(y)
        if (x, y) not in grid:
            grid[(x, y)] = char

    max_x = max(coordinate[0] for coordinate in grid.keys())
    max_y = max(coordinate[1] for coordinate in grid.keys())
    for y in range(max_y, -1, -1):
        row = ''.join(grid.get((x, y), ' ') for x in range(max_x + 1))
        print(row)

doc_URL = input("Enter Google Doc URL: ")
table_data = extract_table_from_html(doc_URL)
print_grid_of_characters(table_data)