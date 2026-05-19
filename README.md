# Geo Tracker API

## Descripción del Proyecto

Geo Tracker API es una aplicación desarrollada en Python que consume una API pública de geolocalización para obtener información aproximada de ubicación basada en la dirección IP del usuario.

La aplicación fue contenerizada utilizando Docker y automatizada mediante Jenkins, permitiendo construir y ejecutar el proyecto automáticamente desde un repositorio GitHub.

---

# A. Definición del Contexto y Narrativa

## Stakeholder

Un administrador de redes y ciberseguridad necesita identificar rápidamente información geográfica aproximada de direcciones IP para tareas de monitoreo, validación de conexiones y análisis de actividad en la red.

## Propuesta de Valor (Problema / Solución)

En muchas organizaciones, los administradores necesitan verificar desde qué ubicación se originan conexiones hacia servicios internos o externos. Realizar este proceso manualmente puede ser lento y poco eficiente.

Geo Tracker API automatiza la consulta de geolocalización mediante APIs públicas, permitiendo obtener información relevante como:

* Dirección IP
* País
* Ciudad
* Región
* Latitud
* Longitud

Además, el proyecto implementa automatización CI/CD básica usando Jenkins y Docker, facilitando despliegues rápidos y reproducibles.

---

# Tecnologías Utilizadas

* Python 3.11
* Docker
* Jenkins
* GitHub
* API pública de geolocalización

---

# Estructura del Proyecto

```bash
geo-tracker-api/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── README.md
│
└── evidencias/
    └── docker/
    │    ├── docker.png
    │    └── output.txt
    └── jenkins/
        ├── console_output_build.png
        ├── stage_view.png
        ├── credentials.png
        └── pipeline_script.txt
```

---

# Guía de Configuración

## Variables de Entorno

Actualmente el proyecto no requiere variables de entorno obligatorias.

En futuras versiones se podría implementar:

```env
API_KEY=valor_api
```

---

# Instalación Local

## 1. Clonar repositorio

```bash
git clone https://github.com/ncseguel-lang/geo-tracker-api.git
```

## 2. Ingresar al proyecto

```bash
cd geo-tracker-api
```

## 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# Ejecución Local

## Ejecutar aplicación

```bash
python app.py
```

---

# Ejecución Docker

## Construir imagen Docker

```bash
docker build -t geo-app .
```

## Ejecutar contenedor

```bash
docker run --name samplerunning geo-app
```

---

# Jenkins

## BuildAppJob

Trabajo de tipo Freestyle encargado de:

* Clonar el repositorio desde GitHub
* Construir la imagen Docker
* Ejecutar el contenedor
* Mostrar salida de la API

## SamplePipeline

Pipeline encargado de automatizar el flujo completo en dos etapas:

### Preparation

* Detener contenedor anterior
* Eliminar contenedor existente
* Uso de catchError para evitar fallos si el contenedor no existe

### Build

* Ejecutar automáticamente BuildAppJob

---

# Pipeline Script

```groovy
pipeline {
    agent any

    stages {

        stage('Preparation') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat 'docker stop samplerunning'
                    bat 'docker rm samplerunning'
                }
            }
        }

        stage('Build') {
            steps {
                build job: 'BuildAppJob'
            }
        }
    }
}
```

---

# Evidencias Jenkins

Las evidencias solicitadas por el informe se encuentran en:

```bash
evidencias/jenkins
```

Archivos incluidos:

* console_output_build.png
* stage_view.png
* credentials.png
* pipeline_script.txt

---

# Autor

Nicolas Eliseo Seguel Barrientos

---

# Repositorio GitHub

[https://github.com/ncseguel-lang/geo-tracker-api](https://github.com/ncseguel-lang/geo-tracker-api)
