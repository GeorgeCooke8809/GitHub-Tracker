from github import Github, Auth
import logging
from dotenv import load_dotenv
import os
from rich.progress import track
import time

class GitHubData:
    def __init__(self, ansi: bool = True):
        self.ansi = ansi

        self.file_types = None

        load_dotenv()
        self.access_token = os.getenv("GITHUB_TOKEN")

        if self.access_token == None or self.access_token == "" or self.access_token == "YOUR_GITHUB_TOKEN":
            raise ValueError("No GitHub token found.")
        
        auth = Auth.Token(self.access_token)

        self.git_con = Github(auth=auth)

    def display_top_languages_line_count(self, entries: int = 5):
        if self.file_types == None:
            logging.error("self.file_types not declared")
            raise ValueError("self.file_types does not exist yet, call update_data() before displaying")

        total_lines = 0

        logging.debug(f"{self.file_types = }")

        for language in self.file_types:
            total_lines += self.file_types[language][0]

        logging.debug(f"{total_lines = }")

        sorted_languages = sorted(self.file_types, key=lambda x: self.file_types[x][0], reverse=True)

        if entries > len(sorted_languages):
            entries = len(sorted_languages)

        logging.debug(f"{sorted_languages = }")
        
        if self.ansi:
            print("\033[1mTop Languages (By Line Count):\033[0m")

            for i in range(entries):
                print(f"{f"\033[1mLanguage {i+1}":<{(15+len(str(entries)))}}-\033[0m {sorted_languages[i]:^8} - {f"{self.file_types[sorted_languages[i]][0]:,} lines":^25}-{f"{self.file_types[sorted_languages[i]][0] / total_lines * 100 :.2f}%":>7}")
        else:
            print("Top Languages (By Line Count):")

            for i in range(entries):
                print(f"{f"Language {i+1}":<{(15+len(str(entries)))}}- {sorted_languages[i]:^8} - {f"{self.file_types[sorted_languages[i]][0]:,} lines":^25}-{f"{self.file_types[sorted_languages[i]][0] / total_lines * 100 :.2f}%":>7}")

    def display_top_languages_character_count(self, entries: int = 5):
        if self.file_types == None:
            logging.error("self.file_types not declared")
            raise ValueError("self.file_types does not exist yet, call update_data() before displaying")
        
        total_characters = 0

        logging.debug(f"{self.file_types = }")

        for language in self.file_types:
            total_characters += self.file_types[language][1]

        logging.debug(f"{total_characters = }")

        sorted_languages = sorted(self.file_types, key=lambda x: self.file_types[x][1], reverse=True)

        if entries > len(sorted_languages):
            entries = len(sorted_languages)

        logging.debug(f"{sorted_languages = }")

        if self.ansi:
            print("\033[1mTop Languages (By Character Count):\033[0m")

            for i in range(entries):
                print(f"{f"\033[1mLanguage {i+1}":<{(15+len(str(entries)))}}-\033[0m {sorted_languages[i]:^8} - {f"{self.file_types[sorted_languages[i]][1]:,} characters":^25}-{f"{self.file_types[sorted_languages[i]][1] / total_characters * 100 :.2f}%":>7}")
        else:
            print("Top Languages (By Character Count):")

            for i in range(entries):
                print(f"{f"Language {i+1}":<{(15+len(str(entries)))}}- {sorted_languages[i]:^8} - {f"{self.file_types[sorted_languages[i]][1]:,} characters":^25}-{f"{self.file_types[sorted_languages[i]][1] / total_characters * 100 :.2f}%":>7}")

    def update_data(self):
        repos = self._get_repos()

        files = self._get_repo_files(repos)

        logging.debug(f"{files = }")

        self.file_types = {}

        for file in files:
            if files[file][0] in self.file_types:
                self.file_types[files[file][0]][0] += files[file][1][0]
                self.file_types[files[file][0]][1] += files[file][1][1]
            else:
                self.file_types[files[file][0]] = [files[file][1][0], files[file][1][1]]

    def _get_repos(self):
        user = self.git_con.get_user()
        repos = user.get_repos(visibility="all")

        print(f"{repos.totalCount} Repos Found")

        return repos
    
    def _get_repo_files(self, repos):
        files = {}

        file_index = 0

        for i in track(range(repos.totalCount)):
            repo = repos[i]

            print(f"Working on repo no. {i+1} ({repo.name})...")

            repo_files = []
            contents: list = repo.get_contents("")

            while len(contents) > 0:
                element = contents.pop(0)

                logging.debug(f"{element = }")

                if element.type == "dir": # Is folder
                    contents.extend(repo.get_contents(element.path))
                    logging.debug("Element is directory")
                else:
                    try: # for if it is a single file in directory or list
                        repo_files.extend(element)
                    except TypeError: #  Triggered when trying to extend list by single class
                        repo_files.extend([element])

            logging.debug(f"{repo_files = }")

            for file in repo_files:
                file_title = file.name
                
                file_title_split = file_title.split(".")
                file_type = f".{file_title_split[-1]}"

                logging.debug(f"{file_title = }")
                logging.debug(f"{file_type = }")

                try:
                    file_content = file.decoded_content.decode("utf-8")
                except (AssertionError, UnicodeDecodeError): # for unsupported file types
                    logging.debug(f"Could not decode {file} - treated as empty")
                    file_content = "" # Means that any file that cannot natively be decoded is stored as empty

                line_count = len(file_content.splitlines())
                character_count = len(file_content)

                logging.debug(f"{line_count = }")
                logging.debug(f"{character_count = }")

                files[f"{file_index} - {file_title}"] = [file_type, [line_count, character_count]]

                file_index += 1

        return files

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")

    connection = GitHubData()

    connection.update_data()

    connection.display_top_languages_line_count(10)

    print()

    connection.display_top_languages_character_count(10)