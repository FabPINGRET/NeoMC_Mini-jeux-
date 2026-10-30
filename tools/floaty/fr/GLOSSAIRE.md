# Glossaire de la traduction française de Floaty

**VALIDÉ par Maxime le 2026-10-30** (décisions au §6). Les tables de traduction (`fr/*.json`, `{anglais: français}`) et les surcharges par
fonction (`fr/ctx.json`) s'écrivent d'après ce document. Les chiffres viennent de `python tools/floaty/fr_extract.py --map <carte>`
(sortie dans `cache/floaty_fr/`, hors dépôt).

**Principe d'ensemble : tout ce qui est un NOM reste en anglais (personnages, lieux, objets, titres, peuples inventés, noms de boss ou de
mécanique) ; les noms communs et le reste du texte sont traduits.**

## 1. Chiffres de l'extraction

- 13 599 occurrences de texte visible, 5 102 clés distinctes, clés protégées déjà exclues (98 : 95 calculées + 4 manuelles, voir
  `protected.txt`). Le recensement du plan annonçait ~13 502 / ~4 922 : écart non reproduit (le compte inclut ici advancements et barres de boss).
- Par espace de noms (occurrences) : npc 11 132, game 780, boss 529, dungeon 349, summon 225, utility 201, main_quest 190, sidequest_2 78,
  sidequest 62, floaty 41, item 10, tool 2. Dans `npc`, `glooblin` (Wuggy) pèse 4 193 occurrences pour 243 clés seulement : une même phrase
  répétée par arme.
- Par emplacement : tellraw 11 694, lore 706, CustomName 313, custom_name 260, sign 224, title 154 (presque tous des lettres isolées, voir
  §5), advancements 193 (96 titres, 97 descriptions), bossbar 31, subtitle 12, actionbar 11, text_display 1.
- Le texte est surtout du **dialogue de PNJ** découpé en fragments (`<` + nom + `> ` + phrase) : une clé est un FRAGMENT, pas une phrase.

## 2. Conventions

- **Tutoiement du joueur** (« Tu as trouvé la clé »), **vouvoiement pour le groupe** (« Vous avez trouvé... », « Venez », quand le PNJ s'adresse
  à plusieurs personnes ou à un collectif). **Entre PNJ** (cinématiques) : tutoiement par défaut, **vouvoiement envers les seigneurs et la
  reine**.
- **Apostrophe typographique ’** (U+2019) partout : « l’épée », « aujourd’hui ». Jamais l'apostrophe droite `'` dans le français produit.
- **Espace insécable U+00A0 AVANT** `:` `;` `!` `?` et `»`, et APRÈS `«` : « Attention ! », « Quoi ? », « Il dit : « non » ». (Seuls ces exemples portent de vrais U+00A0 ;
  ailleurs dans ce document les espaces sont ordinaires, par lisibilité.) Pas d'espace avant `.` ni `,`.
- **Guillemets français « »** pour les citations ; les guillemets droits `"` n'apparaissent que dans le JSON.
- Points de suspension : on garde `...` (trois points ASCII), jamais `…` (§6, q. 14).
- Onomatopées : les **actions** sont adaptées (« *checks notes* » devient « *regarde ses notes* ») ; les **sons purs** (`*nuk-tuk*`, `*tuk-nuk*`,
  `bzzrt...`) restent tels quels (§6, q. 11).
- Un fragment qui n'a pas de lettre (« < », « . », nombres, emoji) n'est jamais traduit : le moteur l'ignore déjà.
- L'ordre des mots français diffère : un fragment traduit doit rester **juste à sa place** (avant ou après le nom propre qui l'entoure).
  Quand ce n'est pas possible, voir §5 (surcharge par fonction dans `ctx.json`).

## 3. Noms propres conservés en anglais

Personnages, lieux, objets nommés, titres, peuples inventés et noms de boss ou de mécanique ne se traduisent pas. Quand le nom est un fragment seul (`{"text":"Wuggy"}`), la table porte une entrée
d'identité (`"Wuggy": "Wuggy"`) pour que le fragment ne soit pas compté « manquant » ; ce n'est pas obligatoire pour le jeu.

