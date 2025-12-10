from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"Testando {carro.__class__.__name__}: ")
    carro.acelera()
    carro.exibe_velocidade()

if __name__ == "__main___":
    carro_inteligente = CarroInteligente(10)
    print("Carro Inteligente: ")
    carro_inteligente.acelera()
    test_drive(carro_inteligente)
    carro_esportivo = CarroEsportivo(50)

    print("Carro Esportivo: ")
    carro_esportivo.turbo()
    test_drive(carro_esportivo)

    print("Carro de Corrida:")
    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)

