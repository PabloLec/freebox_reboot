# Principe

Ce script Python permet de redémarrer sa Freebox (Freebox OS >3.0) via un périphérique du réseau local avec l'aide de Selenium

# Prérequis

- Python 3.x
- Selenium 3.x (voir https://www.selenium.dev)
- Chrome driver (voir https://chromedriver.storage.googleapis.com/index.html) 

# Installation/Utilisation

- Téléchargez/Clonez le dépot
- Remplacez la valeur de la variable MOT_DE_PASSE par le mot de passe que vous utilisez pour vous connecter à Freebox OS.
  (voir https://mafreebox.freebox.fr)
- Exécutez le fichier free_reboot.py
  
# Troubleshooting 
Si ce n'est pas déjà le cas, installez Selenium via pip (Pip inclus par défaut dans python 3.4+):

Pour l'installation de pip: https://pip.pypa.io/en/stable/installing/

Pour installer Selenium: ```pip3 install selenium```

---

Si vous utilisez pour la première fois Selenium : 

Le driver Chrome doit se trouver dans votre PATH.

- Pour visualiser vos PATH et éventuellement déplacer/copier le driver Chrome dans l'un des chemins:

 >Windows Powershell :
```$env:path -split ";"```

>Linux/MacOS :
```echo $PATH```

- Sinon, ajoutez le chemin du driver à la variable PATH:

> Windows Powershell :
```$env:Path += ";LEMPLACEMENT_DU_DRIVER_CHROME"```  

> Linux/MacOS :
```PATH=$PATH:LEMPLACEMENT_DU_DRIVER_CHROME```



Si vous obtenez tout de même une erreur de driver à l'exectution du script vous pouvez essayer de modifier le fichier ```free_reboot.py```:

- En première ligne :
```import os```  

- Avant ou après la variable MOT_DE_PASSE:

> Windows Powershell :
```os.system("$env:Path += ";LEMPLACEMENT_DU_DRIVER_CHROME")```  

> Linux/MacOS :
```os.system("PATH=$PATH:LEMPLACEMENT_DU_DRIVER_CHROME")```
