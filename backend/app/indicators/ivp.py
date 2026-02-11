def calculate_ivp(renda, moradia, alimentacao, transporte, servicos):
    custo_total = moradia + alimentacao + transporte + servicos

    if custo_total == 0:
        return {"erro": "Custo total não pode ser zero"}

    ivp = renda / custo_total

    return {
        "ivp": round(ivp, 2)
    }
