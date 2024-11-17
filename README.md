# Ciencia-de-datos.-Taller-2

El objetivo de este taller es aplicar técnicas de machine learning, las cuales permita descubrir insights, sugerir accionables al negocio y calcular el valor ganado.

###### Contexto del negocio - Apoyo a un Supermercado Inteligente

El concepto de supermercado inteligente está transformando la manera en que interactuamos con los entornos de retail, combinando la inteligencia artificial, la automatización y la ciencia de datos para ofrecer una experiencia de compra más eficiente, personalizada y sin fricciones. Estos supermercados están diseñados para mejorar todos los aspectos del proceso de compra, desde la entrada del cliente hasta la salida, utilizando tecnologías avanzadas para automatizar tareas, gestionar inventarios en tiempo real y analizar el comportamiento del consumidor.

Un nuevo supermercado inteligente, ha implementado tecnologías avanzadas como sensores y cámaras. Para iniciar la automatización de procesos, ahora necesita aprovechar mejor los datos generados a diario para tomar decisiones más informadas y eficaces.

El supermercado requiere el desarrollo de un sistema de automatización que permita a los clientes tomar productos y salir sin pasar por caja, mientras las cámaras y sensores registran automáticamente los artículos seleccionados.


**Tabla de Contenido**
* [Estratégia de Análisis](#estrategia-de-analisis)
* [Conclusiones](#conclusiones)
* [Recomendaciones](#recomendaciones)
* [Instrucciones de Ejecución](#instrucciones-de-ejecucion)
* [Autores](#autores)


#### Estratégia de Análisis

Mediante el uso de modelos de Machine Learning y en conjunto con técnicas de preparación de datos, se realiza la construcción de un modelo que identifique los productos tomados por los clientes, y se argumenta el valor generado al supermercado.

Para el desarrollo de la solución se prueban dos modelos de Machine Learning, Convolutional Neural Network (CNN) y MobileNetV2 como modelo basado en Transfer Learning utilizando imageNet de dataset.

Para el entrenamiento del modelo se utiliza el conjunto de imágenes de train, para seleccionar el modelo con mejores resultados se utiliza el conjunto de imágenes de test y, finalmente, para el análisis de los resultados del modelo seleccionado se utiliza el conjunto de imágenes de val. 

#### Conclusiones

1.	El modelo de Transfer Learning superó significativamente al modelo CNN en todas las métricas clave: accuracy, precision, recall, y F1 Score.

2.	La precisión del 64.53% del modelo de Transfer Learning muestra que aún hay un margen significativo de optimización, especialmente en clases con menor frecuencia.

3.	El modelo automatiza el registro de productos, reduciendo el tiempo de procesamiento en un 53.78% en comparación con el método manual, mejorando el flujo de clientes y reduciendo los cuellos de botella.

4.	Los productos en las categorías de vegetales tuvieron una mejor clasificación en comparación con las categorías de frutas y paquetes. 

5.	Productos como zanahorias, lechuga, banano, aguacate, pepino, berenjenas, tomates y la leche de la marca Gran Ecological obtuvieron las mejores predicciones, alcanzando un 100% en algunas de ellas.

6.	Fue complejo diferenciar productos como papa, jengibre y champiñones, debido a su similitud en color y forma, lo que resultó en un bajo desempeño en estas categorías.

7.	A pesar de los costos asociados a los errores de clasificación, el modelo sigue siendo rentable, generando un ROI positivo del 386.67% y alcanzando el punto de equilibrio a los 2 meses de implementación.

#### Recomendaciones

Se recomienda optimizar el modelo de Transfer Learning entrenándolo con imágenes individuales y ampliando el dataset para mejorar la precisión en categorías visualmente similares, como los tubérculos. Configurarlo con 15 épocas asegura un mejor desempeño en comparación con 10 épocas, y se sugiere aplicar ajuste fino en las capas superiores de MobileNetV2 para incrementar la precisión. Además, implementar un sistema de revisión manual para productos con baja confianza en la predicción ayudará a reducir los costos asociados a errores en inventario.
Antes de una implementación total, se aconseja realizar un piloto en un entorno controlado, asegurando que el modelo opere adecuadamente bajo las condiciones reales del supermercado. Monitorear continuamente el desempeño y recalcular el ROI permitirá ajustar costos de mantenimiento y evaluar la sostenibilidad del sistema, maximizando así su impacto operativo y financiero.
Adicionalmente, una vez implementado el modelo, se recomienda entrenarlo regularmente ya que en los supermercados hay una rotación considerable de productos, así como cambios en la presentación. 

#### Instrucciones de Ejecución

Se genera un archivo .py y un notebook para el desarrollo de los puntos del taller los cuales deben ejecutarse en el siguiente orden: 
1. 


#### Autores

| Organización   | Nombre | Correo electronico | 
|----------|-------------|-------------|
| Uniandes |  Lizeth Viviana Perdomo Castañeda | lv.perdomoc1@uniandes.edu.co |
| Uniandes |  David Esteban Fajardo Torres | de.fajardo@uniandes.edu.co |
