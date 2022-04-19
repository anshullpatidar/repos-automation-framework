import os
import yaml


class TestContext:
    # Can be set via TEST_ENV environemnt variable
    test_env = 'qa'
    # Current working directory
    root_dir = os.getcwd()

    # Log folder
    log_dir = None

    # Configuration folder
    config_dir = os.path.join(root_dir, 'config')

    # Configuation object reading from test .yaml configure file
    config = None

    # Web browser driver used in UI test
    web_browser = None
    headless_webdriver = False
    # Service protocol: REST vs gRPC
    protocol = 'REST'

    __initialized = False

    @classmethod
    def init(cls):
        '''
        Initialize test context
        '''
        if not cls.__initialized:
            if ('TEST_ENV' in os.environ):
                TestContext.test_env = os.environ.get('TEST_ENV')

            # Read configuration .yaml file
            if (None == TestContext.config):
                with open(os.path.join(cls.config_dir, '{}.yaml'.format(TestContext.test_env)), 'r') as f:
                    TestContext.config = yaml.load(f, Loader=yaml.FullLoader)

            # Web browser driver
            TestContext.web_browser = TestContext.config['uiTest']['browser']
            TestContext.headless_webdriver = TestContext.config['uiTest']['headless']

            host_name = TestContext.config['service']['hostName']

            # Log folder path
            TestContext.log_dir = os.path.join(cls.root_dir, 'log\{}\{}'
                                               .format(TestContext.test_env, host_name))

            if (False == os.path.exists(TestContext.log_dir)):
                os.makedirs(TestContext.log_dir)

            cls.__initialized = True