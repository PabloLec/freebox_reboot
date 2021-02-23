import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec

##### RENTREZ VOTRE MOT DE PASSE FREEBOX OS #####
MOT_DE_PASSE = "VOTRE_MOT_DE_PASSE_FREEBOX_OS"
# # # # # # # # # # # # # # # # # # # # # # # # #


def click_on_element(element):
	"""Clic sur un élément du DOM avec offset"""
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

# Saisie du mot de passe
mdp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//input[@class='password']")))
mdp.send_keys(MOT_DE_PASSE)

# Clic sur le bouton de connexion
bouton_connexion = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//input[@class='submit-btn']")))
click_on_element(bouton_connexion)

# Clic sur le bouton de menu Freebox OS
bouton_free = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//span[@id='ext-comp-1017-btnIconEl']")))
click_on_element(bouton_free)

# Clic sur le bouton de redémarrage
bouton_reboot = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='menuitem-1038']")))
click_on_element(bouton_reboot)


# Confirmation du redémarrage
bouton_oui = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[@id='button-1006']")))
click_on_element(bouton_oui)

# Fermeture de Selenium
selenium_chrome.quit()


# Fin du script
print("Script terminé - Freebox en cours de redémarrage")
