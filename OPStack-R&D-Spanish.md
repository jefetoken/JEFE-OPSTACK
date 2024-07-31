INVESTIGACION & DESARROLLO
OPTIMISM STACK [OP STACK]
www.jefetoken.com

#OPStack
www.optimism.io

# INVESTIGACION & DESARROLLO
# OPTIMISM STACK [OP STACK]

## Marco Referencial
### 1. Resumen 
#### 1.1 Capacidades de Sincronización de la Cadena.
Mediante el desarrollo de JEFE KNUCKLES basado en los  TUTORIALES DE OP STACK  se realizaron pruebas de operación en la test net con la finalidad de investigar y analizar la gestión de sincronización de la cadena principal con la capa de optimización por medio de OPTIMISM STACK. Y utilizando las actividades y productos digitales en web3 que brinda JEFE TOKEN se realizaran ejemplos de casos de uso de almacenaje en la blockchain de OPTIMISM.

Cronograma

Semana 1-2 Mayo: Configuración del entorno de pruebas y despliegue inicial de contratos.
Semana 3-4 Mayo: Ejecución de pruebas, recopilación de datos, ejemplos de demanda.
Semana 1-2 junio: Análisis de datos y redacción del informe preliminar.
Semana 3-4 junio: Revisión y análisis final de los resultados.
Semana 1-2 Julio: Finalización del informe y análisis de conclusiones.
Semana 3-4 Julio: Publicación. 


### 2. Planteamiento del tema
#### 2.1. Justificación   
En un constante y creciente ecosistema web3 es necesario seguir creando oportunidades que brinden a los usuarios casos de uso que se adapten a sus necesidades, por lo cual es vital conocer y analizar mediante la implementación de una cadena de bloques el impacto que está tiene mediante el uso de Optimism Stack (Op Stack).

#### 2.2. Delimitación del tema
Se midió el alcance que brinda la blockchain de OPTIMISM aterrizando del concepto a la práctica algunos temas principales de implementación para brindar a los usuarios y proyectos que quieran desarrollar en la cadena de bloques cuáles son las capacidades de almacenamiento para contratos inteligentes, datos almacenados, peticiones y transacciones. Esto con un enfoque general independientemente del tipo de información almacenada, así como con enfoques específicos dependiendo casos de uso para permitir a los usuarios comprender y planificar mejor sus proyectos.  
Se medirá la capacidad de procesamiento de transacciones y peticiones en Optimism. latencia y rendimiento del sistema bajo diferentes cargas de trabajo, tanto como bajo condiciones mínimas de configuración así como implementando un servidor privado virtual con las siguientes especificaciones: 16gb / 80SSD / 4 cores.

Se realizó la recopilación de Datos y Análisis con los siguientes enfoques:
•	Medición del tiempo de sincronización de bloques entre la cadena principal y Optimism.
•	Registro de la capacidad de almacenamiento utilizada por los contratos y transacciones.
•	Evaluación del rendimiento de la red en términos de tiempos de respuesta y carga máxima sostenible.
•	Comparación de los resultados obtenidos con los sistemas basados en capa única como Ethereum.
Por último se plasmaran las conclusiones obtenidas sobre la eficacia y eficiencia de Optimism Stack en relación con la escalabilidad y el rendimiento.


### 3. Hipótesis
Tomando como referencia las necesidades de JEFE TOKEN de plasmar en la blockchain la interacción de los usuarios de una comunidad digital con los distintos productos web3  y de a su vez recopilar información web2 de usuarios y actividades, se plantea la necesidad de crear una blockchain propia por medio de OPTIMISM STACK.

### 4. Objetivos
#### 4.1 Objetivos generales
Crear ejemplos tangibles basados en la demanda de almacenaje de datos para la comprensión de la infraestructura de código abierto que provee optimism.

#### 4.2 Objetivos particulares
- Sincronizar una cadena de bloques mediante el Op Stack
- Configurar un entorno de pruebas
- Despliegue de contratos y recursos específicos como tablas de contenido de datos CSV  y NFTs de almacenaje de usuarios, a lo largo de periodos de votación sobre actividades web2 y web3.
- Medir y recopilar los datos de la blockchain, comparar los datos obtenidos contra la demanda de almacenaje dependiendo los casos de uso. 

