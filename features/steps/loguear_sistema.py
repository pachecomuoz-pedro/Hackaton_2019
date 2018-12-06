# -*- coding: UTF-8 -*-
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given(u'que ingreso credenciales no validas "{user}" y "{password}"')
def step_impl(context, user, password):
    context.browser.get(context.get_url('/'))
    context.browser.find_element_by_name('username').send_keys(user)
    context.browser.find_element_by_name('password').send_keys(password)


@then(u'se me notifica en pantalla "{error}"')
def step_impl(context, error):
    resultado = context.browser.find_element_by_xpath('/html/body/div/div/div[1]/section/div')
    assert error == resultado.text, "El titulo esperado " + error + " no es igual al resultado " + resultado.text


@given(u'que ingreso credenciales validas "{user}" y "{password}"')
def step_impl(context, user, password):
    context.browser.get(context.get_url('/'))
    context.browser.find_element_by_name('username').send_keys(user)
    context.browser.find_element_by_name('password').send_keys(password)


@when(u'selecciono la opción iniciar sesión')
def step_impl(context):
    context.browser.find_element_by_xpath('/html/body/div/div/div[1]/section/form/div[3]/button').click()


@then(u'se mostrara la pagina principal del evento "{titulo}"')
def step_impl(context, titulo):
    titulo_res = context.browser.title
    assert titulo == titulo_res, "El titulo esperado " + titulo + " no es igual al resultado " + titulo_res
