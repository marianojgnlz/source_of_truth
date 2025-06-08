### Teoria de colas

```mermaid
graph TD
    A[Teoría de Colas] --> B{Componentes};
    B --> B1[Estación de Servicio];
    B1 --> B1a[Servidor (Recurso)];
    B1 --> B1b[Cola de Espera (Trabajos)];
    
    A --> C{Parámetros Temporales};
    C --> C1[Tiempo de Servicio];
    C --> C2[Tiempo de Respuesta];

    A --> D{Tipos de Redes de Colas};
    D --> D1[Redes Abiertas];
    D1 --> D1a[Cargas Transaccionales];
    D --> D2[Redes Cerradas];
    D2 --> D2a[Cargas Interactivas/Batch];

    subgraph "Modelo vs. Realidad"
        direction LR
        M1[Recurso del Sistema] --> R1[Servidor];
        M2[Trabajos (SW)] --> R2[Cola];
    end
```

**Una estación de servicio está compuesta por un servidor y una cola de espera**. El servidor representa al recurso físico del computador, mientras que la cola de espera modela la cola de trabajos que aguardan a utilizar el recurso físico. **Los parámetros temporales más importantes** de una estación de servicio desde el punto de vista del rendimiento son dos: 

* El **tiempo de servicio** es el tiempo que transcurre desde que un trabajo empieza a utilizar el recurso hasta que lo deja libre.  
* El **tiempo de respuesta** es el tiempo de servicio más el tiempo que el trabajo pasa aguardando en la cola de espera.

Cuando se puede atender a más de un trabajo en paralelo, las estaciones de servicio incluyen más de un servidor. Se pueden describir tres tipos de estaciones de servicio:  
![][image123]  
Formalmente podemos definir una red de colas como un grafo dirigido cuyos nodos son las estaciones de servicio. Los arcos entre estos nodos indican las transiciones posibles entre las estaciones. 

Las redes también pueden ser clasificadas según la topología del grafo subyacente.

* **Las redes abiertas** se caracterizan por la existencia de, al menos, una fuente de trabajos y uno o más sumideros que absorben los trabajos que salen del sistema y, así mismo, la posibilidad de encontrar al menos un camino que, a partir de cada nodo, lleve a un sumidero. **Las redes abiertas se emplean para modelar el comportamiento de sistemas que soportan cargas transaccionales**. La productividad de una red abierta es igual a la tasa de entrada al sistema. Los índices son el tiempo de respuesta y el número de trabajos dentro del sistema. En la Figura 4.2 se muestra una red de colas abierta que comprende tres estaciones de servicio, la fuente de trabajos y el sumidero de la red.

![][image124]

* **Las redes cerradas** son redes en las cuales los trabajos ni entran ni salen y, por tanto, su número permanece constante. El flujo de trabajos a través del enlace entre la salida y la entrada define la productividad de la red. En estas redes resulta de gran interés conocer el tiempo de respuesta y la productividad. **Los sistemas con carga de tipo interactivo y con carga por lotes (batch) se modelan mediante redes cerradas.** La Figura 4.3 muestra un ejemplo en donde la estación con infinitos servidores se suele utilizar para representar el tiempo transcurrido entre la finalización de una petición al sistema y el comienzo de una nueva. En caso de que la carga fuera por lotes la estación con infinitos servidores desaparecería del modelo y se uniría la salida con la entrada de esta estación.

![][image125]

⇒ Una estación de servicio puede tener más de un servidor y más de una cola.

Sistema real                                                                 	Modelo

Recurso del sistema (HW)		 →	 servidor

Trabajos (SW) asociados al recurso 	→	 cola

**El análisis intenta deducir los simples índices de prestaciones a partir de parámetros cuantificables del sistema y las relaciones entre esos parámetros.** Las relaciones entre ellos se establecen a través de las Leyes Operacionales / verificables mediante mediciones 