### 5. Marco teórico
#### 5.1. Optimism Stack Blockchain web3 
Repositorio de github que permite la construcción de una blockchain de manera que este pueda ser colocado en línea en un servidor privado virtual, capaz de desplegar los contratos necesarios para la intercomunicación de información en la red.

#### Optimism Docs <a href="https://docs.optimism.io/">

#### 5.2. Blockchain On Chain & OFF Chain   
El aumento de la cantidad de información producida por todas las interacciones que se realizan en el mundo digital como en el mundo fuera del internet nos lleva al punto de poder considerar importante el almacenarla de manera descentralizada para que su disponibilidad no dependa de tan solo un servidor si no de toda una cadena de bloques interconectada por cientos de miles de computadores alrededor del mundo.

### 6. Configuración del Entorno de Pruebas
El paso de configuración del entorno es vital para poder realizar la creación del l2 rollup de un OP chain basado en OP STACK, en grandes rasgos los pasos principales son los siguientes:
- Configuración de servidor privado virtual de Linux Debian12.
- Actualización de fuentes de origen para dependencias de sistema.
- Instalación de actualizaciones de dependencias de sistema operativo.
- Correr herramienta de JEFE KNUCKLES o seguir el tutorial de OPTIMISM DOCS.

### 6.1 Recursos Necesarios
- Vps Virtual 16gb 
- Nodo de RPC (Remote Procedure Call): Utiliza comandos RPC para obtener detalles sobre el estado actual de la red, incluyendo información sobre bloques, transacciones y contratos inteligentes desplegados.

### 7. Herramienta de Desarrollo 
#### 7.1. KOSOTL (KNOCKLES OPEN SOURCE OPSTACK TOOL) 
KOSOTL es una herramienta open source desarrollada por JEFETOKEN con la finalidad de brindar un índice de referencia para generar los primeros pasos de la creación de OP CHAINS [ Blockchains creadas con Op Stack] . Esta herramienta le facilitará a usuarios y desarrolladores la experiencia del despliegue de una blockchain de capa 2 ( L2 ) usando el Op Stack . 

#### https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-LAB-OPSTACK/knuckles-KOSOTL.py

#### 7.2 Funciones de Consulta como optimism etherscan 
Las funciones de consulta en blockchain permiten acceder a información de manera rápida y eficiente, algunas de estas son: Búsqueda de transacciones, consulta de direcciones, seguimiento de tokens,gas tracker, exploración de bloques y rollups, transacciones entre Capa 1 y 2, entre otras.

### 8. Eventos y Logs:
Para almacenar datos de una dApp en un NFT utilizando codificación base64 en una cadena Optimism (OP chain), se puede seguir un enfoque eficiente que considere tanto las limitaciones de almacenamiento de los NFT como las capacidades de la blockchain
Los eventos y logs en el OP Stack son cruciales para la auditoría y el monitoreo de la red, así como para poder tomar métricas o análisis de los datos:
1.	Eventos de Contratos Inteligentes:
	- TransactionDeposited: Emitido cuando una transacción es depositada desde L1 a L2.
	- BatchSubmitted: Emitido cuando un lote de transacciones es enviado a L1.
2.	Logs de Sistema:
	- Métricas del OP Node: Logs que indican la sincronización del nodo, el estado de las conexiones y errores potenciales.
	- Batch Submitter Logs: Información sobre la compresión y envío de lotes de transacciones.

### 9.	Capacidades de Almacenaje
#### 9.1 Métodos de Almacenamiento y Funciones para Base64 en Blockchain vs Bases de Datos Tradicionales
Métodos de Almacenamiento
1.	Blockchain (Optimism OP Chain)
	- Almacenamiento en NFT: Utilizar NFT para almacenar datos codificados en base64 en los metadatos.
	- Contratos Inteligentes: Implementar funciones en contratos inteligentes para guardar y recuperar cadenas de texto.
	- IPFS (InterPlanetary File System): Almacenar los datos en IPFS y guardar el hash en la blockchain, permitiendo una recuperación descentralizada de los datos.
	- BLOB (Binary Large Object): Usar campos BLOB para almacenar grandes volúmenes de datos binarios.

2.	Bases de Datos Tradicionales (MySQL)
	- Tablas y Columnas: Almacenar los datos directamente en tablas y columnas de la base de datos.
	- Archivos en el Servidor: Guardar los datos en archivos en el servidor y almacenar las rutas de acceso en la base de datos.

