import pytest
from components.restaurante import Restaurante

def test_instanciacao_restaurante():
    mock_avaliacao = {"average": 4.5, "individual_ratings": []}
    restaurante = Restaurante("sabor caseiro", "brasileira", [], mock_avaliacao)
    assert restaurante._nome == "Sabor Caseiro"
    assert restaurante._categoria == "BRASILEIRA"

def test_str_retorno_formatado():
    mock_avaliacao = {"average": 4.5, "individual_ratings": []}
    restaurante = Restaurante("sabor", "fastfood", [], mock_avaliacao)
    assert str(restaurante) == "Sabor | FASTFOOD"

def test_alternar_estado():
    restaurante = Restaurante("Teste", "FastFood", [], {"average": 0, "individual_ratings": []})
    estado_inicial = restaurante._ativo
    restaurante.alternar_estado()
    assert restaurante._ativo != estado_inicial

def test_calcular_media_avaliacoes():
    mock_avaliacoes = {"average": 0, "individual_ratings": [{"rating": 4}, {"rating": 2}, {"rating": 5}]}
    restaurante = Restaurante("Teste", "FastFood", [], mock_avaliacoes)
    restaurante.calcular_media_avaliacoes()
    assert round(restaurante._avaliacoes.media, 1) == 3.7