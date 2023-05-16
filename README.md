# lcl-extractor-py

===EN===

lcl-extractor-py returns a unique .csv file from separated LCL bank monthly statements pdfs.

The exported .csv file is made up of four columns : 'objet' (object type), 'date' (datetime64 type), 'debit' (float64 type) and 'credit' (float64 type).

It handles several errors that may appear during the cleaning process. The aleatory appearance of theses errors is due to the semi-structured nature of data originating from pdf files.

It is likely that errors unknown to me, but appearing in your files, may occur. Please, contact me so that I can try to fix them and improve this program.

The next step is to categorize the 'objet' values (e.g., categories such as "grocery", "rent", "fuel", etc.). Then, providing a couple of analysis tools to the user. Finally, providing data visualization tools to the user.

===FR===

lcl-extractor-py met sous la forme d'un unique fichier .csv les différents relevés bancaires mensuels LCL séparés au format .pdf.

Le fichier .csv final comporte quatre colonnes : 'objet' (object type), 'date' (datetime64 type), 'debit' (float64 type) et 'credit' (float64 type).

Ce programme gère plusieurs type d'erreurs qui peuvent se rencontrer durant l'import à cause de la nature semi-structurée des tableaux extraits des fichiers .pdf.

Il est possible que certaines erreurs ne soient pas prises en charge, dans ce cas, faites m'en part afin que je l'améliore.

La prochaine étape prévue sera de mettre au point un système de catégorisation des 'objet' (nom d'opération) afin de pouvoir analyser les dépenses ou les crédits par famille. Cela rajoutera donc un certain nombre de colonnes.


