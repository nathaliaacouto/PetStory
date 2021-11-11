import time
from selenium.webdriver.common.by import By

def test_novo_atendimento_interface(browser, app):
    browser.get('http://localhost:5000/novo-atendimento')
    assert browser.title == 'PetStory | Novo Atendimento'
    browser.find_element(By.ID, "search_box").send_keys('98765432')
    browser.find_element(By.ID, "search").click()
    time.sleep(1)
    browser.find_element(By.ID, "user_data-0-nome")
    browser.find_element(By.ID, "user_data-0-phone")