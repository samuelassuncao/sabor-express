import pytest
from components.avaliacao_restaurante import AvaliacaoRestaurante

def test_criacao_avaliacao_restaurante():
    media = 4.2
    avaliacoes = [{"cliente": "Robson", "rating": 5}, {"cliente": "Samuel", "rating": 3}]
    avaliacao = AvaliacaoRestaurante(media, avaliacoes)
    assert avaliacao.media == media
    assert avaliacao.avaliacoes_individuais == avaliacoes
