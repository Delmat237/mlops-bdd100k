# mlops-bdd100k

Pipeline MLOps de bout en bout pour un modèle de vision : classification du type
de scène routière (city street / highway / residential) sur le jeu de données
BDD100K.

Le modèle reste volontairement simple. L'objet du projet est la chaîne qui
l'entoure : reproductibilité, suivi, déploiement et surveillance.

## Contexte
Projet d'apprentissage réalisé dans le cadre d'une préparation à la recherche
en vision et MLOps (ENSTA Paris, spécialisation Data & IA).

## Avancement
- [ ] Jalon 0 : socle (repo, packaging, tests, CI)
- [ ] Jalon 1 : reproductibilité (DVC, config, seeds)
- [ ] Jalon 2 : suivi d'expériences (MLflow)
- [ ] Jalon 3 : conteneurisation et serving (Docker, FastAPI)
- [ ] Jalon 4 : CI/CD ML
- [ ] Jalon 5 : monitoring et détection de dérive
- [ ] Jalon 6 : orchestration et ré-entraînement

## Démarrage rapide
> À compléter au jalon 0.

    make install
    make test

## Structure
    src/       code du package
    tests/     tests pytest
    configs/   configuration d'entraînement
    data/      données (suivies par DVC, non commitées)

## Données
BDD100K (Berkeley DeepDrive), sous-ensemble 10K. Les données ne sont pas
incluses dans le dépôt ; voir les conditions d'utilisation du jeu de données.

## Licence
MIT (code uniquement).
