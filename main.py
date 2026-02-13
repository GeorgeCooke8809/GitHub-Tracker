from github import Github, Auth
import json

class App():
    def __init__(self, debugging: bool = False):
        self.debugging = debugging

        with open("tokens.json", "r") as file:
            access_token = json.load(file)["token"]

        self.__debugging_statement(f"{access_token = }")

        auth = Auth.Token(access_token)

        self.git_con = Github(auth=auth)

        repos = self.__get_repos()

        file_paths = []

        for repo in repos:
            repo_files = self.__get_repo_files(repo)

            file_paths.extend(repo_files)

            self.__debugging_statement(f"\033[92m{file_paths = }\033[0m")

        files = []

        for file_path in file_paths:
            file_type = file_path.type
            file_lines = 0

            files.extend([file_type, file_lines])

    def __get_repos(self):
        user = self.git_con.get_user()
        repos = user.get_repos(visibility="all")

        self.__debugging_statement(f"{repos.totalCount} Repos Found")
        self.__debugging_statement()

        repo_names = [repo.name for repo in repos]

        for i in range(len(repo_names)):
            self.__debugging_statement(f"{i+1} - {repos[i]}")

        return repos
    
    def __get_repo_files(self, repo):
        repo_files = []
        contents: list = repo.get_contents("")

        while len(contents) > 0:
            element = contents.pop(0)

            self.__debugging_statement(f"{element = }")

            if element.type == "dir": # Is folder
                contents.extend(repo.get_contents(element.path))
                self.__debugging_statement("\033[95mElement is directory\033[0m")
            else:
                try: # for if it is a single file in directory or list
                    repo_files.extend(element)
                except:
                    repo_files.extend([element])

                self.__debugging_statement(f"{repo_files = }")

            self.__debugging_statement()

        return repo_files
    
    def __debugging_statement(self, message = ""):
        if self.debugging:
            print(f"\033[94mDEBUGGING - {message}\033[0m")

if __name__ == "__main__":
    app = App(debugging = True)