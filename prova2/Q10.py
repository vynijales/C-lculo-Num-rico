from scipy.interpolate import CubicSpline

x = (0, 0.5, 1.0, 1.5, 2.0)
y = (3, 1.8616, -0.5571, -4.1987, -9.0536)

spline = CubicSpline(x, y)
res = spline(0.25)

print(f"Valor aproximado por spline cúbica: {res}")
