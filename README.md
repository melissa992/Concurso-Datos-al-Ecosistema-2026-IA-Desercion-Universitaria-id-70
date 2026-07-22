# CM IA

# Observatorio Inteligente para el Análisis y Predicción de la Deserción Universitaria

## Concurso Datos al Ecosistema 2026 – IA para Colombia

Categoría: **Educación – Nivel Intermedio**

El objetivo es combinar una aplicación web con un backend de análisis para explorar y comprender los patrones de deserción universitaria a partir de datos abiertos.

## README

Título del Proyecto

Sistema Inteligente para la Predicción del Riesgo de Deserción Universitaria mediante Inteligencia Artificial

Problema abordado

La deserción universitaria representa un desafío para las instituciones de educación superior debido a sus impactos académicos, económicos y sociales. Generalmente, las universidades identifican estudiantes en riesgo cuando ya presentan problemas críticos, dificultando una intervención oportuna.

Este proyecto desarrolla una plataforma basada en Inteligencia Artificial que permite predecir el riesgo de deserción estudiantil a partir de variables académicas y socioeconómicas, facilitando la toma de decisiones preventivas.

Justificación (Valor público o empresarial)

La solución permite que las instituciones educativas identifiquen tempranamente estudiantes con riesgo de abandonar sus estudios, optimizando recursos destinados al acompañamiento académico y mejorando la permanencia estudiantil.

Su implementación contribuye a:

Reducir la deserción.
Mejorar indicadores institucionales.
Optimizar programas de apoyo.
Apoyar la toma de decisiones basada en datos.

---

# Descripción

CM IA es una plataforma inteligente que integra **datos abiertos, inteligencia artificial y visualización interactiva** para analizar el fenómeno de la deserción universitaria en Colombia.

Cantidad del Dataset utilizado

3

## Estructura del proyecto

La solución permite explorar información histórica, identificar patrones de comportamiento y estimar el riesgo de deserción mediante modelos de Machine Learning, facilitando la toma de decisiones basada en datos para instituciones de educación superior, investigadores y entidades gubernamentales.

El proyecto fue desarrollado utilizando tecnologías modernas para ofrecer una arquitectura modular, escalable y fácilmente desplegable en la nube.

---

# Objetivo

Desarrollar una plataforma tecnológica que aproveche datos abiertos e inteligencia artificial para apoyar el análisis de la deserción universitaria, proporcionando herramientas de consulta, visualización y predicción que contribuyan al diseño de estrategias de permanencia estudiantil.

---

# Problemática

La deserción universitaria representa uno de los principales desafíos del sistema educativo colombiano debido a factores académicos, económicos y sociales.

Aunque existen múltiples fuentes de información pública, estos datos generalmente se encuentran dispersos y sin herramientas analíticas que permitan interpretarlos de forma sencilla.

CM IA centraliza estos datos y los transforma en información útil mediante inteligencia artificial y analítica de datos.

---

# Arquitectura de la solución

La solución está compuesta por tres componentes principales.

## Frontend

Aplicación web desarrollada con:

- React 18
- Vite
- React Router
- HTML5
- CSS3
- JavaScript

Funciones principales:

- Visualización de indicadores
- Navegación por módulos
- Consulta de datos
- Consumo de la API REST
- Integración con Power BI

---

## Backend

API REST desarrollada con:

- FastAPI
- Python 3
- Uvicorn
- Pandas
- NumPy
- Scikit-learn

Responsabilidades:

- Procesamiento de datasets
- Limpieza y transformación de datos
- Generación de estadísticas
- Entrenamiento y ejecución del modelo de IA
- Exposición de servicios REST

---

## Inteligencia Artificial

El proyecto incorpora un modelo de clasificación supervisada utilizando **Random Forest**, seleccionado por su capacidad para:

- manejar variables categóricas y numéricas,
- reducir el sobreajuste mediante árboles múltiples,
- ofrecer buena precisión con datos tabulares,
- identificar la importancia de las variables.

El modelo permite estimar la probabilidad de deserción de un estudiante a partir de las características presentes en los datos abiertos.

---

# Flujo del sistema

```
Datos Abiertos Colombia
            │
            ▼
   Limpieza de datos
            │
            ▼
Procesamiento con Pandas
            │
            ▼
Modelo Random Forest
            │
            ▼
API FastAPI
            │
            ▼
Frontend React
            │
            ▼
Dashboard Power BI
```

---

# Tecnologías utilizadas

## Frontend