### 10. Costo de creación y almacenamiento de NFT en la blockchain
Para conocer el costo asociado con el almacenamiento de datos en Optimism. Se deben considerar tarifas de gas, precios de transacción y cualquier tarifa adicional por el uso prolongado de almacenamiento.

### 11. Estructura de Datos de los NFTs
La estructura de datos de un NFT incluye el identificador del token, los metadatos descriptivos, el propietario actual y la URI de los metadatos, con funciones y eventos específicos para gestionar la propiedad y las transferencias del token. 
De los cuales los atributos que definirán el espacio de memoria que necesita un NFT son
- URI de los Metadatos
- Archivos Multimedia Referenciados
- Metadatos JSON

### 12. Rendimiento y Latencia
Considerar el rendimiento de la red y la latencia asociada con el almacenamiento y recuperación de datos de NFTs en Optimism puede influir en la experiencia del usuario y la viabilidad de aplicaciones que manejan grandes volúmenes de NFTs.

### 13. Monitoreo y Análisis Continuo
El monitoreo y análisis de datos es un punto importante por considerar si se está planeando correr un contrato propio en la Testnet, independientemente del caso de uso o enfoque que maneje esto permitirá identificar problemas de rendimiento, optimizar el uso de recursos y mejorar la experiencia general de usuario.

13.1 Caso de uso, monitoreo y análisis de atributos
JEFE TOKEN mediante su DAPP JEFE COMPASS genera la exposición de una revista digital con distintos temas que hacen referencia a las actividades tanto web 2 (deportes, gaming, exposiciones artísticas, etc) como web 3 (contenido artístico digital y media). 
Se utilizará como ejemplo práctico para medir la demanda de almacenamiento y costos de operación de un NFT generado del contenido grafico de la primer edición de la revista digital de JEFE TOKEN.

Paso 1. Monitoreo de información
<a href="https://optimistic.etherscan.io/token/0x4e13201ED7a029BC38A34A9b377F397D0D98a3BC">JEFE COMPASS E-MAGAZINE I NFT Contract: </a>
Opmainnet 
•	Visita Etherscan para Optimism: https://optimism.etherscan.io/  
•	Busca por Dirección de Contrato
•	Identifica la información principal
•	Registra y analiza los datos

Paso 2. Evaluar la Demanda de Almacenamiento de tus NFTs
Calcula el tamaño promedio de cada NFT que planeas almacenar en tu cadena. Esto incluye no solo el tamaño del archivo principal del NFT (como una imagen o un archivo de audio), sino también los metadatos asociados que se almacenarán en la blockchain.
Paso 3: Estimar el Volumen de NFTs
Estima cuántos NFTs planeas desplegar en tu aplicación. Multiplica el tamaño promedio de cada NFT por el número total de NFTs para obtener una estimación del volumen total de datos que necesitarás almacenar.
Paso 4: Considerar el Crecimiento Futuro:
Proyecta cómo podría crecer la demanda de almacenamiento a medida que tu aplicación escala y atrae más usuarios. Esto te ayudará a anticipar necesidades futuras y a planificar en consecuencia.
Paso 5: Comparar Capacidades con Demanda
Compara el espacio de almacenamiento actualmente utilizado por tu cadena en Optimism con la estimación de la demanda de almacenamiento para tus NFTs.
Asegúrate de que la capacidad de almacenamiento actual de tu cadena en Optimism sea suficiente para manejar la carga proyectada de NFTs y otros datos.


### 14. Congestión en la Blockchain
La congestión de la blockchain es otro punto a considerar que repercute directamente en el costo de implementación de una blockchain ya que genera los siguientes criterios:
- Aumento en las fees de transacción debido a que las transacciones superan la capacidad de procesamiento de la blockchain. De igual manera en una red congestionada las transacciones pagadas con tarifas más altas tienen prioridad lo que genera una competencia por el espacio en bloques.
- Incremento en costos de ejecución ya que existe una mayor carga computacional lo que ocasiona mayor consumo de gas y competencia por recursos computacionales.
- Retrasos en transacciones debido al tiempo de confirmación fuera de sincronización lo que genera costos extras para acelerar el procesamiento de las transacciones.
- Impacto en la experiencia del usuario, la escalabilidad y sostenibilidad de los proyectos.

