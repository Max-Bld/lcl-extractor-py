# extracteur-donnees-LCL

L'extracteur de données LCL permet de mettre sous la forme d'un unique fichier .csv les données bancaires séparées dans différents relevés de comptes LCL au format .pdf.

Le fichier .csv final comporte quatre colonnes : objet (object), date (datetime64), debit (float64), credit (float64).

Durant le nettoyage des données, ce programme gère plusieurs type d'erreurs qui peuvent se rencontrer durant l'import à cause de la nature semi-structurée des tableaux extraits des fichiers .pdf.

La prochaine étape prévue sera de mettre au point un système de catégorisation des 'objet' (nom d'opération) afin de pouvoir analyser les dépenses ou les crédits par famille. Cela rajoutera donc un certain nombre de colonnes.

Si vous avez un compte chez LCL et que vous souhaitez un fichier .csv de vos relevés bancaires, n'hésitez pas à essayer ce programme. Il est possible que certaines erreurs ne soient pas prises en charge, dans ce cas, faites m'en part afin que je l'améliore.
