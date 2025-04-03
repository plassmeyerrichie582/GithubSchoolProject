class SimpleGithubSchoolProject:
    def __init__(self):
        self.projects = {}

    def add_project(self, name, description):
        self.projects[name] = {'description': description}

    def get_projects(self):
        return self.projects

if __name__ == "__main__":
    simple_git_proj = SimpleGithubSchoolProject()
    simple_git_proj.add_project("Python for Everyone", "Learn Python for everyone")
    print(simple_git_proj.get_projects())
