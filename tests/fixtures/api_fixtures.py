import os
import pytest
from libs.logger import Logger
from datetime import datetime
from libs.webdriver import WebDriver
from libs.test_context import TestContext


@pytest.fixture(scope='function')
def setup_teardown(request):
    log_file = '{}_{}.txt'.format('log', datetime.now().strftime("%d%m%Y%H%M%S"))
    Logger.init()
    log_dir = "logs/"
    Logger._log_dir = os.getcwd()
    Logger.add_log_handler(log_file, log_dir=log_dir)
    yield
    Logger.remove_log_handler()

@pytest.fixture(scope='function')
def webDriver():
    test_env = TestContext.test_env
    webDriver = WebDriver(TestContext.config['service']['hostName'], TestContext.headless_webdriver)
    return webDriver

@pytest.fixture(scope='session')
def log():
    return Logger()