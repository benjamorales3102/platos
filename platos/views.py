from django.shortcuts import render
from django.http import Http404
from .datos_platos import platos

def inicio(request):
    query = request.GET.get('q', '').strip()
    platos_filtrados = platos

    if query:
        query_lower = query.lower()
        platos_filtrados = [
            plato for plato in platos
            if query_lower in plato['nombre'].lower()
            or query_lower in plato['descripcion'].lower()
            or query_lower in plato['categoria'].lower()
        ]

    precio_total_carta = round(sum(plato["precio"] for plato in platos_filtrados))
    cantidad_vegetarianos = sum(1 for plato in platos_filtrados if plato["vegetariano"])

    return render(request, 'platos/inicio.html', {
        'platos': platos_filtrados,
        'precio_total_carta': precio_total_carta,
        'cantidad_vegetarianos': cantidad_vegetarianos,
        'query': query,
    })

def detalle(request, id):
    plato = next((p for p in platos if p["id"] == id), None)
    if plato is None:
        raise Http404("Plato no encontrado")

    precio_con_propina = round(plato["precio"] * 1.10)

    if plato["vegetariano"] and not plato["picante"]:
        etiqueta = "Apto para todos"
    elif plato["picante"]:
        etiqueta = "Contiene aji"
    else:
        etiqueta = "Plato tradicional"

    return render(request, 'platos/detalle.html', {
        'plato': plato,
        'precio_con_propina': precio_con_propina,
        'etiqueta': etiqueta,
    })