- React
- Vite
- React Router

## Backend

- FastAPI
- Python
- Uvicorn

## Ciencia de Datos

- Pandas
- NumPy
- Scikit-learn

## Visualización

- Power BI

## Despliegue

- Vercel (Frontend)
- Render (Backend)

---

# Modelo de Inteligencia Artificial

El modelo implementado corresponde a un algoritmo de clasificación Random Forest.

## Variables utilizadas

Entre las variables analizadas se encuentran:

- nivel académico
- programa
- periodo académico
- estado del estudiante
- características registradas en los conjuntos de datos abiertos

## Salida del modelo

El modelo estima la probabilidad de que un estudiante pertenezca a una categoría asociada con riesgo de deserción, proporcionando un apoyo para el análisis institucional.

---

# Valor agregado

CM IA aporta valor mediante:

- Integración de múltiples conjuntos de datos abiertos.
- Plataforma web de acceso sencillo.
- Predicción basada en inteligencia artificial.
- Dashboard interactivo para análisis visual.
- Arquitectura desacoplada entre frontend y backend.
- Solución completamente desplegada en la nube.
- Uso exclusivo de tecnologías de código abierto.

---

# Escalabilidad

La arquitectura fue diseñada para crecer de forma modular.

Entre las posibilidades de escalamiento se encuentran:

- incorporación de nuevos conjuntos de datos;
- entrenamiento periódico del modelo con información actualizada;
- integración con bases de datos institucionales;
- incorporación de nuevos algoritmos de Machine Learning;
- despliegue en servicios cloud con balanceo de carga;
- integración mediante APIs con otras plataformas educativas.

Gracias a la separación entre frontend, backend y modelo de IA, cada componente puede evolucionar independientemente sin afectar el funcionamiento general del sistema.

---

# Estructura del proyecto

```
CM-IA/

frontend/
│
├── src/
├── public/
└── package.json

backend/
│
├── app/
├── models/
├── services/
├── requirements.txt
└── main.py

data/

docs/

powerbi/

README.md
```

---

# Instalación

## Clonar el repositorio

```bash
git clone https://github.com/melissa992/Concurso-Datos-al-Ecosistema-2026-IA-Desercion-Universitaria-id-70.git
```

---

## Instalar Frontend

```bash
cd frontend
npm install
```

Ejecutar

```bash
npm run dev
```

---

## Instalar Backend

```bash
cd backend
pip install -r requirements.txt
```

Ejecutar

```bash
uvicorn app.main:app --reload
```

Documentación Swagger

```
http://localhost:8000/docs
```

---

# Datos utilizados

La solución utiliza conjuntos de datos abiertos publicados por el Gobierno de Colombia.

| Dataset                                 | Fuente                                                                                        |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| Deserción Académica Pregrado y Posgrado | https://www.datos.gov.co/dataset/DESERCION-ACADEMICA-PREGRADO-Y-POSGRADO/3iew-7wpx/about_data |
| Deserción No Académica 1-2019           | https://www.datos.gov.co/Educaci-n/Deserci-n-no-acad-mica-1-2019/fhn9-rk3r/about_data         |
| Deserción No Académica 2-2019           | https://www.datos.gov.co/Educaci-n/Deserci-n-no-acad-mica-2-2019/uxa5-pmvd/about_data         |

---

# Estado del proyecto

- Frontend funcional
- Backend funcional
- ✅ API REST
- ✅ Modelo de Machine Learning
- ✅ Dashboard Power BI
- ✅ Despliegue en la nube

---

# Enlaces

## Repositorio

https://github.com/melissa992/Concurso-Datos-al-Ecosistema-2026-IA-Desercion-Universitaria-id-70

## Aplicación Web

https://concurso-datos-al-ecosistema-2026-i-seven.vercel.app/

---

# Equipo de desarrollo

**Angie Melissa Ocoro Hurtado**  
Ingeniería de Sistemas  
Universidad del Valle

**Juan Camilo López Quintana**  
Ingeniería de Sistemas  
Universidad del Valle

---

# Impacto esperado

CM IA busca contribuir al fortalecimiento de la permanencia estudiantil mediante el análisis inteligente de datos abiertos, facilitando la identificación temprana de factores asociados a la deserción y apoyando la formulación de estrategias institucionales basadas en evidencia.

---

# Licencia

Proyecto desarrollado para el Concurso **Datos al Ecosistema 2026 – IA para Colombia**.

Uso académico e investigativo.
