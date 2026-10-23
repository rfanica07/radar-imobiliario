# Números de porta — fontes e limites

Consulta em 23/10/2026. Os dados municipais foram cruzados com o OpenStreetMap nos perímetros aproximados já usados pela aplicação. Não constituem uma contagem de prédios: um edifício pode ter várias entradas, incluindo lojas e garagens. Não foram geradas sequências numéricas nem andares.

Fontes integradas:

- [Montijo — números de polícia municipais](https://mtgeo.mun-montijo.pt/arcgis/rest/services/INFOBASE/RUAS_NRS_POLICIA/MapServer/1).
- [Seixal — endereços municipais](https://sig.cm-seixal.pt/arcgis/rest/services/PLOC/MapServer/29), para Corroios, Santa Marta e Cruz de Pau.
- [Lisboa — números de polícia, base cartográfica 2018](https://gisbase.cm-lisboa.pt/arcgis/rest/services/MapaBase_Cart2018/MapServer/3), para o perímetro de Benfica. A data da consulta não é a data de atualização de cada entrada.
- [OpenStreetMap](https://www.openstreetmap.org/copyright), dados já incorporados nos 20 perímetros.

Os números foram filtrados pelo perímetro e por rua/número; os registos municipais sobrepostos a uma entrada existente com o mesmo número num raio aproximado de 12 metros foram removidos. Podem subsistir variantes de nomes de ruas. Não se inferiu uma percentagem de cobertura: não existe um total independente confirmado.

Outras fontes investigadas:

- [CTT — pesquisa de códigos postais](https://appserver2.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx?lang=def): segmentos e intervalos postais não comprovam a existência de cada número intermédio.
- [GeoMoita](https://moita.city-platform.com/v2/portal): identificado o portal oficial; o recurso de configuração consultado pediu autenticação. Entretanto foi obtido o inventário histórico do INE, descrito abaixo.
- Odivelas e Sintra: camadas municipais identificadas, mas as consultas de dados exigiram token. Nenhum acesso protegido foi contornado.
- Não foi feita uma inspeção visual sistemática em Google Street View. Nenhum registo está classificado como confirmado por fotografia.

Na aplicação, ao selecionar uma rua, a lista de entradas cartográficas mostra também números cujas etiquetas se sobrepõem no mapa. Um clique abre o resumo, dois cliques abrem a edição. Os andares e frações continuam a ser confirmados no terreno. Os registos pessoais de prospeção permanecem no armazenamento local do navegador.

O ficheiro `Cobertura-de-portas.json` contém as contagens por perímetro. As fontes municipais são atribuídas, sem presumir uma licença CC0 ou uma autorização para redistribuição comercial autónoma dos dados.


## Atualização da Moita e Baixa da Banheira

Integrada a **Base Nacional de Moradas do Instituto Nacional de Estatística, I.P.**, edição histórica com validade indicada de 01/01/2018. Fonte direta: [serviço INSPIRE do INE](https://inspire.ine.pt/AD/atom/downloadservice.html), ficheiro municipal [Moita — WGS84](https://inspire.ine.pt/AD/atom/gml/Addresses_1506_EPSG4326.zip). O ficheiro GML declara extração em 03/04/2018.

A pesquisa no [Overture Maps](https://docs.overturemaps.org/guides/addresses/) permitiu encontrar esta fonte nacional. Foram também consultados os registos da área da vila na versão Overture de 21/10/2026, que atribui a origem ao OpenAddresses/INE. A importação em 2026 não demonstra atualização das moradas no terreno em 2026. Licença identificada: CC BY 4.0; atribuição: Instituto Nacional de Estatística, I.P.; via OpenAddresses / Overture Maps quando aplicável.

Foram extraídos exclusivamente os identificadores de edifício (`buildingIdentifier`), a rua e o ponto geográfico. Registos repetidos de andares e frações foram agrupados por rua/número; esses andares e frações não foram importados. Registos sem número não foram transformados em portas fictícias. Não foram importados nomes ou dados de residentes.

- Perímetro atual da Moita: **1 561 entradas cartográficas**, das quais **1 544 acrescentadas** nesta atualização.
- Perímetro atual da Baixa da Banheira: **2 891 entradas cartográficas**, das quais **2 811 acrescentadas** nesta atualização.
- Inventário histórico municipal exportado: **8 998 combinações de rua/número** no ficheiro `Moita-inventario-INE-2018.geojson`. Este inventário abrange o concelho; os dois mapas da aplicação continuam a respeitar os seus perímetros de prospeção.

Os nomes abreviados de vias foram normalizados para associar os números às ruas do mapa. Algumas variantes, renumerações, lotes e entradas secundárias podem exigir correção no terreno. A fonte e a idade dos dados aparecem no resumo de cada porta importada. Não se trata de uma confirmação visual por Street View nem de uma garantia de que todas as entradas continuam iguais.
