# Global Sustainable Energy Analysis (2000–2020)

**Author:** Francisco  
**Platform:** Google Colab / Kaggle

*Autor: Francisco*  
*Plataforma: Google Colab / Kaggle*

---

## Objective

Analyze the evolution of energy access, the transition to renewable energy, and energy efficiency at a global level, with a focus on sustainability and decision support.

*Analizar la evolución del acceso a la energía, la transición hacia las energías renovables y la eficiencia energética a nivel global, con foco en sostenibilidad y apoyo a la toma de decisiones.*

---

## 1. Context and Motivation

Universal access to affordable, reliable, and sustainable energy remains one of the major global development challenges. While access to electricity has improved over the last decades, significant inequalities persist in clean cooking fuels, energy efficiency, and decarbonization.

*El acceso universal a una energía asequible, fiable y sostenible sigue siendo uno de los grandes retos del desarrollo global. Aunque el acceso a la electricidad ha mejorado en las últimas décadas, persisten importantes desigualdades en combustibles limpios, eficiencia energética y descarbonización.*

---

## 2. Analytical Questions

1. How has access to electricity evolved globally between 2000 and 2020?
2. How does access to clean cooking fuels differ across countries?
3. What is the relationship between economic development and energy consumption?
4. How has the share of renewable energy changed over time?
5. Is there evidence of decoupling between economic growth and CO₂ emissions?

*1. ¿Cómo ha evolucionado el acceso a la electricidad a nivel global entre 2000 y 2020?*  
*2. ¿Cómo difiere el acceso a combustibles limpios para cocinar entre países?*  
*3. ¿Qué relación existe entre desarrollo económico y consumo energético?*  
*4. ¿Cómo ha cambiado el peso de las energías renovables con el tiempo?*  
*5. ¿Existe evidencia de desacoplamiento entre crecimiento económico y emisiones de CO₂?*

---

## 3. Environment Setup

This section prepares the Python environment by loading the necessary libraries for data analysis and visualization.

*Esta sección prepara el entorno de Python cargando las librerías necesarias para el análisis y la visualización de datos.*

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:.2f}".format)

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
```

---

## 4. Dataset Loading

The dataset is loaded from the Kaggle input directory and inspected to confirm successful import.

*El dataset se carga desde el directorio de entrada de Kaggle y se inspecciona para confirmar que la importación ha sido correcta.*

```python
df = pd.read_csv("/kaggle/input/global-data-on-sustainable-energy/global-data-on-sustainable-energy (1).csv")
df.head()
```

---

## 5. Initial Data Exploration

This step examines the structure, data types, and completeness of the dataset in order to understand its analytical potential and limitations.

*Este paso examina la estructura, los tipos de datos y la completitud del dataset para comprender su potencial analítico y sus limitaciones.*

```python
df.info()
```

---

## 6. Data Cleaning and Variable Selection

To ensure a focused and interpretable analysis, a subset of key variables related to energy access, energy mix, emissions, and economic development is selected.

*Para garantizar un análisis enfocado e interpretable, se selecciona un subconjunto de variables clave relacionadas con acceso a la energía, mix energético, emisiones y desarrollo económico.*

```python
key_columns = [
    "Entity",
    "Year",
    "Access to electricity (% of population)",
    "Access to clean fuels for cooking",
    "Renewable energy share in the total final energy consumption (%)",
    "Electricity from fossil fuels (TWh)",
    "Electricity from renewables (TWh)",
    "Low-carbon electricity (% electricity)",
    "Primary energy consumption per capita (kWh/person)",
    "Energy intensity level of primary energy (MJ/$2017 PPP GDP)",
    "Value_co2_emissions_kt_by_country",
    "gdp_per_capita"
]

df_clean = df[key_columns].copy()
df_clean.head()
```

---

## 7. Missing Values Assessment

Before proceeding with the analysis, the proportion of missing values is evaluated to ensure transparency and guide later analytical decisions.

*Antes de continuar con el análisis, se evalúa la proporción de valores faltantes para garantizar transparencia y guiar decisiones analíticas posteriores.*

```python
df_clean.isna().mean().sort_values(ascending=False)
```

---

## 8. Exploratory Analysis: Electricity Access

The first exploratory analysis focuses on the global evolution of access to electricity, one of the core indicators of SDG 7.

*El primer análisis exploratorio se centra en la evolución global del acceso a la electricidad, uno de los indicadores clave del ODS 7.*

```python
global_electricity_access = df_clean.groupby("Year")["Access to electricity (% of population)"].mean()

global_electricity_access.plot()
plt.title("Global Average Access to Electricity (% of Population)")
plt.xlabel("Year")
plt.ylabel("Percentage of population")
plt.show()
```

---

## 9. Key Takeaways

- Global access to electricity has increased steadily over time.
- Progress is uneven across countries and regions.
- Energy access improvements do not automatically imply clean energy transitions.

*- El acceso global a la electricidad ha aumentado de forma sostenida.*  
*- El progreso es desigual entre países y regiones.*  
*- La mejora del acceso no implica automáticamente una transición hacia energías limpias.*

---

## 10. Next Steps

Future analysis may include regional segmentation, income-level comparisons, and deeper exploration of the relationship between renewables, emissions, and economic growth.

*El análisis futuro puede incluir segmentación regional, comparaciones por nivel de renta y una exploración más profunda de la relación entre renovables, emisiones y crecimiento económico.*

