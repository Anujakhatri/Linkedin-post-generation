import json
import re
from typing import Any

import pandas as pd


SURROGATE_RE = re.compile(r"[\ud800-\udfff]")


class FewShotPosts:
    def __init__(self, file_path = "data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            posts = self._sanitize_surrogates(posts)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            # collect unique tags
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def _sanitize_surrogates(self, value: Any) -> Any:
        if isinstance(value, str):
            return SURROGATE_RE.sub('', value)
        if isinstance(value, list):
            return [self._sanitize_surrogates(item) for item in value]
        if isinstance(value, dict):
            return {key: self._sanitize_surrogates(item) for key, item in value.items()}
        return value

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  # Tags contain 'Influencer'
            (self.df['language'] == language) &  # Language is 'English'
            (self.df['length'] == length)  # Line count is less than 5
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Medium", "Neplish", "Job Search")
    print(posts)
