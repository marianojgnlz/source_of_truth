# 5. El Rol de las Tecnologías de la Información (TI)

Este documento explora la relevancia de las Tecnologías de la Información (TI) en la implementación de los Sistemas de Información (SI), su impacto en la organización y la distinción entre estrategias de SI y TI.

```mermaid
mindmap
  root("Rol de las Tecnologías de Información (TI)")
    ("Relevancia de las TI")
      ("Aunque necesidad inicial es SI, tecnología es relevante")
      ("TI" ~colon~ "Conjunto de recursos tecnológicos para implementar SI")
        ("Aplicaciones")
        ("Comunicaciones")
        ("Dispositivos de acceso")
      ("Punto de contacto TI-SI" ~colon~ "Solución a problemas comunes (almacenamiento, tratamiento rápido, comunicaciones automáticas)")
    ("Impacto de la Adopción Tecnológica")
      ("No es hacer lo mismo de otra manera")
      ("Tecnología NO ES NEUTRAL, aporta idiosincrasia")
      ("Implica cambios organizacionales")
      ("Si se quiere operar igual, no cambiar tecnología")
    ("Responsabilidad y Evaluación Crítica")
      ("Alguien debe estar al día y ser crítico con TI (desde perspectiva SI)")
      ("Situaciones con tecnología")
        ("Mejores maneras de hacer las cosas")
        ("Peores maneras (eficientes pero menos efectivas)")
      ("Imprescindible conocer posibilidades de TI para el SI")
    ("Estrategias de SI (Demanda) vs. Estrategias de TI (Oferta)")
      ("Estrategia de SI (Demanda)")
        ("Determinación de demanda de aplicaciones")
        ("Identificación de demandas de información")
      ("Estrategia de TI (Oferta)")
        ("Satisfacción de la demanda de aplicaciones")
        ("Cómo la tecnología satisface la demanda")
      ("Diagrama" ~colon~ "Flujo Negocio -> Estrategia SI -> Estrategia TI")
```

[< Volver al Índice Principal](./00_Indice_SI_TI.md) | [Anterior: 4. El Sistema de Información y los demás Sistemas de la Empresa](./04_SI_Otros_Sistemas_Empresa.md)

## Relevancia de las TI

A pesar de que la necesidad inicial se plantea en términos de SI, la tecnología es **relevante y puede llegar a serlo mucho**.

Las **TI son el conjunto de recursos tecnológicos utilizados para la implementación de los SI**. Como mínimo, están conformados por:
*   Aplicaciones.
*   Comunicaciones.
*   Todo dispositivo necesario para acceder a la información.

El punto de contacto inicial entre TI y SI es la provisión de soluciones a problemas comunes en la implementación de SI:
*   Almacenamiento de datos y acceso flexible a los mismos.
*   Tratamiento de datos rápido y con pocos errores.
*   Comunicaciones automáticas.

## Impacto de la Adopción Tecnológica

Es crucial entender que, al utilizar TI en la implementación de SI, a menudo **no será posible simplemente hacer lo mismo que antes y de la misma manera**, sólo que utilizando una tecnología diferente. Esto se debe a que **la tecnología no es neutral**, sino que aporta su propia idiosincrasia.

Cuando se toma una decisión de estrategia tecnológica (ETI), la tecnología cambia el modo en que se realizan las tareas. Al adoptar una nueva tecnología, se deben considerar y advertir los **cambios organizacionales** que implicará.

> Si una organización quiere seguir operando de la misma forma, no debería realizar un cambio tecnológico significativo.

Un cambio tecnológico impactará en cómo se realizan las tareas en la organización.

## Responsabilidad y Evaluación Crítica

Alguien en la estructura organizativa debe responsabilizarse de:
*   Estar al día acerca de las cambiantes posibilidades de las TI.
*   Mantener una actitud crítica frente a las mismas desde la perspectiva de las necesidades de SI.

Se pueden dar dos situaciones con la tecnología:
1.  Que aporte **mejores maneras de hacer las cosas**.
2.  Que fuerce a tener que hacerlas de **maneras peores** (quizás más eficientes, pero menos efectivas).

Es imprescindible conocer claramente las posibilidades de la tecnología en términos de lo que puede aportar para el SI de la empresa.

## Estrategias de SI (Demanda) vs. Estrategias de TI (Oferta)

*   **Estrategias de SI (Demanda)**:
    *   Consisten en la **determinación de la demanda de aplicaciones**.
    *   Se identifican demandas de información que deben ser satisfechas mediante tales aplicaciones.

*   **Estrategias de TI (Oferta)**:
    *   Se enfocan en la **satisfacción de la demanda de aplicaciones**.
    *   Definen las formas en las que esa demanda de información puede ser satisfecha mediante la tecnología.

```mermaid
graph LR
    EstrategiaNegocio[Estrategia de Negocio] --> EstrategiaSI[Estrategia de SI (Demanda)]
    EstrategiaSI --> NecesidadesInformacion[Necesidades de Información]
    NecesidadesInformacion --> DemandaAplicaciones[Demanda de Aplicaciones]
    DemandaAplicaciones --> EstrategiaTI[Estrategia de TI (Oferta)]
    EstrategiaTI --> SolucionesTecnologicas[Soluciones Tecnológicas]
    SolucionesTecnologicas --> ImplementacionSI[Implementación de SI]

    style EstrategiaSI fill:#ccf,stroke:#333,stroke-width:2px
    style EstrategiaTI fill:#cfc,stroke:#333,stroke-width:2px
```
*Diagrama: Flujo desde la Estrategia de Negocio hacia la Estrategia de SI (demanda) y Estrategia de TI (oferta).*

---

Siguiente: [6. Planificación de SI/TI a partir de la Estrategia de Negocio](./06_Planificacion_SI_TI_Desde_Estrategia_Negocio.md) 