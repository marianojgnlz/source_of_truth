# 11. Administración de los SI

Este documento describe los diferentes niveles de administración dentro del área de Sistemas y Tecnologías de la Información (SI/TI), asociándolos con roles gerenciales típicos.

```mermaid
mindmap
  root("Administración de los SI")
    ("Introducción" ~colon~ "Niveles de administración en SI/TI, roles gerenciales")
    ("Niveles de Administración en SI/TI")
      ("1. Administración de la Información (Nivel Estratégico)")
        ("Enfoque" ~colon~ "Estratégico")
        ("Responsabilidad" ~colon~ "Políticas info, alineamiento SI/negocio, gobernanza datos, portafolio SI")
        ("Rol Típico" ~colon~ "CIO / Director SI")
        ("Foco" ~colon~ "QUÉ y POR QUÉ de info y sistemas (global)")
      ("2. Administración del Uso de los Sistemas de Información (Nivel Táctico/Gerencial)")
        ("Enfoque" ~colon~ "Táctico / Gerencia media")
        ("Responsabilidad" ~colon~ "Uso eficaz/eficiente SI, gestión proyectos, relación usuarios, gestión demanda")
        ("Rol Típico" ~colon~ "Gerentes SI, Jefes Proyecto, BRMs")
        ("Foco" ~colon~ "CÓMO se usan sistemas y QUIÉN los usa (objetivos deptales/empresa)")
      ("3. Administración de la Tecnología (Nivel Supervisión/Operativo)")
        ("Enfoque" ~colon~ "Supervisión / Gerencia primera línea (operativo)")
        ("Responsabilidad" ~colon~ "Infraestructura (HW, SW base, redes), operación diaria, seguridad técnica, soporte")
        ("Rol Típico" ~colon~ "CTO (si enfocado en tecno), Jefes Operaciones/Soporte, Admins Sistemas/Redes/BD")
        ("Foco" ~colon~ "DISPONIBILIDAD, RENDIMIENTO, SEGURIDAD plataforma tecno")
    ("Diagrama" ~colon~ "Jerarquía y enfoque de los niveles")
    ("Nota" ~colon~ "Títulos y responsabilidades varían, pero funciones deben cubrirse")
```

[< Volver al Índice Principal](./00_Indice_SI_TI.md) | [Anterior: 10. Management de Recursos de IS (Área de Sistemas)](./10_Management_Recursos_IS.md)

La administración dentro del ámbito de SI/TI se puede estructurar en diferentes niveles, cada uno con un enfoque y responsabilidades distintas, alineados con la jerarquía administrativa general de una empresa.

## Niveles de Administración en SI/TI

1.  **Administración de la Información (Nivel Estratégico)**
    *   **Enfoque**: Estratégico.
    *   **Responsabilidad Principal**: Definición de políticas de información, alineamiento de la estrategia de SI/TI con la estrategia de negocio, gobernanza de datos, gestión del portafolio de SI.
    *   **Rol Típico**: **CIO (Chief Information Officer)** o Director de Sistemas de Información.
    *   Se centra en el **QUÉ** y el **POR QUÉ** de la información y los sistemas a nivel global de la empresa.

2.  **Administración del Uso de los Sistemas de Información (Nivel Táctico/Gerencial)**
    *   **Enfoque**: Táctico o de gerencia media.
    *   **Responsabilidad Principal**: Asegurar que los SI se utilicen eficaz y eficientemente para soportar los procesos de negocio, gestión de proyectos de SI, relación con las áreas usuarias, gestión de la demanda de servicios de SI.
    *   **Rol Típico**: Gerentes de SI, Jefes de Proyecto, Gerentes de Desarrollo, Gerentes de Soporte, Business Relationship Managers (BRMs).
    *   Se centra en el **CÓMO** se utilizan los sistemas y **QUIÉN** los utiliza para lograr los objetivos departamentales y de la empresa.

3.  **Administración de la Tecnología (Nivel de Supervisión/Operativo)**
    *   **Enfoque**: Supervisión o gerencia de primera línea (operativo).
    *   **Responsabilidad Principal**: Gestión de la infraestructura tecnológica (hardware, software de base, redes, comunicaciones), operación diaria de los sistemas, seguridad técnica, soporte técnico, mantenimiento de la infraestructura.
    *   **Rol Típico**: **CTO (Chief Technology Officer)** en algunas organizaciones (especialmente si es más enfocado a la tecnología y no tanto a la información estratégica), Jefes de Operaciones de TI, Jefes de Soporte Técnico, Administradores de Sistemas/Redes/Bases de Datos.
    *   Se centra en la **DISPONIBILIDAD**, **RENDIMIENTO** y **SEGURIDAD** de la plataforma tecnológica.

```mermaid
graph TD
    subgraph Niveles de Administración SI/TI
        A[Administración de la Información <br/> (Estratégico - CIO)]
        B[Administración del Uso de los SI <br/> (Táctico - Gerentes SI)]
        C[Administración de la Tecnología <br/> (Operativo - CTO/Jefes Técnicos)]
    end

    EstrategiaNegocio[Estrategia de Negocio] --> A
    A --> B
    B --> C
    C --> InfraestructuraTI[Infraestructura y Operaciones TI]
    B --> ProcesosNegocio[Soporte a Procesos de Negocio]
    A --> GobernanzaDatos[Gobernanza de Datos y Políticas]

    style A fill:#add8e6,stroke:#333,stroke-width:2px
    style B fill:#b0e0e6,stroke:#333,stroke-width:2px
    style C fill:#b0c4de,stroke:#333,stroke-width:2px
```
*Diagrama: Jerarquía y enfoque de los niveles de administración en SI/TI.*

Es importante notar que los títulos exactos (CIO, CTO) y la distribución de responsabilidades pueden variar significativamente entre organizaciones, dependiendo de su tamaño, estructura y cultura. Sin embargo, las funciones descritas en estos tres niveles generalmente necesitan ser cubiertas.

---

Siguiente Tema: [12. Integración de los SI y la Estrategia Empresarial](./12_Integracion_SI_Estrategia_Empresarial.md) 