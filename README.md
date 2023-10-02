# Despliegue Open Telementry python dynatrace demo
Integración python opentelemetry con instrumentación automática sobre AKS

#### Aplica la configuración de Kubernetes:
	kubectl apply -f deployment-aks.yaml

#### Una vez desplegado, puedes ver la IP del balanceador de carga:
	kubectl get services gestor-de-datos-service

#### Para ver las trazas y métricas en los logs del pod:
   - Encuentra el nombre del pod:

	kubectl get pods -l app=gestor-de-datos
   - Ve los logs:

	kubectl logs [NOMBRE_DEL_POD]
   
