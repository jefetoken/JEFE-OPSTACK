# Progreso en el Desarrollo de Blockchain con el OP STACK de Optimism: El Caso de Knuckles

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/opstack2.jpg">

## 1. Mejoras en Almacenamiento y Desarrollo de la OPCHAIN Knuckles

### **1.1 Desarrollo y Capacidades Mejoradas de la Cadena de Bloques Knuckles con Optimism**

Desarrollo de "Knuckles" ha avanzado significativamente en su capacidad de almacenamiento y operaciones en la red de prueba Sepolia de Optimism. Este progreso se ha registrado mediante la implementación de una blockchain optimism en testnet utilizando el paquete op stack de optimism.io <a href="https://github.com/ethereum-optimism/optimism"> OP STACK </a>  y de un explorador open source que permite darle una amplitud a la visualización de lo que esta sucediendo en la blockchain , como la producción de bloques y transacciones, ampliando la capacidad de procesamiento de solicitudes y mejorando cómo se visualiza el desarrollo de la cadena de bloques “Knuckles” creada con el Op Stack de OPTIMISM completamente OPEN SOURCE.

## **Acciones Clave:**

- **Establecimiento de un Servidor Virtual Privado (VPS) Mejorado:** Equipado con 8GB de RAM y 160GB de almacenamiento SSD, este servidor soporta un explorador de blockchain que facilita la observación de transacciones y confirmaciones de bloques.

- **Optimización de Conexiones API:** Incrementamos las solicitudes computacionales a la API de Alchemy para una mejor integración con la red Sepolia.

- **Reconfiguración de Archivos Críticos:** Se analizaron los archivos de génesis y rollup para la sincronización de la blockchain.

- **Desarrollo del RPC de Knuckles:** Creamos y aplicamos un punto de conexión RPC para permitir el monitoreo de la blockchain.

- **Uso de Herramientas de Código Abierto:** Implementamos Blackscout para mejorar la transparencia y el seguimiento de la blockchain.

Ahora, con el RPC activo y el explorador en funcionamiento, es posible monitorear y almacenar datos de la blockchain de manera efectiva, observando transacciones y confirmaciones de bloques en tiempo real.

## Optimización de Sincronización 

- **Relevancia de la Configuración Inicial:** La correcta configuración de los archivos de génesis y rollup es vital para la eficiencia de despliuege y sincronización de la blockchain. 

## **1. Archivo Crítico Génesis y su Creación:**

- **Fundamento de la Blockchain:** El archivo génesis es esencial porque define el estado inicial de la blockchain. Es el punto de partida que contiene todos los parámetros y configuraciones iniciales. Su correcta creación es crucial para:

  - **Integridad y Seguridad:** Garantiza que la blockchain inicie con una base segura y libre de errores que podrían comprometer la red desde su concepción.
  
  - **Compatibilidad y Continuidad:** Asegura que cualquier evolución o actualización de la red sea compatible con el estado inicial, facilitando futuras integraciones y escalabilidad.

- **Customización y Optimización:** Permite personalizar la blockchain para necesidades específicas, con el OpStack.

## **2. Balances de Sepolia en Faucets para sus Pruebas:**

- **Entorno de Pruebas Realista:** Utilizar Sepolia, una red de prueba en Optimism, para obtener tokens de prueba es vital para:

  - **Gas de Transacciones:** Permite generar transacciones y contratos inteligentes en un entorno que refleja las condiciones de la red principal (mainnet).
  
  - **Desarrollo y Depuración:** Facilita el desarrollo y la depuración de aplicaciones y contratos sin el riesgo de perder valor real, acelerando el ciclo de desarrollo y prueba , pero lo mas importante es que permite de manera meticulosa analizar en tiempo real como funciona cada uno de los componentes de op Stack en funcionamiento , permitiendo medir y optimizar 

- **Accesibilidad:** Los faucets permiten al developer obtener recurso para poner en prueba un entorno antes de despliegue en una mainnet

## **3. Modificación de Intervalos de Tiempo en Proposer y Batcher:**

- **Eficiencia Operativa:** Ajustar los intervalos de tiempo para el proposer (el que propone los bloques) y el batcher (el que agrupa las transacciones en bloques) es crítico para:

  - **Optimización de la Red:** Mejora la velocidad y eficiencia con la que se procesan y confirman las transacciones, afectando directamente la experiencia del usuario y la capacidad de la red.

  - **Reducción de Latencia:** Minimizar el tiempo entre la proposición y la inclusión de bloques puede reducir la latencia, un factor clave en la usabilidad de aplicaciones descentralizadas (dApps).

- **Adaptabilidad:** Permite que la blockchain se adapte a diferentes cargas de trabajo y condiciones de red, asegurando que la blockchain con OpStack pueda escalar y responder a demandas cambiantes de manera eficiente.



## **Limitantes del Archivo Crítico Génesis y su Creación:**

- **Complejidad de Configuración:** La creación del archivo génesis requiere una comprensión profunda de la configuración de la blockchain. Un error en este archivo puede llevar a vulnerabilidades de seguridad o a una funcionalidad defectuosa desde el inicio.

