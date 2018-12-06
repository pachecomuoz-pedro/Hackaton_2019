# -*- coding: UTF-8 -*-
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given(u'que Ingreso al apartado de un equipo')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[3]').click()
    context.browser.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[3]/ul/li[2]').click()


@when(u'selecciono la opción dar de baja equipo')
def step_impl(context):
    tabla = context.browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div/div[3]/div/table/tbody')
    celdas = tabla.context.find_element_by_tag_name('td')
    verificacion = [item.text for item in celdas if (item.text=='Equipo a eliminar')]
    celdas.context.find_element_by_id('editar_equipo').click()


@then(u'el equipo es eliminado y se me notifica en pantalla que el equipo ya no existe y ya no pertenezco a el.')
def step_impl(context):
    pass


@given(u'que no se eliminó el equipo')
def step_impl(context):
    pass


@when(u'presionó el botón de eliminar equipo')
def step_impl(context):
    pass


@then(u'se notificará que no se eliminó y podrá intentar nuevamente')
def step_impl(context):
    pass