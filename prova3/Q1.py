# Dados fornecidos
x = [0, 80, 160, 240, 320, 400, 480, 560, 640, 720, 800, 880, 960, 1040, 1120, 1200]
y_above = [0, 0, 0, 0, 0, 480, 480, 480, 260, 230, 220, 200, 190, 225, 190, 0]
y_below = [0, -90, -160, -310, -330, -245, -245, -340, -475, -600, -640, -650, -410, -370, -245, -240]

# Ponto central
def midpoint_composite(x, y):
    integral = 0
    for i in range(len(x) - 1):
        h = x[i+1] - x[i]
        midpoint = (y[i] + y[i+1]) / 2
        integral += midpoint * h
    return integral

# Simpson 3/8 composto
def simpson_38_composite(x, y):
    integral = 0
    for i in range(0, len(x) - 1, 3):
        h = x[i+1] - x[i]
        integral += (y[i] + 3*y[i+1] + 3*y[i+2] + y[i+3]) * (3*h / 8)
    return integral

if __name__ == "__main__":
    # Calculando as áreas acima e abaixo do eixo x usando ambos os métodos
    area_acima_midpoint = midpoint_composite(x, y_above)
    area_abaixo_midpoint = midpoint_composite(x, y_below)
    area_midpoint = area_acima_midpoint + abs(area_abaixo_midpoint)

    area_acima_simpson = simpson_38_composite(x, y_above)
    area_abaixo_simpson = simpson_38_composite(x, y_below)
    area_simpson = area_acima_simpson + abs(area_abaixo_simpson)

    # Exibindo os resultados
    print(f"Área total usando o método do ponto central composto: {area_midpoint} km²")
    print(f"Área total usando o método de Simpson 3/8 composto: {area_simpson} km²")