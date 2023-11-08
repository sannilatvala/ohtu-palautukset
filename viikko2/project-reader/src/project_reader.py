from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_data = toml.loads(content)

        tool_data = toml_data.get("tool", {})
        poetry_data = tool_data.get("poetry", {})

        name = poetry_data.get("name", [])
        description = poetry_data.get("description", [])
        license = poetry_data.get("license", [])
        authors = poetry_data.get("authors", [])
        dependencies = poetry_data.get("dependencies", {}) 

        group_data = poetry_data.get("group", {})
        dev_data = group_data.get("dev", {})
        dev_dependencies = dev_data.get("dependencies", {})

        return Project(name, description, license, authors, dependencies, dev_dependencies)
