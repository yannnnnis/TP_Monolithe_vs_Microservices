# TP — Monolithe vs Microservices

Ce dossier contient :
- `DOCUMENT_EXPLICATIF.md` : comparaison pédagogique complète ;
- `01-monolithe/` : application e-commerce en monolithe ;
- `02-microservices/` : application découpée en `order-service` et `payment-service`.

Chaque exemple contient Docker, tests et un exemple de pipeline GitLab CI.

Objectif : comparer organisation, déploiement, CI/CD, communication, scalabilité, données et complexité.

# Architecture Hexagonale - Plateforme de Réservation

## 1. Principe Ports & Adapters
L'architecture hexagonale (ou Ports & Adapters) vise à isoler la logique métier (le cœur de l'application) des préoccupations externes (bases de données, interfaces utilisateur, API tierces). 
* **Le Cœur (Domain & Application)** ignore tout du monde extérieur.
* **Les Ports** définissent des interfaces pour communiquer avec l'extérieur.
* **Les Adapters** implémentent ces ports pour connecter des technologies concrètes (frameworks web, SGBD, services de paiement).

## 2. Rôle des dossiers et responsabilités

* **`domain/` (Le Cœur Métier)**
  * **Rôle :** Contient la logique métier pure et les règles de gestion de la plateforme de réservation (ex: règles de disponibilité, calcul des prix, validation d'une réservation).
  * **Responsabilités :** Définir les entités (`Reservation`, `User`, `Disponibilite`) et les objets de valeur sans aucune dépendance externe (pas de framework, pas de SQL).

* **`application/` (Cas d'utilisation)**
  * **Rôle :** Coordonne les flux de l'application en fonction des requêtes entrantes.
  * **Responsabilités :** Implémenter les cas d'utilisation (ex: `EffectuerReservationUseCase`, `EnvoyerNotificationUseCase`). Il orchestre le domaine mais ne contient pas de règles métier.

* **`ports/` (Interfaces)**
  * **Rôle :** Fait la liaison entre l'intérieur et l'extérieur. On distingue :
    * *Ports Entrants (Driving/Primary)* : Interfaces appelées par l'extérieur (ex: contrôleurs HTTP, commandes CLI).
    * *Ports Sortants (Driven/Secondary)* : Interfaces utilisées par l'application pour interagir avec l'extérieur (ex: repository de données, passerelle de paiement, service de notification).

* **`adapters/` (Implémentations techniques)**
  * **Rôle :** Contient le code technique lié aux frameworks et technologies spécifiques.
  * **Responsabilités :** 
    * *Adapters Entrants* : API REST, GraphQL, interfaces web.
    * *Adapters Sortants* : Connexion à la base de données (PostgreSQL/MongoDB), intégration de l'API de paiement (Stripe), service d'e-mail (SendGrid).

## 3. Relations entre les parties

1. L'utilisateur interagit avec un **Adapter Entrant** (ex: API REST).
2. Cet adapter appelle un **Port Entrant** (Cas d'utilisation dans `application/`).
3. L'application manipule les objets du **`domain/`** pour exécuter la logique métier.
4. Si une persistance ou un service externe est requis, l'application passe par un **Port Sortant**.
5. Un **Adapter Sortant** implémente ce port pour effectuer l'appel technique réel (ex: requête SQL ou appel HTTP vers Stripe).

## 4. Schéma de l'architecture

[ Client / UI / API ] 
        │
        ▼ (Adapters Entrants)
   [ Port Entrant ]
        │
        ▼
   [ Application ] ──> [ Domain ]
        │
        ▼ (Ports Sortants)
   [ Adapters Sortants ] ──> [ Base de données / Stripe / Notifications ]