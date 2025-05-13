Politique de sécurité pour le projet Football Prediction Bot
📜 Objectif
Ce projet utilise des API externes pour prédire les résultats des matchs de football et interagir avec Telegram. Il est donc impératif que les données sensibles soient gérées de manière sécurisée pour protéger l'accès à l'API, à Telegram, et aux informations personnelles des utilisateurs.

🔒 Bonnes pratiques de sécurité
Clé API : Ne jamais stocker les clés API, tokens ou mots de passe dans le code source. Utilisez un fichier .env pour stocker ces informations et ajoutez-le à .gitignore afin qu'il ne soit pas commité dans le dépôt public.

Gestion des secrets :

Utilisez des outils comme Vault, AWS Secrets Manager, ou GitHub Secrets pour gérer les tokens et informations sensibles.

Si vous devez tester localement, assurez-vous que le fichier .env est dans .gitignore et non dans le dépôt Git.

Fichiers sensibles : Ne jamais inclure des fichiers contenant des informations sensibles, comme des clés API, mots de passe ou données d'utilisateurs. Utilisez des environnements de développement et de production séparés.

Permissions : Restreindre l’accès aux secrets dans GitHub. Si vous travaillez en équipe, configurez des access permissions strictes (par exemple, principle of least privilege).

🛡️ Gestion des vulnérabilités
🚨 Comment signaler une vulnérabilité ?
Si vous découvrez une vulnérabilité de sécurité dans ce projet, nous vous encourageons à la signaler de manière responsable en suivant ces étapes :

Ne pas publier immédiatement la vulnérabilité.

Contactez le mainteneur du projet directement à l'adresse email suivante : gmebale@gmail.com (ou créez un issue privé).

Fournissez des détails sur la vulnérabilité, y compris comment elle peut être reproduite (idéalement dans un environnement de test).

Suivi de la résolution : Nous nous engageons à résoudre toute vulnérabilité de manière proactive et à publier des correctifs dès que possible.

🛠️ Gestion des incidents
Rapports d'incident : Si vous pensez que votre clé API ou un autre secret a été exposé, révoquez-le immédiatement via l'interface d'administration de l'API concernée (par exemple, Football-data API, Telegram Bot API).

Audit de sécurité : Ce projet sera audité de manière régulière pour détecter des vulnérabilités potentielles. Les résultats des audits seront publiés dans le répertoire security-audits/.

⚠️ Remarques importantes
N'utilisez jamais des tokens API ou des informations sensibles en texte clair dans le code source.

Les commits contenant des informations sensibles seront immédiatement révoqués, et des mesures correctives seront prises.

En cas de doute, contactez le mainteneur pour obtenir des conseils avant d'effectuer des modifications.

🔑 Accès et vérification
Ce projet peut utiliser des services externes comme Telegram API et Football-Data API, et nécessite des tokens d'authentification. Les utilisateurs doivent s'assurer de gérer ces tokens de manière sécurisée et de ne pas les exposer dans les commits.

🛑 Limitations d'accès
Les utilisateurs ne doivent pas essayer de contourner les restrictions d'accès à l'API ou à Telegram, telles que celles configurées dans le code ou dans l'environnement de production.

📅 Mise à jour
Dernière mise à jour : 2025-05-13