- **Clés protégées (jamais traduites, comparées par la carte)** : `Anchorblade`, `Eensy Sword`, `Imperishable Blade`, `Knowledge & Learning`,
  `Oath to Order`, `Taproot Sword`, `Ximglie` (7 noms), plus 88 clés techniques (nombres, ids `minecraft:`, base64 de têtes) : liste
  complète dans `protected.txt`. Ajouts manuels de ce lot : `Book of Naughty Secrets` (comparé dans le terrain), `NAME` et `TEXT`
  (gabarits d'écriture des PNJ botsicle, jamais exécutés).
- **Personnages (les plus fréquents)** : Wuggy (736), Gylvester (165), Pretzel Jenkins (64), Brendeloy (55), Slime Man, Germ Eater, Groveguard,
  Zephyr, Dungor, Dungorex, Whisper, Lord Morbex / Scourgelord Morbex / Morbex, Brain Cactus, Spoom-Ee IV (et III), Brainzo, Frogcrates,
  Moonlight Nexus, Pupu-Nini, Mayor Plubby, Phmlub, Guathman, Anglero, Clay More, Virus / World Virus, Lake Freak(s), Kraken Eye, Mindczar,
  Nirizhma, Wahrog, Moon Queen, King / Queen Glenman, Smilewalker, Squashly, Venna, Yommod, Igor, Weevo, Royroy... (les 1 444 clés courtes
  commençant par une majuscule sont presque toutes des noms : `todo_npc.jsonl`).
- **Titres** (351 occurrences pour « Lord ») : « Lord of Flame / Water / Smoke / Forest / Valor / Spores / Ice / Stone », « Dreadwarden of X »,
  « Supplicant of », « God of X » sont des noms : conservés en anglais, article compris quand il fait partie du titre (§6, q. 2). La phrase
  autour est traduite normalement.
- **Boss et mécaniques** : World Virus, Contagion, Nexus (Mind Nexus, Bone Nexus, Memory Nexus, Moonlight Nexus...), Bell of Life : conservés
  (§6, q. 4 et 13).
- **Lieux** : Floaty Isles, Dark Isles (conservés, §6, q. 3), Valor Tower, Worldgate, Magma Kingdom, Alabaster Pools, Bubble Lake, Dwarf City,
  Isle of Silence, Isle of Ice, Isle of Smoke, Warped Land, Moldsap Woods, Frostbolt Spire, Windbite Tundra, Tanglevine, Sticky Hollow,
  Shrunken Temple, Ember Depot, Sanctum of Petals, Serpent King's Tomb, Brain Mesa, Court of the Grengleshoft.
- **Objets nommés** : armes (Earthshard, Final Eclipse, Flamewaker, Mycobite, Prism's Edge, Tidebringer, Cosmic Dominance, Duality, Sovereignty,
  Starbinder, Voidmantle, Wintermaul, Pearlhammer, Necrosaber, Razorflint, Lurksaw, Ichorblight, Photalis, Smoldercap, Barnacleaver...),
  Blitzite, Tri-Aspect Amulet, Di-Aspect Amulet, Waxwane Brick, Seawater Orb, Weird Ring, Juice Chalice. Les noms d'objets du quotidien (Small
  Key, Ink Jar, Rock Scales, Adventure Notes, Diamond Gem, Tiny Chest...) sont aussi des noms d'objets : conservés (q. 7). Les 23 arcs « X Bow »
  (Golem Bow, Troll Bow, Pixie Bow...) et les armes de Wuggy : conservés (q. 8).
- **Peuples et créatures nommées au pluriel** (Gillmen, Glooblins, Pygmies, Botsicles, Froggadews, Valorites, Nightrobes, Cultists, Orcs,
  Abnormazoids, Glenfolk...) : conservés (noms de peuples inventés) ; seuls « dwarves / dwarf » (**nains**) et « Orcs » (**orcs**) sont des mots
  courants et se traduisent (q. 9). « Dwarf City » reste un nom de lieu.

## 4. Termes récurrents

Nombres = clés distinctes / occurrences qui contiennent le mot (extraction). Ne valent que pour le **nom commun** employé dans une phrase :
dès que le mot fait partie d'un nom (personnage, lieu, objet, titre, boss : §3), le nom entier reste en anglais.

