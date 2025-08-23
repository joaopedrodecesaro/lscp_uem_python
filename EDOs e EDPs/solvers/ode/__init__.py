print("\nResolver problemas de EDOs com scipy.integrate.")
print("Métodos disponíveis para escolher:")
print("  - 'RK23': Método de Runge-Kutta explícito de ordem 2(3).")
print("  - 'RK45': Método de Runge-Kutta explícito de ordem 4(5).")
print("  - 'DOP853': Método de Runge-Kutta explícito de ordem 8.")
print("  - 'Radau': Método de Runge-Kutta implícito da família Radau IIA de ordem 5.")
print(
    "  - 'BDF': Método implícito multi-passo de ordem variável (1 a 5) baseado em fórmulas de diferenciação retroativa."
)
print("  - 'LSODA': Método Adams/BDF com detecção automática de rigidez e comutação.")
print("Se você precsisa de desempenho, leia a discussão abaixo:")
print(
    "https://www.reddit.com/r/Python/comments/1ca4bwy/what_is_currently_the_fasteststateoftheart_ode/\n"
)
