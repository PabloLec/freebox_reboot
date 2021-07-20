# Principe

Ce script Python permet de redémarrer sa Freebox (Freebox OS >3.0) via un périphérique du réseau local.

# Installation

```
python3 -m pip install freebox_reboot
```
  
# Utilisation 

Pour démarrer le script:

```
python3 -m freebox_reboot
```

A la première utilisation, l'application va générer un token d'authentification qui sera automatiquement utilisé à l'avenir.

- Démarrez le script avec la commande ci-dessus.
- Au bout de quelques secondes vous devriez voir apparaître " - En attente d'autorisation"
- Sur l'écran de votre Freebox une demande de confirmation devrait vous être demandée, accordez l'accès à l'application à l'aide des boutons présents sur votre Freebox.
- Le script va reprendre son éxecution puis vous informer qu'il ne dispose pas des droits nécessaires.
- Rendez vous sur http://mafreebox.freebox.fr/#Fbx.os.app.settings.Accounts
- Ouvrez l'onglet *Applications*.
- Trouvez l'application *Freebox Reboot*.
- Cochez la case *Modification des réglages de la Freebox*.
- Validez.
- La configuration est terminée, les paramètres sont sauvegardés, vous pouvez maintenant relancer le script.

# Arguments

Les arguments optionels suivants sont disponibles:

- `-v`, `--verbose` Affiche toutes les requêtes et leurs réponses.
- `-d`, `--dry` Exécute le script sans redémarrer la Freebox.
- `--http` Effectuer les requêtes vers l'API en HTTP et non en HTTPS.
