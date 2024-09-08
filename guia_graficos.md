# Guía rápida para crear gráficos en Python usando la biblioteca **Matplotlib**

### 1. **Instalar Matplotlib**
Si no tienes la biblioteca instalada, puedes hacerlo con:
```bash
pip install matplotlib
```

### 2. **Importar Matplotlib**
```python
import matplotlib.pyplot as plt
```

### 3. **Tipos Básicos de Gráficos**

#### a. **Gráfico de Líneas**
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Gráfico de Líneas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
```

#### b. **Gráfico de Barras**
```python
import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [3, 8, 1, 10]

plt.bar(x, y)
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()
```

#### c. **Gráfico de Dispersión**
```python
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y)
plt.title("Gráfico de Dispersión")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

#### d. **Histograma**
```python
import matplotlib.pyplot as plt

data = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7]

plt.hist(data, bins=5)
plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
```

### 4. **Ajustes Comunes**
- **Colores**: Puedes cambiar los colores de los gráficos. Por ejemplo:
```python
plt.plot(x, y, color='red')
```
- **Estilos de línea**: Puedes usar diferentes estilos como `'-'`, `'--'`, `':'`, etc.:
```python
plt.plot(x, y, linestyle='--')
```
- **Marcadores**: Añadir marcadores a los puntos:
```python
plt.plot(x, y, marker='o')
```

### 5. **Subplots (Varios gráficos en una figura)**
Puedes crear varias gráficas en una misma figura usando `subplot`.
```python
import matplotlib.pyplot as plt

# Crear una figura con dos subgráficos
plt.subplot(1, 2, 1)  # 1 fila, 2 columnas, gráfico 1
plt.plot(x, y)
plt.title("Gráfico 1")

plt.subplot(1, 2, 2)  # 1 fila, 2 columnas, gráfico 2
plt.bar(x, y)
plt.title("Gráfico 2")

plt.tight_layout()  # Para ajustar el espacio entre subplots
plt.show()
```

### 6. **Guardar Gráficos**
Para guardar la gráfica en un archivo:
```python
plt.plot(x, y)
plt.savefig("grafico.png")  # Guarda como PNG
plt.savefig("grafico.pdf")  # Guarda como PDF
```

#### Guardar gráficos en una carpeta específica 
Para guardar los gráficos en una carpeta específica, puedes usar el módulo `os` de Python para asegurarte de que la carpeta existe o crearla si no existe, y luego especificar la ruta completa en el momento de guardar el gráfico.


### 6.1. **Importar el Módulo `os`**
Este módulo te permite trabajar con rutas y directorios del sistema de archivos.
```python
import os
import matplotlib.pyplot as plt
```

### 6.2. **Crear o Verificar la Carpeta**
Antes de guardar el gráfico, verificamos si la carpeta existe, y si no, la creamos usando `os.makedirs()`.

```python
# Definir la ruta de la carpeta
folder_path = 'graficos_guardados'

# Crear la carpeta si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
```

### 6.3. **Guardar el Gráfico en la Carpeta**
Cuando guardes el gráfico, especifica la ruta completa incluyendo la carpeta.

```python
# Crear datos de ejemplo
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Crear el gráfico
plt.plot(x, y)
plt.title("Gráfico de Ejemplo")

# Guardar el gráfico en la carpeta
file_name = 'grafico_ejemplo.png'
plt.savefig(os.path.join(folder_path, file_name))
```

### Código Completo
Aquí tienes el código completo que guarda el gráfico en una carpeta específica:
```python
import os
import matplotlib.pyplot as plt

# Definir la ruta de la carpeta
folder_path = 'graficos_guardados'

# Crear la carpeta si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Crear datos de ejemplo
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Crear el gráfico
plt.plot(x, y)
plt.title("Gráfico de Ejemplo")

# Guardar el gráfico en la carpeta
file_name = 'grafico_ejemplo.png'
plt.savefig(os.path.join(folder_path, file_name))

# Mostrar el gráfico
plt.show()
```

#### Notas:
- La variable `folder_path` define la ruta de la carpeta donde quieres guardar los gráficos.
- La función `os.path.join(folder_path, file_name)` se utiliza para crear la ruta completa del archivo dentro de la carpeta.
- Puedes cambiar `file_name` para personalizar el nombre de cada gráfico que guardes.

 
### 7. **Personalización Avanzada**
Matplotlib te permite personalizar los gráficos de forma muy detallada, como ajustar la cuadrícula, los ejes, anotaciones, etc.
```python
plt.grid(True)  # Añadir cuadrícula
plt.xlim(0, 5)  # Limitar el eje X
plt.ylim(0, 35)  # Limitar el eje Y
```

### 8. **Gráficos en 3D (Opcional)**
Si quieres hacer gráficos en 3D, necesitas importar el módulo `Axes3D`:
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
z = [2, 3, 5, 7]

ax.plot(x, y, z)
plt.show()
```

