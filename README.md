# Sistema Analítico Predictivo para la Gestión Sostenible del Hardware (Green IT)

**Universidad Nacional Abierta y a Distancia (UNAD)**  
**Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)**  
**Programa de Ingeniería de Sistemas | Proyecto de Grado (202016907)**  
**Fase 4 - Componente Práctico (Prototipo Funcional TRL 5)**  
**Grupo:** 19  

---

## 📌 Integrantes
* Jhonathan Orlando Muñoz
* Jessica Yulieth Olaya Montilla
* Omar Aragón Orjuela

**Tutor** Daniel Andrés Guzmán Arévalo  

---

## 🚀 Descripción del Proyecto
Este repositorio reúne los artefactos técnicos y el prototipo funcional (TRL 5) de un sistema pensado para resolver un problema concreto que enfrentan muchos departamentos de TI: no saber realmente cómo están sus equipos hasta que algo falla[cite: 4]. 

La solución monitorea una muestra controlada de 40 laptops corporativas, recopilando automáticamente variables clave como temperatura del CPU, ciclos de batería, uso del almacenamiento y consumo energético en kWh. Esos datos se procesan en Python y se visualizan en un tablero interactivo de Microsoft Power BI, con el objetivo de anticipar fallas, planificar renovaciones con criterio y reducir el impacto ambiental del hardware desechado innecesariamente.[cite: 4].

El proyecto se alinea con los principios de Green IT y contribuye directamente a las metas del ODS 9 (Industria, Innovación e Infraestructura) y el ODS 12 (Producción y Consumo Responsables).[cite: 4].

---

## 🛠️ Arquitectura Tecnológica & Artefactos
* **`data/telemetria_laptops_40.csv`**: Dataset con los registros de telemetría y variables físicas del parque informático[cite: 4].
* **`src/analitica_hardware.py`**: Script en Python para limpieza de datos (ETL), cálculo de métricas de desgaste y generación de alertas de obsolescencia[cite: 4].
* **`dashboard/Dashboard_Telemetría.pbix`**: Tablero interactivo en Power BI Desktop con indicadores de salud, dispersión térmica, proyecciones de vida útil y consumo energético[cite: 4].

---

## 📋 Mapeo de Requerimientos Funcionales (`RF`)
| Código | Requerimiento Funcional | Estado / Módulo en Prototipo |
| :--- | :--- | :--- |
| **RF-01 / RF-02** | Registro y administración de inventario | Mantenido en Dataset & Vistas de Power BI[cite: 4] |
| **RF-03** | Captura de métricas de telemetría | Dataset con CPU, RAM, Batería, kWh[cite: 4] |
| **RF-04 / RF-05** | Gestión de KPIs y Predicción de vida útil | Lógica en Python + Gráfico de Barras PBI[cite: 4] |
| **RF-06 / RF-07** | Clasificación de estado y Alertas preventivas | Tarjetas KPI + Filtro dinámico Slicer[cite: 4] |
| **RF-08** | Alertas de obsolescencia Green IT | Notificación de reemplazo en tabla interactiva[cite: 4] |
| **RF-09 / RF-10** | Dashboard interactivo y reportes | Lienzo general en Power BI Desktop[cite: 4] |

---

## 📽️ Video de Sustentación del Prototipo (Máx 10 Minutos)
* **Enlace a la grabación:** [Insertar aquí el link de YouTube / Teams / Loom][cite: 2, 3]
