# Proyecto 2 - Clasificación de género de películas 🎧

**Universidad:** Universidad de los Andes  
**Programa:** Maestría en Inteligencia Analítica de Datos - MIAD  
**Curso:** Machine Learning y Programación de Lenguaje Natural  
**Semestre:** 2025-1, ciclo 2  
**Organización GitHub:** [GrupoODJ](https://github.com/GrupoODJ)  
**Repositorio:** [ProyectoPelis](https://github.com/GrupoODJ/ProyectoPelis)

---

## 🎯 Descripción

En este proyecto trabajamos con una base de datos de películas que abarca una amplia gama de géneros diferentes. observación contiene el título de una película, su año de lanzamiento, la sinopsis o plot de la película (resumen de la trama de una película) y los géneros a los que pertenece. Los datos están en formato CSV, lo cual permite cargarlos rápidamente de manera tabular.

El trabajo se desarrolla colaborativamente en el archivo principal `S3P1_proyectoPelis.ipynb`, dentro de un entorno compartido de GitHub y controlado mediante ramas por integrante.

---

## 👥 Integrantes del grupo

| Nombre                      | Usuario de GitHub       | Rol Principal   |
|----------------------------|--------------------------|-----------------|
| Óscar Javier Sánchez Ruiz  | `@OsCrazo`               | _(por definir)_ |
| Clara Sierra Ossorio       | `@clairesie`             | _(por definir)_ |
| Diego Alejandro Arias      | `@Darias0185`            | _(por definir)_ |
| Leonardo Urrea Morales     | `@LeonardoUrrea`         | _(por definir)_ |

---

## 📁 Estructura del Repositorio

```
ProyectoPelis/
│
├── S3P1_proyectoPelis.ipynb # Notebook principal del proyecto
├── data/                      # Archivos de entrada
├── images/                    # Visualizaciones generadas
├── README.md                  # Este archivo
└── .gitignore                 # Exclusión de archivos innecesarios
```
---

## 🤝 Guía de colaboración para el equipo

### 1. Clonar el repositorio

```bash
git clone https://github.com/GrupoODJ/ProyectoPelis.git
cd ProyectoPelis
```

### 2. Crear una rama con tu nombre

```bash
git checkout -b tu-nombre
git push origin tu-nombre
```

Ejemplo:
```bash
git checkout -b camilo-desarrollo
```

### 3. Hacer cambios y subir

```bash
git add .
git commit -m "Descripción clara de los cambios"
git push origin tu-nombre
```

### 4. Crear un Pull Request en GitHub

- Ve a la pestaña **"Pull Requests"**.
- Haz clic en **"New Pull Request"**.
- Asegúrate que diga: `base: main ← compare: tu-rama`
- Agrega título y descripción, luego haz clic en **"Create Pull Request"**.

### 5. Revisión y merge

- El equipo puede comentar y aprobar.
- Al aprobar, haz clic en **"Merge pull request"**.
- Luego, elimina la rama si ya no se necesita.

### 🧠 Buenas prácticas

- Trabajar solo en tu rama.
- Sincroniza tu rama con `main` antes de subir:
  ```bash
  git pull origin main
  ```
- Mantén mensajes de commit claros.
- No trabajes sobre `main` directamente.