### 15. Presupuesto y Financiamiento de una Blockchain Opstack

CONCEPTO      	COSTO
VPS-Desarrollo	45 usd
RPC NODO	      25usd
ETH SEPHOLIA 	~10 Eth en Testnet 
 	 
TOTAL	70 USD / Mes + Nodo testnet (Basado en Unidades de Computo) 

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/apikeycosts.png"/> 

La información mostrada es en términos de Sepolia Testnet y los valores deben ser considerados aproximados en un despliegue de producción basado en la carga de información que el proyecto proyecta tener. 


### 16. Accesibilidad de la Información: Descentralizada vs Centralizada


Es súper importante la investigación e integración de la tecnología del blockchain a aplicaciones cotidianas o web2 genera los siguientes puntos en cuanto al acceso a la información: 
1.	Descentralizada (Blockchain)
	- Ventajas:
		+ Inmutabilidad: Los datos no pueden ser alterados una vez registrados.
		+ Transparencia: Todos los registros son públicos y verificables.
		+ Seguridad: Alto nivel de seguridad contra manipulaciones y ataques.
	- Desventajas:
		+ Costos de Transacción: Costos de gas asociados con la escritura y lectura de datos.
		+ Limitaciones de Tamaño: Restricciones en la cantidad de datos que pueden almacenarse directamente en la cadena.

2.	Centralizada (MySQL)
	- Ventajas:
		+ Flexibilidad y Escalabilidad: Fácil de ajustar y escalar según las necesidades.
		+ Bajo Costo: Menores costos operativos en comparación con la blockchain.
		+ Alta Velocidad: Transacciones rápidas y eficientes.
	- Desventajas:
		+ Riesgo de Manipulación: Mayor vulnerabilidad a la manipulación de datos.
		+ Dependencia de Confianza: Requiere confiar en una entidad central para la integridad de los datos.

### 17. Ejemplo Comparativo: OP Chain con Rollups en L2 vs MySQL
- Caso de Uso en Blockchain (OP Chain con Rollups en L2):
	- Aplicaciones: Registro de propiedades, certificados digitales, activos digitales (NFTs).
	- Ventajas: Seguridad, transparencia, y resistencia a censura.
	- Desventajas: Costos elevados de gas y limitaciones de almacenamiento.
- Caso de Uso en MySQL:
	- Aplicaciones: Sistemas de gestión de contenido, aplicaciones empresariales internas, análisis de datos.
	- Ventajas: Bajo costo, alta eficiencia, y facilidad de gestión.
	- Desventajas: Centralización y vulnerabilidad a manipulaciones.

17.1 Comparación de Almacenamiento
Para la comparación en tu investigación sobre cuánto puedes almacenar, considera los siguientes factores:
1.	Tamaño Máximo de los Metadatos del NFT:
o	Las plataformas pueden tener límites en el tamaño de los metadatos. Por ejemplo, en Ethereum, los datos deben ser menores de 24 kB por transacción para evitar problemas de gas.
2.	Costo de Almacenamiento:
o	El almacenamiento en una blockchain es costoso en términos de gas. Optimism, siendo una solución de escalado de capa 2, reduce estos costos, pero es importante calcular el costo exacto basado en la cantidad de datos.
3.	Eficiencia de Codificación Base64:
o	La codificación base64 aumenta el tamaño de los datos en aproximadamente un 33%. Por lo tanto, los 100 kB de datos originales se convertirán en aproximadamente 133 kB en base64.


JEFE COMPASS contiene +1600 Usuarios activos realizando votaciones de deportes almacenando 1,218,303 bytes<br><br>
JEFE GREEN mediciones mediante sensores off chain que apoyan la reforestación  almacenando 171,000 bytes<br><br>
JEFE REWARDS recompensas por la participación e información compartida entre la comunidad almacenando + 114,104 bytes<br><br>
Data creada por cada 30 dias de la semana.

Si tienes 100 kB de datos:
		+ Tamaño en base64: 100 kB * 1.33 = 133 kB
		+	Número de NFT necesarios: Si cada NFT puede almacenar 24 kB, necesitarás al menos 6 NFT (133 kB / 24 kB ≈ 6).
