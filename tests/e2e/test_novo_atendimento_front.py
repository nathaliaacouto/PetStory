import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_novo_atendimento_interface(browser, app):
    browser.get('http://localhost:5000/novo-atendimento')
    assert browser.title == 'PetStory | Novo Atendimento'
    browser.find_element(By.ID, "search_box").send_keys(12345678)
    browser.find_element(By.ID, "search").click()
    assert browser.find_element(By.ID, "user_data-0-nome").get_attribute("value") == 'Marcos da Silva'
    assert browser.find_element(By.ID, "user_data-0-telefone").get_attribute("value") == '12345678'
    select_element = browser.find_element(By.ID, "pet_data-0-dog")
    select_object = Select(select_element)
    select_object.select_by_visible_text("Toto")
    assert select_element.get_attribute("value") == "1"
    servico1 = browser.find_element(By.ID, "servicos_data-0-servico")
    servico2 = browser.find_element(By.ID, "servicos_data-1-servico")
    s1_select = Select(servico1)
    s2_select = Select(servico2)
    s1_select.select_by_visible_text("Banho Pug")
    s2_select.select_by_visible_text("Hidratação")
    time.sleep(1)
    browser.find_element(By.ID, "obs_text_area").send_keys("cadela idosa, cuidado ao manejar.")
    browser.find_element(By.ID, "submit").click()
    