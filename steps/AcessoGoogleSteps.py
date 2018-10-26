from behave import given,when,then


@given(u'Acesso google')
def step_impl(context):
    context.app.pagina('https://www.google.com.br/')
    context.app.escreve('lst-ib','teste','id')

    


@when(u'Efetuo uma pesquisa')
def step_impl(context):
    pass

@then(u'Obtenho o resultado')
def step_impl(context):
    pass