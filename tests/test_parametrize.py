"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, be


@pytest.mark.parametrize('setting_browser_desktop_or_mobile', [(2048, 1080), (1920, 1080), (1280, 720)],
                         ids=['QXGA', 'Full HD', 'WXGA'], indirect=True)
def test_github_desktop(setting_browser_desktop_or_mobile):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


@pytest.mark.parametrize('setting_browser_desktop_or_mobile', [(393, 816), (360, 720), (412, 915)],
                         ids=['Xiaomi Mi 8 SE', 'Huawei Mate 10 Lite', 'Samsung A32'], indirect=True)
def test_github_mobile(setting_browser_desktop_or_mobile):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