- **Inmutabilidad Inicial:** Una vez que el archivo génesis está configurado y la blockchain se lanza, es preferible no alterar ni cambiar aspectos fundamentales definidos en este archivo .

- **Compatibilidad Futura:** Al definir el estado inicial, el archivo génesis debe anticipar futuras actualizaciones y escalabilidad. 

- **Verificación y Auditoría:** El archivo génesis debe ser exhaustivamente revisado y auditado para asegurar que no contiene errores o configuraciones que podrían ser explotadas. 

- **Interoperabilidad:** Si se planea que la nueva blockchain interactúe con otras redes o sistemas, el archivo génesis debe ser diseñado teniendo en cuenta estas interacciones.

Estas limitaciones subrayan la importancia de una planificación meticulosa y una ejecución precisa en la creación del archivo génesis, ya que este documento no solo define el inicio de la blockchain sino que también establece las bases para su evolución y éxito a largo plazo.

## **2. Balances de Sepolia en Faucets para pruebas:**

- **Acceso a Faucets:** Los faucets como el de QuickNode o el de Superchain Faucet,  proporcionan tokens de prueba para la red Sepolia de Optimism. Estos faucets están diseñados para distribuir ETH de prueba sin costo, solo con un periodo de espera por cada 24 horas.

- **Configuración de Wallet:** Siempre es importante verificar en todo despliegue que el uso de las wallets (como MetaMask) estén super bien configuradas para interactuar con la red Sepolia de Optimism. Esto implica añadir la red Sepolia a su wallet con los parámetros correctos de la cadena (Chain ID, RPC URL, etc.). Asegurar la propia configuración inicial de variables de entorno siempre en cuenta las direcciones de ERC-20 de Admin, Proposer, Batcher, Sequencer, el monitoreo constante de balance es importante . 

- **Solicitud de Tokens:** Una simple solicitud desde su wallet al faucet elegido y asi de fácil puede uno solicitear tokens y continuar con el despliuegue de la blockchain.

## **3. Modificación de Intervalos de Tiempo en Proposer y Batcher:**

La modificación en componentes de sincronización ha sido amplio y de importancia para lograr el obetivo de tener una buena sincronización , esto ha implicado generar entornos de pruebas con variables alteradas en la configuración de: 

- **Proposer:** El proposer es responsable de proponer nuevos bloques. Para ajustar los intervalos:
  - **Configuración del Nodo:** Mediante este se accede a la configuración del nodo Optimism. Esto generalmente se hace a través de archivos de configuración nuestro objetivo es proponer un nuevo parámetro como `--proposeInterval` que defina cuánto tiempo espera un proposer antes de proponer un nuevo bloque adaptado mas a las necesidades de Knuckles y su integración de caso de uso. El cual puede variar de quien lo despliega.

- **Batcher:** Mediante el crucial funcionamiento el batcher continuara agrupando las transacciones

  - **Intervalo de Batching:** Similar al proposer, se experimento con otro parámetro muy interesante como lo es el `--batchSubmitInterval` en la configuración del nodo del el código fuente de OpStack de OPTIMISM
. Este intervalo determina con qué frecuencia el batcher envía lotes de transacciones a la red principal.

  - **Optimización para Eficiencia:** Ajustar este intervalo puede optimizar el costo de gas en L1 versus la latencia de las transacciones en L2 es un experimento activo por lo que un intervalo más largo podría reducir costos al enviar más transacciones por lote, pero aumentaría la latencia para los usuarios de L2.

Ambos procesos requieren un acceso directo a la configuración del software de la blockchain o al código fuente si es open source, como es el caso con Optimism. La modificación de estos intervalos debe hacerse con cuidado, considerando el balance entre eficiencia, costo, y experiencia del usuario en la red.
Acceso a Knuckels RPC

KNUCKLES OPCHAIN TESTNET RPC : http://51.195.202.219:8545 <br>
idchain: 42069 <br>
Blockchain inspector-explorer: https://explorer.jefetoken.com || http://217.182.72.132:3001/ <br>
https://github.com/jefetoken/JEFE-OPSTACK
<br>
<br>
En resumen, estos aspectos son fundamentales para la creación de una blockchain efectiva y eficiente usando el OpStack de Optimism. Cada uno juega un rol vital en asegurar que la blockchain no solo funcione correctamente desde su inicio sino que también sea capaz de adaptarse y optimizarse para futuras necesidades y desafíos.



## **Conclusión:** 

El proyecto Knuckles, utilizando la tecnología de Optimism especificamente el Op Stack, ha demostrado ser un terreno fértil para aplicaciones en blockchain y su caso  de uso como implementacion educativa, facilitando el analisis y estudio especialmente en cuanto a almacenamiento y eficiencia de red. No obstante, los retos en la sincronización subrayan la importancia de una optimización continua y la necesidad de ajustes precisos en la configuración de la blockchain para su óptimo funcionamiento. . A pesar de los desafíos presentados, particularmente en la sincronización y configuración inicial, este proyecto ilustra el potencial de las soluciones de segunda capa para superar las limitaciones de la blockchain de Ethereum. La experiencia adquirida con Knuckles no solo allana el camino para futuras mejoras en su propia red sino que también proporciona valiosas lecciones para la comunidad blockchain en general.