| Anglais | Français proposé | Clés/occ. | Remarque |
|---|---|---|---|
| hero (vocatif) | héros | 123 / 198 | décidé (q. 1) |
| key | clé | 150 / 165 | nom commun en phrase ; « Small Key », « Secret Key » (noms d'objets) : conservés (q. 7) |
| secret | secret / secrète | 104 / 107 | adjectif : accord avec le nom |
| monster(s) | monstre(s) | 98 / 616 | |
| Lord of X, Dreadwarden of X, Supplicant of, God of X | (conservés) | 109 / 351 | titres = noms : restent en anglais (q. 2) ; « lord » seul, nom commun : seigneur |
| isle(s) | île(s) | 107 / 310 | « the Isles » seul : « les îles » ; « Floaty Isles », « Dark Isles » conservés (q. 3) |
| mind | esprit | 58 / 83 | « Mind Nexus » : nom propre, conservé |
| power | pouvoir | 59 / 65 | « puissance » pour la force brute |
| world | monde | 64 / 80 | « World Virus » conservé (q. 13) |
| bone | os | 57 / 80 | « Bone Nexus » conservé |
| dark | sombre | 53 / 174 | « Dark Isles » conservé (q. 3) |
| city | cité | 51 / 58 | « Dwarf City » conservé |
| life | vie | 49 / 67 | « Bell of Life » conservé (q. 4) |
| bow | arc | 55 / 233 | nom commun seul ; les 23 « X Bow » conservés (q. 8) |
| sword | épée | 22 / 162 | |
| blade | lame | 19 / 34 | |
| arrow | flèche | 27 / 34 | |
| scale(s) | écaille(s) | 46 / 215 | nom commun en phrase ; « Rock Scales » etc. (noms d'objets) conservés (q. 7) ; elemental = élémentaire(s) |
| shard | éclat | 4 / 12 | « A shard of frozen lightning » : Un éclat de foudre gelée |
| soul | âme | 22 / 117 | « soul of a » + monstre : « âme de » + nom du monstre en anglais (q. 5) |
| gem | gemme | 3 / 18 | nom commun en phrase ; « Diamond Gem » conservé (q. 7) |
| amulet | amulette | 3 / 6 | noms d'amulettes conservés |
| ring, orb, belt, mask, jar | anneau, orbe, ceinture, masque, pot | 14 / 33 | noms communs en phrase ; « Ink Jar », « Weird Ring » conservés (q. 7) |
| bell | cloche | 10 / 42 | « the Bell » dans une phrase : « la Cloche » ; « Bell of Life » conservé (q. 4) |
| chest | coffre | 8 / 12 | nom commun en phrase ; « Tiny Chest » conservé (q. 7) |
| book / notes | livre / notes | 50 / 70 | nom commun en phrase ; « Adventure Notes » conservé (q. 7) |
| potion | potion | 7 / 8 | Dragonbrews : conservé |
| spell / magic | sort / magie | 53 / 76 | |
| sigil | sceau | 15 / 19 | décidé (q. 6) |
| curse | malédiction | 10 / 10 | |
| oath | serment | 4 / 8 | décidé (q. 6) ; l'objet « Oath to Order » est protégé et reste anglais |
| dungeon | donjon | 10 / 10 | nom commun en phrase ; « Dungeon of the Lord of Flame » et consorts (noms de lieux) conservés |
| quest | quête | 37 / 37 | nom commun en phrase (titres d'advancements : traduction littérale, §6, q. 12) |
| tower / temple | tour / temple | 48 / 66 | noms propres conservés |
| forest / lake | forêt / lac | 44 / 111 | |
| kingdom / king / queen | royaume / roi / reine | 63 / 94 | noms communs ; « Moon Queen », « Magma Kingdom », « Queen Glenman » conservés |
| guild | guilde | 9 / 18 | « Gill Guild » conservé |
| golem, dragon | golem, dragon | 24 / 53 | |
| dwarf / dwarves | nain(s) | 76 / 92 | décidé (q. 9) ; « orc(s) » : orc(s) ; Gillmen, Glooblins... conservés |
| fairy, prophet, mayor | fée, prophète, maire | 19 / 41 | |
| flame / fire | flamme / feu | 25 / 74 | |
| water / ice | eau / glace | 43 / 107 | |
| stone / smoke / spore(s) | pierre / fumée / spore(s) | 71 / 138 | « Lord of Stone / Smoke / Spores » conservés (titres) |
| light | lumière | 15 / 18 | |
| eye / hand / heart | œil (yeux) / main / cœur | 61 / 96 | « Nacre Hearts », « Kraken Eye » (noms) conservés |
| memory | mémoire | 21 / 25 | « Memory Nexus » conservé |
| treasure | trésor | 8 / 8 | |
| friend / enemy | ami(e) / ennemi(e) | 41 / 125 | |
| fight / die / death | combattre / mourir / mort | 23 / 26 | |
| health / damage / strength / speed | santé / dégâts / force / vitesse | 16 / 17 | les stats du jeu (peu présentes : carte surtout narrative) |
| thanks | merci | 50 / 96 | « Thanks so much ! » : Merci beaucoup ! |
| talk to | parler à | 28 / 44 | panneaux « Talk to the » + nom : §5 |
| (right) click | (clic droit) / cliquer | 2 / 6 | « Right click to swap active mode » : Clic droit pour changer de mode |
| press the button | appuyer sur le bouton | 7 / 12 | impératif tutoiement : Appuie sur le bouton |
| step on / off | marcher sur / quitter | 7 / 13 | « Step on the bricks first! » : Marche d’abord sur les briques ! |
| use / find / help | utiliser / trouver / aider | 187 / 219 | impératif à la 2e personne du singulier (tutoiement) |
| ... bursting with energy | débordent d’énergie | 2 / 16 | lore des écailles |
| (étiquettes de locuteur) Narrator, Fortune Teller, Actor | Narrateur, Diseuse de bonne aventure, Acteur | | le rôle est traduit ; un nom propre ne change pas (q. 10) |

## 5. Phrases fragmentées (à surcharger dans `ctx.json` quand ce sera nécessaire)

La table traduit par fragment. Quand un même fragment anglais doit se traduire autrement selon la phrase (accord, ordre des mots), on
écrit `{"ns:fonction": {"fragment": "français"}}` dans `ctx.json` (prioritaire sur la table globale). Cas repérés, aucun écrit encore :

1. **Amélioration d'arme par Wuggy** (`npc:glooblin/wuggy/*`, 1 200 occurrences) : « Ta-tink! There you have it! Your » (600) + arme +
   « is now » (500) / « is now a » (100) + arme + « ! How exciting! Go ruin some monsters' days with it. » (480). Phrase française :
   « Ta-tink ! Et voilà ! Ton » + arme + « est maintenant » + arme + « ! Quelle joie ! Va gâcher la journée de quelques monstres avec. » ;
   problème : les noms d'armes restent anglais (q. 8), mais « Ton » / « ta » et « un » / « une » devant l'arme demandent un genre. Piste : une
   formulation sans article ni accord (« Ton arme : » + arme + « est maintenant » + arme). Reste ouvert, à régler avec la tranche pilote
   (surcharge par fonction dans `ctx.json`).
2. **Compas d'Abnormazoid** (`npc:gillmen/gylvester/abnormazoid`) : lore « It points toward » (159) / « somewhere in the » (148) / « Floaty
   Isles... » (83) / « Dark Isles... » (72) : trois lignes de lore qui se lisent bout à bout.
3. **Titres de donjon en lettres isolées** (`dungeon:*/start`, 154 occurrences) : le titre s'écrit lettre par lettre (« e », « l », « o »...) avec un
   effet de machine à écrire. Il n'y a pas de traduction possible clé par clé : ce sont des fragments d'un mot anglais. **À laisser en anglais**
   (ou à refaire à la main en lot ultérieur) ; les sous-titres complets (« Dungeon of the Lord of Flame »...) sont des noms de lieux : conservés.
4. **« The » + nom + suite** (46 occurrences, `npc:botsicle/*`, `boss:10/*`) : « The » seul est un fragment avant un titre (« The Lord of Ice
   has... »). Le titre reste anglais, « The » en fait partie quand il le précède ; le reste de la phrase se traduit (accord au cas par cas :
   surcharge par fonction).
5. **Réponses de quiz** (« A) », « B) » : 27 chacun, `game:firelight/script/*`, `game:quiz/*`) : lettres, identité.
6. **Panneaux « Talk to the » + nom** (`game:firelight/exit/*`, `npc:overworld_cutscene/*`, `boss:mini/*`) : la ligne 1 « Talk to the » et la ligne 2
   le rôle (« Actor », « Creature », « Mime »). « Parle à l’ » + « Acteur » : l’élision dépend du mot suivant : surcharge par panneau.
7. **« Contains the » + « soul of a: » + monstre** (`utility:abnormazoid_flag`, 18 + 38 occurrences) : phrase coupée sur trois lignes de lore : « âme de » + nom du monstre en anglais (q. 5).
8. **« Monsters from » / « Culling » + lieu** (`game:monstervatory/*`) : panneaux à deux lignes (« Monsters from » / lieu ; « Culling » / lieu).
9. **« Supplicant of » / « God of » + nom** (`main_quest:mlc/*`, 9 + 6 occurrences) : titre + nom propre, tous deux conservés (q. 2).
10. **Gabarits botsicle** (`npc:botsicle/botsicle_template`, « NAME » / « TEXT ») : marqueurs, protégés à la main.
11. **Textes techniques de têtes** : `Custom Head ID: 112395` et `www.minecraft-heads.com` (lore, 15 + 9 occurrences) : laisser en anglais.
12. **Barre de boss en petites capitales** : « xxx ᴡᴏʀʟᴅ ᴠɪʀᴜꜱ xxx » (`floaty:install`, 2 occurrences) : décoratif, conservé.

## 6. Décisions de Maxime (2026-10-30)

Règle d'ensemble : tout ce qui est un NOM reste en anglais, les noms communs se traduisent. Numérotation = celle des questions posées.

1. **« hero »** (vocatif) : « héros ».
2. **Titres** (« Lord of X », « Dreadwarden of X », « Supplicant of », « God of X ») : ce sont des noms, ils restent en anglais.
3. **Îles** : « Floaty Isles » et « Dark Isles » restent en anglais ; « the Isles » employé seul : « les îles ».
4. **Cloche** : « Bell of Life » reste en anglais ; « the Bell » dans une phrase : « la Cloche ».
5. **Âmes** : « soul of a » + monstre : « âme de » + nom du monstre en anglais.
6. **« sigil »** : « sceau » ; **« oath »** : « serment ». L'objet « Oath to Order » reste protégé, en anglais.
7. **Noms d'objets du quotidien** (Small Key, Ink Jar, Rock Scales, Adventure Notes, Diamond Gem, Weird Ring, Tiny Chest...) : ce sont des noms
   d'objets, ils restent en anglais.
8. **Les 23 « X Bow »** restent en anglais, comme les armes de Wuggy.
9. **Peuples** : Dwarves : « nains », Orcs : « orcs ». Les peuples inventés (Gillmen, Glooblins...) restent en anglais.
10. **Étiquettes de locuteur** (`<Narrator>`, `<Fortune Teller>`, `<Actor>`) : le rôle est traduit (« Narrateur », « Diseuse de bonne aventure »...) ;
    les noms propres ne changent pas.
11. **Onomatopées** : les actions sont adaptées (« *regarde ses notes* ») ; les sons purs (`*nuk-tuk*`, `bzzrt...`) restent tels quels.
12. **Titres d'advancements à jeux de mots** (« I forgor ☠ », « Smoke Doctor? I Hardly Know Her! », « Live, Laugh, Lovebug », « Every Day I'm
    Trufflin' ») : adaptation libre ; Maxime les vérifiera un par un pendant la tranche pilote. Les autres titres (96) : traduction littérale.
13. **« World Virus », « Contagion », « Nexus »** (noms de boss ou de mécanique) : restent en anglais.
14. **Points de suspension** : on garde `...` (pas de `…`).
15. **Entre PNJ** : tutoiement par défaut, vouvoiement envers les seigneurs et la reine.

Reste ouvert (pas une décision de Maxime) : l'accord de « Ton » / « un » devant un nom d'arme anglais dans la phrase de Wuggy (§5, cas 1), à
régler pendant la tranche pilote.
