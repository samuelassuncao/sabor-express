import pytest
from unittest.mock import patch, MagicMock
from components.restaurantes import Restaurantes

def test_obter_restaurantes_com_dados_validos():
    data = {
        "restaurants": [
            {"name": "Sabor", "category": "FastFood", "menu": [], "ratings": {"average": 4, "individual_ratings": []}},
            {"name": "Caseiro", "category": "Brasileira", "menu": [], "ratings": {"average": 5, "individual_ratings": []}}
        ]
    }
    with patch("components.restaurantes.Restaurante") as MockRestaurante:
        MockRestaurante.side_effect = lambda **kwargs: MagicMock(**kwargs)
        restaurantes = Restaurantes(data)
        assert len(restaurantes._lista_de_restaurantes) == 2

def test_obter_restaurantes_lista_vazia():
    data = {"restaurants": []}
    restaurantes = Restaurantes(data)
    assert restaurantes._lista_de_restaurantes == []
