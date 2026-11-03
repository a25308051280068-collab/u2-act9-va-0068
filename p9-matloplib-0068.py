# Nombre: Christian garcia Jimenez
# NC: 0068
print("Christian garcia Jimenez Nc n= 0068")
# NC: 0068

import matplotlib.pyplot as plt

materias = ['Matemáticas', 'Física', 'Programación', 'Química', 'Inglés']
calificaciones = [85, 90, 95, 78, 88]

plt.pie(calificaciones, labels=materias, autopct='%1.1f%%')

plt.title("Calificaciones - NC: 0068")
plt.xlabel("Materias", labelpad=15)
plt.ylabel("Calificaciones", labelpad=30)  # Separación adicional del eje Y

# Organiza automáticamente los espacios para evitar empalmes
plt.tight_layout()

plt.savefig("grafica_pie.png")
plt.show()

print("Nombre completo: [Tu Nombre Completo Aquí]")
print("Christian garcia Jimenez Nc n= 0068")