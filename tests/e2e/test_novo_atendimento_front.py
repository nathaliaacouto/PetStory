import time
from selenium.webdriver.common.by import By

def test_novo_atendimento_interface(browser, app):
    browser.get('http://localhost:5000/novo-atendimento')
    assert browser.title == 'PetStory | Novo Atendimento'
    browser.find_element(By.ID, "search_box").send_keys(12345678)
    browser.find_element(By.ID, "search").click()
    time.sleep(1)
    assert browser.find_element(By.ID, "user_data-0-nome").get_attribute("value") == 'Marcos da Silva'
    assert browser.find_element(By.ID, "user_data-0-telefone").get_attribute("value") == '12345678'
