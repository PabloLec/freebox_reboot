import time, os
from selenium import webdriver 

##### RENTREZ VOTRE MOT DE PASSE FREEBOX OS #####
MOT_DE_PASSE = "VOTRE_MOT_DE_PASSE_FREEBOX_OS"
# # # # # # # # # # # # # # # # # # # # # # # # #


def click_on_element(element):
	'''Clic sur un élément du DOM avec offset'''
	selenium_action = webdriver.common.action_chains.ActionChains(selenium_chrome)
	selenium_action.move_to_element_with_offset(element, 15, 15)
	selenium_action.click()
	selenium_action.perform()

# URL pour login sur Freebox OS
target_url = 'https://mafreebox.freebox.fr/login.php'

# Démarrage de Selenium
selenium_options = webdriver.ChromeOptions()
selenium_options.add_argument("-headless")
selenium_options.add_argument("-disable-gpu")
selenium_options.add_argument("--disable-extensions")

selenium_chrome = webdriver.Chrome(options=selenium_options)

selenium_chrome.get(target_url)
time.sleep(5)

# Saisie du mot de passe
mdp = selenium_chrome.find_element_by_xpath("//input[@class='password']")
mdp.send_keys(MOT_DE_PASSE)

# Clic sur le bouton de connexion
bouton_connexion = selenium_chrome.find_element_by_xpath("//input[@class='submit-btn']")
click_on_element(bouton_connexion)

time.sleep(5)

# Clic sur le bouton de menu Frebbox OS
bouton_free = selenium_chrome.find_element_by_xpath("//span[@style='line-height: 39px;']")
click_on_element(bouton_free)

time.sleep(1)

# Clic sur le bouton de redémarrage
bouton_reboot = selenium_chrome.find_element_by_xpath("//div[@class='x-menu-item-icon btn-32-reboot ']")
click_on_element(bouton_reboot)

time.sleep(1)

bouton_oui = selenium_chrome.find_element_by_xpath("//a[@style='right: auto; left: 88.5px; top: 0px; margin: 0px; width: 75px;']")
click_on_element(bouton_oui)

# Fermeture de Selenium
selenium_chrome.quit()


# Fin du script
print("Script terminé - Freebox en cours de redémarrage")
