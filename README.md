# Q-Learning Blackjack Simulation

Este é um projeto que implementa uma simulação básica de Q-Learning aplicada a um cenário inspirado em blackjack, onde o jogador aprende a tomar decisões para maximizar suas recompensas.

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-diretorio>

2. Instale ad dependências
    ```bash
   pip install -r requirements.txt 
   ```
3. Execute o Script Principal
    ```bash
    python main.py
    ```
## 📊 Funcionamento do Algoritmo

O algoritmo de Q-Learning utiliza os seguintes conceitos:

- Estados: Representam os valores somados das cartas do jogador, variando de 4 a 21.
- Ações: "Comprar" (pegar uma carta) ou "Parar" (manter a mão atual).
- Recompensas: Baseadas nas regras do blackjack:
    Se o jogador ultrapassa 21, recebe uma grande penalidade.
    Se o jogador vence o dealer, recebe uma grande recompensa.

A matriz Q resultante mostra as recompensas esperadas para cada combinação de estado e ação.
