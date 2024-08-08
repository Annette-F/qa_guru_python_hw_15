"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be


def test_github_desktop(setting_browser_desktop_or_mobile):
    if setting_browser_desktop_or_mobile == 'mobile':
        pytest.skip(reason='The test for the desktop version of the application')
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


def test_github_mobile(setting_browser_desktop_or_mobile):
    if setting_browser_desktop_or_mobile == 'desktop':
        pytest.skip(reason='The test for the mobile version of the application')
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
