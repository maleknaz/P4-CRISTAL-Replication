import json
import os
from pathlib import Path


def link_stats():
    # links = pmap(link_issues_to_reviews, list(apps.keys()))
    links = [json.loads(Path(f'process/cir-links/{a}').read_text()) for a in os.listdir(f'process/cir-links')]
    all_links = {}
    for d in links:
        all_links.update(d)

    total = len(all_links)

    def percent(lst: list, msg: str):
        print(f'{len(lst)} ({len(lst) / total * 100:.1f}%) {msg}')

    print(f'There are a total of {total} reviews.')
    has_issues = [(r, d) for r, d in all_links.items() if d['issues']]
    percent(has_issues, 'reviews linked with at least one issue')
    has_commits = [(r, d) for r, d in all_links.items() if d['commits']]
    percent(has_commits, 'reviews linked with at least one commit')
    has_commits = [(r, d) for r, d in all_links.items() if d['commits'] and d['issues']]
    percent(has_commits, 'reviews linked with at least one issue and one commit')
    print(f'Average number of issues linked (ignoring zeros): {sum(len(d["issues"]) for r, d in has_issues) / len(has_issues):.1f}')
    print(f'Average number of commits linked (ignoring zeros): {sum(len(d["commits"]) for r, d in has_commits) / len(has_commits):.1f}')


if __name__ == '__main__':
    link_stats()
