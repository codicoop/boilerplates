# Boilerplates de Codi Cooperatiu

## django_base_structure
Estructura inicial que tenen en comú la majoria dels nostres projectes.

La pots copiar directament des de la terminal al teu directori actual amb la següent comanda, sempre que estiguis fent servir BASH
```bash
curl -LJO https://codeload.github.com/codicoop/boilerplates/zip/refs/heads/master
unzip boilerplates-master.zip
mv boilerplates-master/django_base_structure/{,.}* .
rm -rf boilerplates-master boilerplates-master.zip
```

> Les opcions pel cURL són:
> -L: Segueix qualsevol redirect que la URL retorni.
> -O: Descarrega la reposta en un fitxer.
> -J: Utilitza el nom del fitxer retornat pels headers.
>
> És necessari la wildcard {,.}* per moure també els fitxers ocults del repositori.


## cities
App per organitzar les poblacions.
De moment compta amb una fixture per carregar les
dades oficials de totes les poblacions de Catalunya.
