def adicionar_item(inventario, item):
    inventario.append(item)

def listar_inventario(inventario):
    if not inventario:
        return "Inventário vazio"
    return ", ".join(inventario)
