# Geo Tracker API

## Descripción del Proyecto

Geo Tracker API es una herramienta desarrollada en Python y Docker orientada a automatizar la consulta de información geográfica y de red mediante el consumo de una API pública de geolocalización IP.

La aplicación permite obtener información relevante de conectividad como:

- Dirección IP pública
- País
- Ciudad
- Región
- Coordenadas geográficas
- ISP
- Zona horaria

El proyecto fue desarrollado aplicando principios DevOps, integración continua y contenedorización con Docker.

---

# Stakeholder

El principal stakeholder de esta herramienta es un administrador de redes o analista DevOps que necesita identificar rápidamente información geográfica y de conectividad asociada a una dirección IP pública para monitoreo, validación de servicios o análisis de infraestructura.

---

# Propuesta de Valor

En entornos de redes y administración de infraestructura, es frecuente necesitar identificar la ubicación aproximada de un host conectado a internet para validar conectividad, detectar accesos externos o verificar servicios desplegados en distintas regiones.

Geo Tracker API automatiza este proceso permitiendo consultar información geográfica y de red de manera rápida, simple y portable mediante contenedores Docker.

La solución elimina la necesidad de realizar búsquedas manuales y facilita la integración con pipelines DevOps y herramientas de monitoreo.

---

# Tecnologías Utilizadas

- Python 3
- Docker
- GitHub
- Jenkins
- Requests API

---

# Variables de Entorno

Actualmente el proyecto no requiere variables de entorno obligatorias para funcionar.

Sin embargo, puede configurarse la URL de la API modificando la variable:

```python
URL = "http://ip-api.com/json/"
```

---

# Estructura del Proyecto

```text
geo-tracker/
│
├── app.py
├── Dockerfile
├── build.sh
├── requirements.txt
├── README.md
├── Jenkinsfile
├── .gitignore
│
└── evidencias/
    ├── docker/
    └── jenkins/
```

---

# Ejecución Local

## Instalar dependencias

```bash
pip install -r requirements.txt
```

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

# Integración Continua (CI/CD)

El proyecto incorpora Jenkins para automatizar:

- Clonado del repositorio GitHub
- Construcción de imágenes Docker
- Ejecución automática del contenedor
- Validación del pipeline DevOps

---

# Evidencias

Las evidencias del proyecto se almacenan en:

```text
evidencias/docker/
evidencias/jenkins/
```

Incluyendo:

- Logs de ejecución
- Capturas de pantalla
- Resultados Docker
- Resultados Jenkins Pipeline

---

# Autor

Proyecto desarrollado por Nicolas Seguel como parte de una evaluación DevOps e integración continua.