Escritura de Batch Data en OP Stack
La escritura de datos en lotes (batch data) en el OP Stack se realiza de la siguiente manera:
		+ Compresión de Datos:
 Los lotes de transacciones son agrupados en canales y comprimidos para minimizar el uso de gas al publicarlos en L1.
		+ Publicación en L1:
 Los datos comprimidos son enviados a través del BatchInbox en la cadena L1 de Ethereum, asegurando la integridad y el orden de las transacciones.
		+ Validación y Desafíos:

Comparativa de Costos de Almacenamiento

Blockchain (OP Chain)
		+ Costos: Los costos de gas varían según el tamaño del lote y la congestión de la red. Almacenamiento directo en la cadena puede ser costoso.
		+ Ejemplo: Un lote de transacciones que ocupa 24 kB podría costar varios dólares en tarifas de gas dependiendo del estado de la red Ethereum.
Bases de Datos Tradicionales (MySQL)
		+ Costos: Relativamente bajos, consistentes en costos de hardware y mantenimiento del servidor.
		+ Ejemplo: Almacenar 1 GB de datos podría costar unos pocos dólares mensuales en términos de infraestructura y almacenamiento.


### Conclusión 
La elección entre blockchain y bases de datos tradicionales depende del caso de uso específico, en el caso de JEFE TOKEN la producción de información de actividades web3 , la blockchain de testnet por nombre Knuckles permite llevar al practica la implementación del OPStack, comprender sus capacidades y poder tener un índice de referencia para futuras blockchains identificando cuales son ideales para aplicaciones que requieren alta seguridad, transparencia y resistencia a la manipulación o en su caso poder integrar las bases de datos tradicionales que  son más adecuadas para aplicaciones que requieren eficiencia, bajos costos y flexibilidad en la gestión de datos . 
Para implementar y gestionar eficientemente una solución hibrida basada en blockchain con el OP Stack, es crucial utilizar las herramientas de instrumentación disponibles, entender los eventos y logs del sistema, y optimizar el almacenamiento de datos en lotes criptográficos en forma de NFT o Contratos inteligentes  para maximizar la eficiencia y minimizar los costos.
Almacenar un dump SQL en un NFT en una OP chain es factible, pero debe manejarse con cuidado debido a las limitaciones de tamaño y costo. Fragmentar los datos y optimizar el almacenamiento es clave para una implementación eficiente. Para la comparación, analiza el costo y la eficiencia en términos de tamaño de datos y costos de gas, considerando la codificación base64 y las capacidades de la blockchain de Optimism.
El OP Stack ha avanzado significativamente en la mejora de la escalabilidad y eficiencia de Ethereum, pero todavía enfrenta desafíos en términos de costos de gas, límites de almacenamiento y tiempos de confirmación. Las mejoras propuestas, como la implementación de EIP-4844, la integración con soluciones de almacenamiento descentralizado y la optimización de pruebas de fraude, pueden abordar estos desafíos y llevar a Optimism hacia una adopción más amplia y eficiente.
Es útil la implementación de una blockchain propia cuando sea necesario tener un enfoque descentralizado, con seguridad, transparencia y verificabilidad.

Adjuntos 






<a href="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/deploy-config/bedrock-config.json">Knuckles Testnet Sepolia Config Bedrock Addresses Knuckles Config Bedrock Addresses  </a>

 <a href="https://sepolia-optimism.etherscan.io/address/0x467d8E8764ca8e4101F74F35cd1147d932EeB1fF">Admin Sepolia Knuckles Address </a>

<a href="https://sepolia-optimism.etherscan.io/address/0x01F092c719CfA89B1095F524DC1b0325fC652Fa9 ">Proposer Sepolia Knuckles Address  </a>

 <a href="https://sepolia-optimism.etherscan.io/address/0x1F1a029BA54513981e4AB05EfF4383647AeB76fF">Batcher Sepolia Knuckles Address </a>

<br>

Pruebas y testing the Knuckles usndo nodo de Alchemy , request, transacciones, Opchain en Sepolia 

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/knuckles2.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/knuckles3.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/knuckles4.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/knuckles5.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/knuckles6.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/knuckles7.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/request%20june.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/requestalchemy.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/requestgraph.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/requestgraph2.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/requestgraph3.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/requesthealthknuckles1.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/requestjuly.png"/>

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/requests.png"/>

Knuckles Running Testnet Sepolia

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/payload.png"/>
