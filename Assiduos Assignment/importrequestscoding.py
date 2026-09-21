import requests
from bs4 import BeautifulSoup


def fetch_points(url):

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    points = []
    for row in rows[1:]:
        cols = row.find_all("td")

        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())

        points.append((x, char, y))

    return points


def create_grid(points):

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, _, y in points)

    grid = [
        [' '] * (max_x + 1)
        for _ in range(max_y + 1)
    ]

    for x, char, y in points:
        grid[max_y - y][x] = char
        # If the output is upside down, change to:
        # grid[y][x] = char

    return grid


def print_grid(grid):

    for row in grid:
        print("".join(row))


def decode_secret_message(url):

    points = fetch_points(url)
    grid = create_grid(points)
    print_grid(grid)


if "_name_" == "_main_":
    url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    decode_secret_message(url)