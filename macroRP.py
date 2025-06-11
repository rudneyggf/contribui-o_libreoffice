import uno


def get_rp_conversion_rate():
    soma_divisoes_rp_por_real = 30.42 + 32.83 + 33.37 + 33.86 + 34.22 + 35.53
    media = soma_divisoes_rp_por_real/6
    return media


def converter_para_reais():
    context = uno.getComponentContext()
    serviceManager = context.ServiceManager
    desktop = serviceManager.createInstanceWithContext(
        "com.sun.star.frame.Desktop", context)
    model = desktop.getCurrentComponent()

    intervalo = model.CurrentSelection

    try:
        real_por_rp = get_rp_conversion_rate()
    except Exception as e:
        print("Erro ao obter taxa de conversão:", e)
        return

    num_rows = intervalo.Rows.Count
    num_cols = intervalo.Columns.Count

    for i in range(num_rows):
        for j in range(num_cols):
            celula = intervalo.getCellByPosition(j, i)

            # Garante que o termo será um float
            try:
                valor = float(celula.Value)
            except Exception:
                celula.String = "Erro ao converter"
                continue

            rp = celula.Value

            # Impede que a conversão com números negativos ocorra
            if valor <= 0:
                celula.String = "Erro ao converter"
                continue

            valor_reais = rp / real_por_rp
            celula.Value = round(valor_reais, 2)
