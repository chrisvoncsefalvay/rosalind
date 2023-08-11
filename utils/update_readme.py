# README.md autoupdater

import os
import re
import requests
from bs4 import BeautifulSoup


def scrape_table():
    url = "https://rosalind.info/problems/list-view/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        problem_list = soup.find('table', class_="problem-list")

        # Extract ID from problem url, title from the row
        problems = {}
        for row in problem_list.find('tbody').find_all('tr'):
            cols = row.find_all('td')
            problem_id = cols[0].text.strip()
            problem_title = cols[1].text.strip()
            problems[problem_id] = problem_title
        return problems
    else:
        print("Failed to retrieve the webpage.")
        return None

def filter_for_implemented_problems(problems_dict: dict) -> dict:
    """Filter the problems dictionary for problems that have been implemented."""
    implemented_problems = []
    for filename in os.listdir("../"):
        if filename.endswith(".py"):
            implemented_problems.append(filename.split(".")[0])
    return {k: v for k, v in problems_dict.items() if k in implemented_problems}


def render_markdown_table(problems_dict: dict) -> str:
    """Render a markdown table from the problems dictionary."""
    markdown_table = "| ID | Title | Script | Rosalind.info link |\n| --- | --- | --- | --- |\n"
    for key, value in problems_dict.items():
        github_link = f"[script](https://github.com/chrisvoncsefalvay/rosalind/blob/main/{key}.py)"
        rosalind_link = f"[Rosalind.info](https://rosalind.info/problems/{key.lower()}/)"
        markdown_table += f"| {key} | {value} | {github_link} | {rosalind_link} |\n"

    return markdown_table


def update_readme(new_toc: str) -> None:
    """Update the README.md file with the new table of contents."""
    with open("../README.md", "r") as f:
        readme = f.read()

    # Replace the old table of contents with the new one
    old_toc = re.search(r"<!-- toc -->.*<!-- tocstop -->", readme, re.DOTALL)
    readme = readme.replace(old_toc.group(0), new_toc)

    # Write the updated README.md file
    with open("../README.md", "w") as f:
        f.write(readme)

if __name__ == "__main__":
    problems = scrape_table()
    problems = filter_for_implemented_problems(problems)
    markdown_table = render_markdown_table(problems)
    update_readme(markdown_table)