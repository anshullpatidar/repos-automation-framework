import requests
import json

class GitApi:
    url = "https://api.github.com/"

    def get_repositories(repository_name):
        headers = {
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'accept-encoding': "gzip, deflate",
            'content-length': "42",
            'Connection': "keep-alive",
            'cache-control': "no-cache",
            'User-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36",
            'Content-Type': "application/json",
        }

        get_url = GitApi.url + 'orgs/{}/repos'.format(repository_name)
        response = requests.request("GET", get_url, headers=headers)
        return json.loads(response.text)

