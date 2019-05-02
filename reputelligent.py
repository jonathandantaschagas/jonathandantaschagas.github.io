from selenium import webdriver
import selenium.webdriver.common.keys as Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
name = 'pimpmypetoficial'
pwd = 'mealpimp18'

 # Selecionando o driver
driver = webdriver.Chrome('C:/Users/jochagas/Documents/Selenium/Driver/Chrome/chromedriver.exe')

# Tempo de espera
time =  10
wait = WebDriverWait(driver, time)

# url = 'http://www.google.com'
driver.get(url)
# presence_of_element_located - Utilizado para seguir apenas quando o elemento for localizado
# driver.implicitly_wait(10) # 10 segundos

# Aguardando o formulário carregar
form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))

user = driver.find_elements_by_css_selector('form input')[0]
password = driver.find_elements_by_css_selector('form input')[1]

user.send_keys(name)
password.send_keys(pwd)

driver.find_element_by_xpath("//button[@type='submit']").click()
print('Entrou no sistema')

print('Buscando usuarios')
form = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))
barra_pesquisa = driver.find_elements_by_css_selector('input')[1]
barra_pesquisa.send_keys('Users')
print('Busca finalizada')


# botao_pesquisa = driver.find_element_by_name('search_button')
# botao_pesquisa.click()


# while True:
# 	arr_obj = wait.until(EC.element_to_be_clickable(By.XPATH, '//img[name="access"]'))

# 	get_itens(arr_obj)
# 	scroll_page()



# def get_itens(img_object):
# 	for img in arr_obj:
# 	img.click()

# 	perfil  =  wait.until(EC.element_to_be_clickable((By.ID, 'search_bar')))
# 	login = driver.find_element_by_name('login')

# 	if profile_f.text == 'Active':
# 		un_list(login)
# 		perfil.click()
# 		driver.execute_script("window.history.go(-1)")

# 	else:
# 		driver.execute_script("window.history.go(-1)")


# def scroll_page():

# 	SCROLL_PAUSE_TIME = 0.5

# 	current_height = driver.execute_script('return document.body.scrollHeight;')

# 	while True:
# 		driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# 		new_height = driver.execute_script('return document.body.scrollHeight;')

# 		if(current_height == new_height):
# 			break

# 		current_height = new_height

# def un_list(login, name):
# 	f = open('list_system.txt','w')
# 	f.write('Login: {}, Name: {}'.format(login,name))
# 	f.close()
