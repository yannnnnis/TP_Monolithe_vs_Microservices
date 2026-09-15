# Monolithe vs Microservices — guide pédagogique

## 1. Application exemple

On utilise une application e-commerce appelée **ShopDemo** avec quatre capacités :
- Commandes
- Catalogue
- Paiement
- Notifications

La même application est étudiée avec deux architectures.

## 2. Monolithe

Toutes les capacités sont regroupées dans **une seule application déployable**.

```text
        APPLICATION SHOPDEMO
┌──────────────────────────────┐
│ Commandes                    │
│ Catalogue                    │
│ Paiement                     │
│ Notifications               │
└──────────────┬───────────────┘
               ↓
         1 déploiement
```

Un pipeline typique :

```text
Git push → Build → Tests → Docker image → Deploy
```

Si seul le paiement change, on reconstruit généralement l'application entière.

## 3. Microservices

Les capacités sont séparées en services autonomes.

```text
┌──────────────┐       HTTP       ┌──────────────┐
│ Order Service│ ───────────────► │Payment       │
│              │                  │Service       │
└──────────────┘                  └──────────────┘
```

Chaque service possède son code, ses tests, son image Docker et peut avoir son pipeline.

```text
Order Service   → Build → Tests → Image → Deploy

Payment Service → Build → Tests → Image → Deploy
```

Si seul le paiement change, seul `payment-service` peut être reconstruit et déployé.

## 4. Comparaison

| Critère | Monolithe | Microservices |
|---|---|---|
| Déploiement | Une unité | Plusieurs unités |
| Code | Une application | Plusieurs services |
| Communication | Appels internes | HTTP, messages, etc. |
| Pipeline | Souvent centralisé | Par service ou pipelines conditionnels |
| Scalabilité | Souvent application entière | Service ciblé |
| Données | Souvent base commune | Peut être séparée par service |
| Réseau | Moins critique | Important |
| Pannes | Plus simples à diagnostiquer | Risques de latence/cascades |
| Observabilité | Plus simple | Tracing distribué souvent nécessaire |
| Infrastructure | Plus simple | Plus complexe |

## 5. Exemple de changement : paiement

### Monolithe

```text
Modification paiement
        ↓
Build application entière
        ↓
Tests
        ↓
Nouvelle image
        ↓
Déploiement de l'application
```

### Microservices

```text
Modification paiement
        ↓
Build payment-service
        ↓
Tests payment-service
        ↓
Nouvelle image
        ↓
Déploiement payment-service
```

C'est l'un des principaux intérêts des microservices : **l'indépendance de déploiement**.

## 6. Scalabilité

Monolithe :

```text
Catalogue très sollicité
        ↓
On scale souvent toute l'application
```

Microservices :

```text
Catalogue  → 10 instances
Commandes  → 3 instances
Paiement   → 4 instances
```

On peut scaler une capacité ciblée.

## 7. Données

Monolithe :

```text
Application → PostgreSQL
              ├── commandes
              ├── clients
              ├── produits
              └── paiements
```

Microservices :

```text
Order Service   → données commandes
Payment Service → données paiements
Catalog Service → données catalogue
```

La séparation augmente l'autonomie, mais rend les transactions entre services plus complexes.

## 8. Pipeline CI/CD

### Monolithe

Un pipeline principal suffit souvent :

```text
Build → Test → Docker → Deploy
```

### Microservices

On peut avoir un pipeline par service :

```text
Order Service
Build → Test → Docker → Deploy

Payment Service
Build → Test → Docker → Deploy
```

Dans un vrai projet, on peut aussi utiliser un mono-repo avec des pipelines déclenchés uniquement lorsqu'un dossier/service change.

## 9. Coûts des microservices

Les microservices apportent :
- déploiement indépendant ;
- scalabilité ciblée ;
- autonomie par domaine.

Mais ils ajoutent :
- réseau ;
- plusieurs pipelines ;
- observabilité ;
- sécurité entre services ;
- gestion des contrats ;
- complexité des données distribuées ;
- infrastructure plus importante.

## 10. Quand choisir ?

### Monolithe
À privilégier lorsque l'application est simple ou lorsque l'équipe veut limiter la complexité opérationnelle.

### Monolithe modulaire
Très bon compromis : une seule application déployable, mais des frontières métier et des dépendances contrôlées.

### Microservices
Pertinents lorsque le domaine est suffisamment complexe et qu'il existe un vrai besoin de déploiement, de scalabilité ou d'autonomie indépendants.

> **Un bon monolithe modulaire est souvent préférable à un mauvais système de microservices.**

## 11. Question de synthèse

Une application e-commerce doit-elle forcément devenir une architecture microservices ?

Justifiez votre réponse en prenant en compte :
- complexité ;
- déploiement ;
- scalabilité ;
- équipe ;
- données ;
- observabilité ;
- coût d'infrastructure.
