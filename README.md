# Principe

Ce script Python permet de redémarrer sa Freebox (Freebox OS >3.0) via un périphérique du réseau local avec l'aide de Selenium

# Prérequis

- Python 3.x
- Selenium 3.x (voir https://www.selenium.dev)
- Chrome driver (voir https://chromedriver.storage.googleapis.com/index.html) 
  
# Troubleshooting
Si vous utilisez pour la première fois Selenium, le driver Chrome doit se trouver dans votre PATH.

Pour visualiser vos PATH et éventuellement déplacer/copier le driver Chrome dans l'un des chemins:

 >Windows/Powershell
```$env:path -split ";"```

>Linux/MacOS
```echo $PATH```

- Sinon, ajouter le chemin du driver à la variable PATH:

> Windows/Powershell
```$env:Path += ";LEMPLACEMENT_DU_DRIVER_CHROME"```  

> Linux/MacOS
```PATH=$PATH:LEMPLACEMENT_DU_DRIVER_CHROME```

Si vous obtenez tout de même une erreur de driver à l'exectution du script vous pouvez essayer:

- En première ligne :
```import os```  

- Avant ou après la variable MOT_DE_PASSE:

> Windows/Powershell
```os.system("$env:Path += ";LEMPLACEMENT_DU_DRIVER_CHROME")```  

> Linux/MacOS
```os.system("PATH=$PATH:LEMPLACEMENT_DU_DRIVER_CHROME")```
