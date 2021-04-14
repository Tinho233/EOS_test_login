import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser_ver", action="store", default="")
    parser.addoption("--headless", action="store", default=False)
    parser.addoption("--remote", action="store", default=False)
    parser.addoption("--hub", action="store", default="localhost")


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browser_ver")
    hub = request.config.getoption("--hub")
    headless = False
    remote = False
    if request.config.getoption("--headless"):
        headless = True
    if request.config.getoption("--remote"):
        remote = True

    return {"remote": remote,
            "version": version,
            "browser": browser,
            "headless": headless,
            "hub": hub}


def get_chrome_options(config):
    options = ChromeOptions()
    options.headless = config["headless"]
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    return options


def get_firefox_options(config):
    options = FirefoxOptions()
    options.headless = config["headless"]
    return options


def create_remote_driver(config):
    if config["browser"] == "chrome":
        options = get_chrome_options(config)
    else:
        options = get_firefox_options(config)
    capabilities = {"version": config["version"],
                    "acceptInsecureCerts": True,
                    "screenResolution": "1920x1080x16"}
    return webdriver.Remote(command_executor="http://192.168.0.11:4444/wd/hub",
                            options=options,
                            desired_capabilities=capabilities)


def create_local_driver(config):
    driver = None
    if config["browser"] == "chrome":
        driver_manager = ChromeDriverManager()
        options = get_chrome_options(config)
        driver = webdriver.Chrome(executable_path=driver_manager.install(), options=options)
    elif config["browser"] == "firefox":
        driver_manager = GeckoDriverManager()
        options = get_firefox_options(config)
        driver = webdriver.Firefox(executable_path=driver_manager.install(), options=options)
    return driver


@pytest.fixture()
def driver(request, config):
    driver = None
    if config["remote"]:
        driver = create_remote_driver(config)
    else:
        driver = create_local_driver(config)
        driver.maximize_window()
        driver.implicitly_wait(10)

    def tear_down():
        driver.quit()

    request.addfinalizer(tear_down)
    yield driver