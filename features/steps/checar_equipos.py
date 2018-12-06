from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

@given(u'que ingreso a la sección de participantes')
def step_impl(context):
    time.sleep(5)
    context.browser.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[3]').click()


@when(u'selecciono la opción mostrar equipos')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[3]/ul/li[2]/a').click()


@then(u'se despliega en pantalla todos los equipos participantes en ese evento')
def step_impl(context):
    pass
