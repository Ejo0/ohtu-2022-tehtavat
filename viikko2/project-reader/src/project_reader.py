from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):

        content = request.urlopen(self._url).read().decode("utf-8")
        try:
            poetry_info = toml.loads(content)["tool"]["poetry"]
            name = poetry_info["name"]
            description = poetry_info["description"]
            dependencies = poetry_info["dependencies"]
            dev_dependencies = poetry_info["dev-dependencies"]
        except:
            return Project("Not found", "-", [], [])

        return Project(name, description, dependencies, dev_dependencies)
