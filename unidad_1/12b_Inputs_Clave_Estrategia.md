# 12.2. Entradas (Inputs) Clave para la Estrategia de SI/TI

Este documento detalla las entradas fundamentales que alimentan el proceso de formulación de la estrategia de Sistemas y Tecnologías de la Información (SI/TI), abarcando el entorno externo, el entorno interno de la empresa, y los recursos y capacidades de SI/TI existentes.

```mermaid
mindmap
  root("Inputs Clave para Estrategia SI/TI")
    ("1. Entorno Empresarial Externo")
      ("Nuevas Tecnologías")
        ("Innovaciones emergentes")
        ("Riesgo y curva de aprendizaje")
      ("Utilización Tecnología por Otros")
        ("Empleo por otros en misma industria (competidores, socios)")
        ("Uso SI/TI en otras industrias (fuente de ideas)")
    ("2. Entorno Interno de la Empresa")
      ("Análisis necesidades info y sistemas (qué hace, cómo, organización, dirección)")
      ("Misión y Objetivos Empresa")
      ("Actividades Empresa (procesos clave)")
      ("Fortalezas y Debilidades (FODA interno)")
      ("Estructura Organizativa y Estilo Dirección")
    ("3. Recursos SI y de Información Empresa (Situación Actual SI/TI)")
      ("Puntos fuertes/débiles sistemas existentes (cartera aplicaciones actual)")
      ("Evitar fracaso nuevos proyectos por cimientos inadecuados")
    ("4. Ventajas y Recursos de los SI/TI")
      ("Evaluar si capacidad y tecnología actuales son adecuadas para futuro")
      ("Auditoría tecnología (HW, SW) Y evaluación equipo humano (habilidades, dirección, métodos)")
    ("Diagrama Inputs")
    ("Conclusión" ~colon~ "Análisis conjunto y equilibrado para estrategia SI/TI robusta y preparada para futuro")
```

[< Volver a Integración de SI y Estrategia Empresarial](./12_Integracion_SI_Estrategia_Empresarial.md) | [< Volver al Índice Principal](./00_Indice_SI_TI.md)

Para desarrollar una estrategia de SI/TI robusta y alineada, es crucial analizar una serie de inputs clave:

## 1. El Entorno Empresarial Externo

Consiste en una evaluación de las fuerzas que afectan a la industria en que opera la empresa.
Una organización necesita comprender dos aspectos del entorno externo de los SI/TI:

*   **Nuevas Tecnologías**: Es fundamental estar al tanto de las innovaciones tecnológicas emergentes. Además de beneficios, todas las nuevas tecnologías conllevan algún **riesgo** y una **curva de aprendizaje** para la empresa.
*   **La Utilización de la Tecnología por Otros**: Una organización necesita conocer:
    *   La forma en que la tecnología de la información es **empleada por otros dentro de la misma industria** (competidores, socios): con qué objetivo y con qué resultados.
    *   El uso de los SI/TI en **otras industrias**, ya que puede proporcionar una fuente de buenas ideas que se pueden trasplantar.

## 2. El Entorno Interno de la Empresa

Consiste en un análisis de las necesidades de información y de sistemas sobre la base de lo que la empresa hace, cómo lo hace, y cómo está organizada y dirigida. Estará relacionado con:

*   **Misión y Objetivos de la Empresa**: La razón de ser de la empresa y las metas que persigue.
*   **Las Actividades de la Empresa**: Describir los principales procesos de la empresa que le permiten ofrecer productos y servicios a sus clientes, así como lo que es preciso hacer para controlar y desarrollar el negocio.
*   **Las Fortalezas y Debilidades (Análisis FODA interno)**: Capacidades distintivas y áreas de mejora de la organización.
*   **Estructura Organizativa y Estilo de Dirección**: Es importante comprender cómo funciona la organización y cómo se toman las decisiones.

## 3. Los Recursos de Sistemas y de Información de la Empresa (Situación Actual de SI/TI)

Es preciso comprender totalmente los puntos fuertes y débiles de los sistemas existentes en la empresa (la **cartera de aplicaciones actuales**, ver [Análisis de la Cartera de Aplicaciones](./12c_Cartera_Aplicaciones.md)) antes de emprender nuevos desarrollos. De otra manera, los nuevos proyectos podrían fracasar a causa de cimientos inadecuados.

## 4. Las Ventajas y los Recursos de los SI/TI

Es necesario determinar si la capacidad y la tecnología actuales de la organización son adecuadas para las necesidades futuras. Esto no es solamente una auditoría de la tecnología disponible (hardware, software, etc.), sino también una **evaluación del equipo humano**, de sus habilidades, de la forma en que son dirigidos y de los métodos empleados para desarrollar y soportar los sistemas y la tecnología de base.

```mermaid
graph TD
    subgraph Inputs para Estrategia SI/TI
        A[Entorno Empresarial Externo]
        B[Entorno Interno de la Empresa]
        C[Recursos SI/TI Existentes (Cartera Aplicaciones)]
        D[Ventajas y Capacidades Actuales en SI/TI (Tecnología y Equipo Humano)]
    end

    A --> EstrategiaSITI[Formulación Estrategia SI/TI]
    B --> EstrategiaSITI
    C --> EstrategiaSITI
    D --> EstrategiaSITI

    A_sub1[Nuevas Tecnologías]
    A_sub2[Uso de TI por Otros (Industria y Externos)]
    B_sub1[Misión y Objetivos]
    B_sub2[Actividades Clave]
    B_sub3[Fortalezas y Debilidades]
    B_sub4[Estructura y Estilo Dirección]

    A --> A_sub1
    A --> A_sub2
    B --> B_sub1
    B --> B_sub2
    B --> B_sub3
    B --> B_sub4
```
*Diagrama: Principales inputs para la formulación de la estrategia de SI/TI.*

El análisis conjunto y equilibrado de estas entradas permite definir una estrategia de SI/TI que no solo responda a las necesidades actuales, sino que también prepare a la organización para el futuro.

---

Siguiente Subtema: [12.3. Análisis de la Cartera de Aplicaciones](./12c_Cartera_Aplicaciones.md) 