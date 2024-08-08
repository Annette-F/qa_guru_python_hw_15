import pytest
from selene import browser


@pytest.fixture(scope='function', params=[(2048, 1080), (1920, 1080), (1280, 720)], ids=['QXGA', 'Full HD', 'WXGA'])
def setting_browser_desktop(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(393, 816), (360, 720), (412, 915)],
                ids=['Xiaomi Mi 8 SE', 'Huawei Mate 10 Lite', 'Samsung A32'])
def setting_browser_mobile(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(2048, 1080), (1920, 1080), (1280, 720), (393, 816), (360, 720), (412, 915)],
                ids=['QXGA', 'Full HD', 'WXGA', 'Xiaomi Mi 8 SE', 'Huawei Mate 10 Lite', 'Samsung A32'])
def setting_browser_desktop_or_mobile(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1020:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
