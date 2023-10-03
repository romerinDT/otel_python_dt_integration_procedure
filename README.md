# Despliegue Open Telementry python dynatrace demo
Integración python opentelemetry con instrumentación automática sobre AKS

#### Crear y subir la imagen a docker hub :
Para este punto seguir las intrucciones [otel-flask-demo](https://github.com/DT-Team-Peru/otel_python_dt_integration_demo/tree/main/otel-flask-demo#construcci%C3%B3n-de-la-aplicaci%C3%B3n)

#### Aplica la configuración de Kubernetes:
	kubectl apply -f deployment-aks.yaml

#### Una vez desplegado, puedes ver la IP del balanceador de carga:
	kubectl get services gestor-de-datos-service

#### Para ver las trazas y métricas en los logs del pod:
   - Encuentra el nombre del pod:

	kubectl get pods -l app=gestor-de-datos
   - Ve los logs:

	kubectl logs [NOMBRE_DEL_POD]
   
#### Generar trafico para prueba:
   - Ejecutar el archivo python trafic_generator.py:

	python trafic_generator.py
