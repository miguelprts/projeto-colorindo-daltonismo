# test/test_core.py
import pytest
from app.services.color_manager import ColorManager
from app.data.repository import ColorRepository
from app.services.translation import GoogleTranslationService
from unittest.mock import MagicMock
from app.core.math_utils import PerceptualColorMath # Importe o serviço aqui

def test_busca_fuzzy_rigorosa_95_percent_RD05():
    """
    Valida o novo requisito de similaridade de 95% (RD05).
    Evidência de Injeção de Dependência (SOLID - DIP).
    """
    # Passo 1: Instanciar a dependência
    math_service = PerceptualColorMath()
    
    # Passo 2: Injetar a dependência no repositório
    repo = ColorRepository(csv_path="color_names.csv", math_service=math_service)
    
    # Caso 1: Nome idêntico (deve passar)
    result_exact, sim_exact = repo.find_by_name_fuzzy("Red")
    
    assert result_exact is not None
    assert sim_exact >= 0.95

def test_calculo_distancia_hsl_RF06():
    math_service = PerceptualColorMath()
    
    # Cores idênticas devem ter distância zero
    cor_a = (120, 50, 50) # Verde
    assert math_service.calculate_distance(cor_a, cor_a) == 0
    
    # Verde (120) deve ser mais perto de Ciano (180) do que de Vermelho (0)
    dist_verde_ciano = math_service.calculate_distance((120, 100, 50), (180, 100, 50))
    dist_verde_vermelho = math_service.calculate_distance((120, 100, 50), (0, 100, 50))
    assert dist_verde_ciano < dist_verde_vermelho

def test_traducao_e_cache_RD03():
    service = GoogleTranslationService()
    
    # Teste de tradução simples
    resultado = service.translate("Red", target="pt")
    assert resultado.lower() == "vermelho"
    
    # O segundo chamado deve vir do cache (comportamento interno do Python)
    resultado_cache = service.translate("Red", target="pt")
    assert resultado_cache == resultado

def test_fluxo_completo_identificacao_95_percent():
    # Setup com Injeção de Dependência (SOLID)
    math_service = PerceptualColorMath()
    repo = ColorRepository(csv_path="color_names.csv", math_service=math_service)
    trans = GoogleTranslationService()
    manager = ColorManager(repo=repo, translator=trans)
    
    # Testando identificação HEX (RF01)
    # Supondo que #FF0000 esteja no CSV como "Red"
    resultado = manager.identify_by_hex("#FF0000")
    assert "name_pt_br" in resultado
    assert resultado["name_pt_br"] == "Vermelho"
    
def test_busca_fuzzy_sem_correspondencia():
    """Valida que a busca retorna None quando a similaridade é baixa (abaixo de 95%)."""
    math_service = PerceptualColorMath()
    repo = ColorRepository(csv_path="color_names.csv", math_service=math_service)
    
    # Nome completamente aleatório que não deve atingir 95% de similaridade
    result, similarity = repo.find_by_name_fuzzy("XyZ123_NonExistent")
    
    assert result is None
    assert similarity < 0.95

def test_busca_fuzzy_quase_perfeita_94_percent():
    """
    Testa uma string muito parecida, mas que falha por pouco no rigor de 95%.
    Se 'Amazonite' for a cor, 'Amazonit' (sem o e) pode resultar em ~0.94.
    """
    math_service = PerceptualColorMath()
    repo = ColorRepository(csv_path="color_names.csv", math_service=math_service)
    
    # Simulação de um erro de digitação leve que fique abaixo de 95%
    result, similarity = repo.find_by_name_fuzzy("Amazonit") 
    
    # Se a similaridade for, por exemplo, 0.94, deve retornar None para ser rigoroso
    if similarity < 0.95:
        assert result is None
    else:
        assert result is not None

def test_find_nearest_by_hex_perfeito():
    """Valida se o cálculo de distância HSL identifica cor idêntica como distância 0."""
    math_service = PerceptualColorMath()
    repo = ColorRepository(csv_path="color_names.csv", math_service=math_service)
    
    # Escolha um HEX que você SABE que existe no seu CSV (ex: 00C4B0 para Amazonite)
    result, distance = repo.find_nearest_by_hex("#00C4B0")
    
    assert distance == 0
    assert result['Name'] == "Amazonite"

def test_identify_by_hex_invalido():
    """Valida comportamento do Manager com HEX malformatado."""
    math_service = PerceptualColorMath()
    repo = ColorRepository(csv_path="color_names.csv", math_service=math_service)
    manager = ColorManager(repo=repo, translator=GoogleTranslationService())

    # HEX inválido
    with pytest.raises(ValueError): # Ou o comportamento que você definiu
        manager.identify_by_hex("INVALID_HEX")

def test_calculo_distancia_extremos_hsl():
    math_service = PerceptualColorMath()
    
    # Branco vs Preto (Extremos de Luminosidade)
    cor_branca = (0, 0, 100)
    cor_preta = (0, 0, 0)
    distancia = math_service.calculate_distance(cor_branca, cor_preta)
    
    assert distancia > 0
    # Valida que o cálculo é comutativo (dist A-B == B-A)
    assert math_service.calculate_distance(cor_branca, cor_preta) == \
           math_service.calculate_distance(cor_preta, cor_branca)