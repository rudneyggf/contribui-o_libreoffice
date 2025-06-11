import uno
import math


def get_rp_conversion_rate():
    reais = 18.90
    rp = 575
    return rp / reais  # Aproximadamente 8.29 RP por real


def converter_para_rp():
    context = uno.getComponentContext()
    serviceManager = context.ServiceManager
    desktop = serviceManager.createInstanceWithContext(
        "com.sun.star.frame.Desktop", context)
    model = desktop.getCurrentComponent()

    intervalo = model.CurrentSelection

    try:
        rp_por_real = get_rp_conversion_rate()
    except Exception as e:
        print("Erro ao obter taxa de conversão:", e)
        return

    num_rows = intervalo.Rows.Count
    num_cols = intervalo.Columns.Count

    for i in range(num_rows):
        for j in range(num_cols):
            celula = intervalo.getCellByPosition(j, i)
            valor = celula.Value
            rp = valor * rp_por_real
            celula.Value = math.ceil(rp)
