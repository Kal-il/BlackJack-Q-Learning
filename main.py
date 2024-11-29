from tabulate import tabulate
import numpy as np

# Definição de valores indicadas pelo artigo
alpha = 0.30
gamma = 0.15
epsilon = 0.01

states_num = 18  # de 4 à 21
actions_num = 2  # comprar ou para de comprar
Q = np.zeros((states_num, actions_num))


# A taxa aprendizado (0 < αlpha ≤ 1) regula a velocidade em que as
# novas informaçõoes sobrepõem-se sobre o aprendizado já
# armazenado na matriz Q

np.random.seed(42)

def select_action(current_state):
    adjusted_state = current_state - 4
    if np.random.rand() < epsilon:
        return np.random.choice(actions_num)
    return np.argmax(Q[adjusted_state])

def dealer():
    stop = False
    dealer_cards = 0
    while not stop:
        dealer_cards += np.random.randint(1, 11)
        # print("Dealer Cards:", dealer_cards)
        if dealer_cards > 16:
            stop = True
    return dealer_cards




def reward_function(current_state, action, next_state):
    if next_state > 21:
        return -1000 * abs(21 - current_state)
    elif action == 1:
        dealer_cards = dealer()
        if dealer_cards > 21 or current_state > dealer_cards:
            return 1000
        elif current_state == dealer_cards:
            return 1000
        else:
            return -1000 * abs(21 - current_state)
    else:  # Comprar
        return 1000 if next_state <= 21 else -1000 * abs(21 - current_state)


if __name__ == '__main__':

    for eps in range(50):
        current_state = np.random.randint(4, 21)
        end = False

        while not end:
            adjusted_state = current_state - 4 # foi preciso fazer uma correção do indice, pois os valores do blackjack, vão de 4 à 21, enquanto a indexação vai de 0 à 17
            action = select_action(current_state)
            # print(action)
            if action == 0:
                next_state = current_state + np.random.randint(1, 11)
            else:
                next_state = current_state

            next_adjusted_state = next_state - 4 if next_state <= 21 else 17

            R = reward_function(current_state, action, next_state)

            Q[adjusted_state][action] = Q[adjusted_state][action] + alpha * (
                    R + gamma * np.max(Q[next_adjusted_state]) - Q[adjusted_state][action]
            )

            current_state = next_state
            if action == 1 or current_state > 21:
                end = True

    # Preparação da tabela para impressão
    states = list(range(4, 22))  # Estados de 4 a 21
    headers = ["Estado", "Comprar", "Parar"]
    table_data = [[state, Q[state - 4, 0], Q[state - 4, 1]] for state in states]

    # Impressão formatada
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))