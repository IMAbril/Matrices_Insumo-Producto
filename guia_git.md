## Guía Rápida para Colaborar en Git

### 1. **Clonar el repositorio (una sola vez por usuario)**
Cada persona debe clonar el repositorio en su máquina local. Abre la terminal y ejecuta:

```bash
git clone https://github.com/IMAbril/Matrices_Insumo-Producto.git
```

Esto descargará una copia del repositorio.

### 2. **Crear una nueva rama para cada feature o tarea**
Cada persona debe trabajar en su propia rama para evitar conflictos. Para crear y cambiar a una nueva rama:

```bash
git checkout -b nombre-de-la-rama
```

Ejemplo:

```bash
git checkout -b nueva-feature
```

### 3. **Hacer cambios y confirmar los commits**
Cada vez que realices cambios en tu rama, añade los archivos que has modificado y realiza un commit:

```bash
git add archivo-modificado.py
git commit -m "Descripción clara del cambio"
```

Puedes añadir todos los cambios a la vez con:

```bash
git add .
```

### 4. **Sincronizar tu trabajo con el repositorio remoto**

#### a. **Actualizar la rama local con los últimos cambios del repositorio remoto**
Antes de subir tus cambios, asegúrate de estar actualizado con los cambios de los demás. Cambia a la rama `main` (o `master`, según tu repositorio) y actualiza:

```bash
git checkout main
git pull origin main
```

Luego, vuelve a tu rama:

```bash
git checkout nombre-de-la-rama
```

Fusiona los últimos cambios de `main` en tu rama para evitar conflictos posteriores:

```bash
git merge main
```

#### b. **Subir tu trabajo al repositorio remoto**
Una vez que has fusionado los últimos cambios de `main`, puedes subir tu trabajo:

```bash
git push origin nombre-de-la-rama
```

### 5. **Crear un Pull Request (PR)**
Para integrar tus cambios en la rama principal (`main`), debes crear un Pull Request. Esto se hace directamente en GitHub:

1. Ve al repositorio en GitHub.
2. En la pestaña **Pull Requests**, haz clic en **New Pull Request**.
3. Selecciona la rama que acabas de subir y envía la solicitud para revisión.

### 6. **Revisar y aprobar Pull Requests**
Antes de fusionar el Pull Request, uno de tus compañeros debe revisarlo y aprobarlo. La revisión asegura que los cambios no rompan el código existente.

- **Revisar el código** en la pestaña de "Files changed".
- **Dejar comentarios** si es necesario.
- Si está todo bien, **aprobar el Pull Request**.

### 7. **Fusionar el Pull Request a `main`**
Una vez aprobado, alguien puede fusionar el Pull Request. Esto integrará los cambios en la rama principal (`main`).

### 8. **Eliminar ramas innecesarias**
Después de fusionar, es recomendable eliminar la rama para evitar confusión:

```bash
git branch -d nombre-de-la-rama
```

También puedes eliminar la rama en el repositorio remoto desde GitHub o con el comando:

```bash
git push origin --delete nombre-de-la-rama
```

### 9. **Mantén siempre tu rama actualizada**
Es importante que antes de comenzar a trabajar o antes de hacer un push, sincronices tu rama local con `main` para evitar conflictos:

```bash
git fetch origin
git checkout main
git pull origin main
```

---

### Resumen de comandos principales:

- **Clonar el repositorio**: `git clone <URL>`
- **Crear y cambiar de rama**: `git checkout -b nombre-de-la-rama`
- **Añadir cambios al commit**: `git add .`
- **Confirmar cambios**: `git commit -m "mensaje"`
- **Actualizar la rama principal**: `git pull origin main`
- **Fusionar `main` en tu rama**: `git merge main`
- **Subir tu rama**: `git push origin nombre-de-la-rama`
- **Crear un Pull Request**: Desde GitHub
- **Eliminar rama local**: `git branch -d nombre-de-la-rama`
- **Eliminar rama remota**: `git push origin --delete nombre-de-la-rama`

Con estos pasos, tú y tus compañeros podrán colaborar de manera eficiente en el proyecto, minimizando conflictos y manteniendo el flujo de trabajo organizado.
