# LCL Data Extractor

*Note: This is my first Python data analysis-oriented project*

![bank](https://img.freepik.com/photos-gratuite/homme-tenant-carte-credit-main-entrant-code-securite-aide-telephone-intelligent-clavier-ordinateur-portable-concept-magasinage-ligne_1423-22.jpg?w=740&t=st=1695044881~exp=1695045481~hmac=32e01969b76374242df28d4be4fac006ad14e25a999fdbd21b99c6c668859b5c)

## (FR)

lcl-data-extractor met sous la forme d'un unique fichier .csv les différents relevés bancaires mensuels LCL séparés au format .pdf.

Le fichier .csv final comporte quatre colonnes : 'objet' (object type), 'date' (datetime64 type), 'debit' (float64 type) et 'credit' (float64 type).

Ce programme gère plusieurs type d'erreurs qui peuvent se rencontrer durant l'import à cause de la nature semi-structurée des tableaux extraits des fichiers .pdf.

Il est possible que certaines erreurs ne soient pas prises en charge, dans ce cas, faites m'en part afin que je l'améliore.

La prochaine étape prévue sera de mettre au point un système de catégorisation des 'objet' (nom d'opération) afin de pouvoir analyser les dépenses ou les crédits par famille. Cela rajoutera donc un certain nombre de colonnes.

## (EN)

lcl-data-extractor returns a unique .csv file from separated LCL bank monthly statements pdfs.

The exported .csv file is made up of four columns : 'objet' (object type), 'date' (datetime64 type), 'debit' (float64 type) and 'credit' (float64 type).

It handles several errors that may appear during the cleaning process. The aleatory appearance of theses errors is due to the semi-structured nature of data originating from pdf files.

It is likely that errors unknown to me, but appearing in your files, may occur. Please, contact me so that I can try to fix them and improve this program.

The next step is to categorize the 'objet' values (e.g., categories such as "grocery", "rent", "fuel", etc.). Then, providing a couple of analysis tools to the user. Finally, providing data visualization tools to the user.
