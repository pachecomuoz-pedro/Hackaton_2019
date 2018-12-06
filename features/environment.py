from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:8000')
    context.browser.find_element_by_name('username').send_keys('pedrop')
    context.browser.find_element_by_name('password').send_keys('pedrop123')
    context.browser.find_element_by_xpath('/html/body/div/div/div[1]/section/form/div[3]/button').click()

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    pass
