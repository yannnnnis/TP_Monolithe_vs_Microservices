# Application en microservices

Exemple pédagogique avec deux services :
- `order-service`
- `payment-service`

Lancer :
```bash
cd docker
docker compose up --build
```

Order Service : http://localhost:8001
Payment Service : http://localhost:8002

Le `order-service` appelle le `payment-service` par HTTP.
Chaque service possède son Dockerfile, ses tests et son pipeline CI/CD.
