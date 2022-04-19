from libs.pages.repositories_page import RepositoriesPage
from libs.api.git_api import GitApi
import pytest

@pytest.mark.usefixtures('setup_teardown')
class TestRepos:

    def test_repos(self, webDriver, log):

        log.info("Capture repo's name and description from UI")
        repositoriesPage = RepositoriesPage(webDriver)
        ui_repos = repositoriesPage.get_repo()

        log.info("Get the repo's name and descirption from api")
        json_response = GitApi.get_repositories('django')

        log.info('Convert api response to dictionary')
        api_repos = TestRepos.convert_json_to_dictionary(self, json_response)

        log.info('Compare api response with ui response')
        TestRepos.compare_repos_dictionary(self, api_repos, ui_repos)

    def convert_json_to_dictionary(self, json_object):
        api_repos = {}
        for repo in json_object:
            api_repos[repo['name']] = repo['description']
        return api_repos

    def compare_repos_dictionary(self, api_repos, ui_repos):
        for key in api_repos.keys():
            try:
                assert api_repos[key] == ui_repos[key]
            except Exception:
                assert False, Exception