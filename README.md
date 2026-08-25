# Global Sustainability Data Analysis

Proyecto en desarrollo para analizar acceso a la energía, transición renovable, eficiencia energética, emisiones y desarrollo económico mediante datos internacionales.

> **Estado:** estructura inicial. El análisis todavía no contiene un notebook ejecutado ni resultados cuantificados y, por tanto, no se presenta como un caso finalizado.

## Objetivo

Construir un estudio reproducible que responda cinco preguntas:

1. ¿Cómo evolucionó el acceso a la electricidad entre 2000 y 2020?
2. ¿Qué desigualdades existen en el acceso a combustibles limpios para cocinar?
3. ¿Qué relación presenta el desarrollo económico con el consumo energético?
4. ¿Cómo cambió la participación de las energías renovables?
5. ¿En qué países existe evidencia de desacoplamiento entre PIB y emisiones de CO₂?

## Fuente prevista

El plan utiliza el dataset público [Global Data on Sustainable Energy](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy), que integra indicadores procedentes de fuentes internacionales.

Los datos brutos no se almacenan en este repositorio. Consulta [data/README.md](data/README.md) para conocer el criterio de documentación.

## Variables de interés

- país y año;
- acceso a electricidad;
- acceso a combustibles limpios para cocinar;
- participación de energía renovable;
- electricidad de origen fósil y renovable;
- electricidad baja en carbono;
- consumo primario de energía por habitante;
- intensidad energética;
- emisiones de CO₂;
- PIB por habitante.

## Método previsto

1. Verificar procedencia, licencia, cobertura temporal y unidad de cada indicador.
2. Auditar estructura, nulos, duplicados y cobertura por país.
3. Evitar promedios mundiales simples cuando países con poblaciones muy distintas requieran ponderación.
4. Analizar tendencias por país, región y nivel de renta.
5. Normalizar indicadores cuando sea necesario para comparaciones válidas.
6. Evaluar el desacoplamiento mediante cambios relativos de PIB y CO₂, no solo correlaciones.
7. Separar hechos observados, interpretaciones, limitaciones y recomendaciones.

## Estructura

- [`analysis_plan.md`](analysis_plan.md): preguntas, variables y código inicial.
- [`data/README.md`](data/README.md): política y fuentes de datos.
- `README.md`: estado y documentación general.

## Criterios para considerar el proyecto completo

- notebook Jupyter válido y ejecutable;
- dataset identificado con versión y licencia;
- dimensiones y calidad de los datos documentadas;
- resultados cuantificados y gráficos con unidades;
- comparación regional o por nivel de renta;
- metodología explícita para medir desacoplamiento;
- limitaciones antes de las conclusiones;
- recomendaciones justificadas por los resultados;
- archivo de dependencias o instrucciones reproducibles.

## Riesgos metodológicos

- Un promedio no ponderado por país no equivale al porcentaje de población mundial con acceso.
- PIB, energía y emisiones tienen escalas muy asimétricas.
- Correlación no implica causalidad ni demuestra desacoplamiento.
- La ausencia de datos puede variar por país, año e indicador.
- Las definiciones y unidades deben comprobarse antes de combinar fuentes.

## Herramientas previstas

Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook

## Autor

Francisco de la Corte · [GitHub](https://github.com/francorte)
