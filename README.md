# ✦ Mini-Jeux Void — Datapack Minecraft 26.2 ✦

Neuf mini-jeux (et de nombreuses cartes / thèmes) prêts à jouer dans une **map vide**, avec lobby, menus cliquables, arènes construites automatiquement, équipes, scores et compteur de victoires.

**Version requise : Minecraft Java 26.2** (pack format 107). Pour une autre version, il suffira d'ajuster `min_format` / `max_format` dans `pack.mcmeta`.

---

## 🎮 Les jeux

| Jeu | Principe | Joueurs |
|---|---|---|
| **Spleef** | Casse la neige sous les pieds des autres à la pelle. De 1 à 4 étages selon le nombre de joueurs, murs invisibles tout autour, l'arène rétrécit après 40 s. Dernier debout gagne. | 2+ |
| **Parkour du lobby** | Parcours de 4 tronçons (≈100 blocs vers l’est, départ sur le plot émeraude à droite du lobby) : 3 checkpoints en lapis, arrivée sur le bloc diamant. Chrono (démarre quand on quitte le plot), compteur de chutes, retour au dernier checkpoint en cas de chute, records personnel et du lobby annoncés dans le chat. Utilisable entre deux parties ; abandon via `/trigger mg.opt set 11`. Reconstruction : `/function mg:parkour/build`. | 1+ |
| **Armurerie du lobby** | À l'ouest du spawn, 4 socles distribuent des armes **inoffensives** pour s'amuser : ⚡ pistolet laser (rayon de 30 blocs, la cible brille 3 s), ✦ baguette feu d'artifice (éclat dans le ciel), ☁ lance-vent (rafale de vent, chute ralentie automatiquement), ❄ lance-neige. Marcher sur un socle équipe l'arme (rechargée à 16 pour le vent et la neige) ; tout est retiré au lancement d'une partie. | tous |
| **Splegg** | Spleef aux œufs : clic droit pour tirer un œuf (munitions infinies) qui détruit instantanément la neige visée (portée 80 blocs, trajectoire en ligne droite avec traînée de neige). Les tirs croisés percent le plateau à toute vitesse ; dernier debout = gagnant. Plateau de 19 à 37 blocs de côté selon le nombre de joueurs, sur 3 étages de neige superposés (y 80 / 74 / 68) ; sous le dernier étage = éliminé. Murs invisibles sur les bords. | 2+ |
| **Splegg XXL** | Le Splegg en version géante : 3 grands plateaux de neige superposés (61×61, 53×53, 45×45) et chaque œuf détruit un cratère de 3×3 blocs. Tomber du premier étage donne une seconde chance, sous le dernier = éliminé. Pour de grosses parties. | 2+ |
| **Sumo** | Petite plateforme circulaire suspendue dans le vide (rayon 7 à 11 selon le nombre de joueurs). Tout le monde reçoit un bâton Knockback : aucun dégât, il faut éjecter les autres ! 3 vies chacun (affichées sous le pseudo), retour sur la plateforme après une chute, dernier debout = gagnant. | 2+ |
| **The Dropper : tube commun** | Même principe, mais tout le monde saute dans le MÊME grand tube (11×11, rebord de départ autour d'un trou 5×5, obstacles en couches colorées, un seul bloc d'eau au fond). Le premier à atterrir dans l'eau gagne la manche ; premier à 2 manches gagne. Pour jouer à plusieurs dans la même chute. | 2+ |
| **Sumo : arène complexe** | Version pour beaucoup de joueurs : grande île de rayon 15 avec une île centrale surélevée et 4 piliers, une douve (qui fait perdre une vie) franchissable par 4 ponts, et un anneau extérieur avec 4 bumpers en obsidienne. Mêmes règles (bâton Knockback, 3 vies). | 4+ |
| **The Dropper** | Chaque joueur a son puits vertical (6 dispositions d'obstacles tirées au hasard à chaque manche, couches de béton colorées avec des trous qui dérivent). Le joueur saute lui-même dans le trou central de son rebord de départ, puis chute en esquivant les couches pour atterrir dans l'unique bloc d'eau au fond ; toucher un obstacle ou le sol = retour en haut. Premier à 2 manches gagne (points affichés sous les pseudos). Gravité réduite pour pouvoir viser. 12 puits, tous construits d'avance. | 1+ |
| **One in the Chamber** | PvP rapide dans une petite arène (25×25, couverts en briques, murs invisibles). respawn illimité, une épée et un arc avec UNE seule flèche : un tir d'arc tue instantanément, chaque kill (arc ou épée) donne une flèche de plus. Une flèche de recharge est offerte après 5 s sans flèche. Respawn aléatoire avec 3 s de protection, le premier à 10 kills (compteur dans le sidebar) gagne. **Cartes** : classique 25×25 (id 26), **Château** 41×41 (donjon à étage, 4 tours à échelles, id 52, zone z 11700), **Grande forêt** 71×71 (collines, arbres, ruines, tours de guet, id 53, zone z 12000). **Flèches enchantées** : 1 kill sur 5 donne une flèche enchantée à la place d'une flèche normale, et toutes les 30 s un joueur tiré au sort en reçoit une — *explosive* (explose au contact, tue tout dans 3,5 blocs), *perforante* (traverse jusqu'à 4 joueurs), *révélatrice* (tous les adversaires brillent 6 s). | 2+ |
| **TNT Tag** | La patate chaude : un joueur au hasard porte une TNT sur la tête (lumineux, plus rapide). Il doit frapper un adversaire pour lui passer la bombe (1,5 s de protection pour l'ancien porteur). Quand le minuteur (affiché en bas de l'écran, de 15 à 30 s selon le nombre de survivants) tombe à zéro, la TNT explose et élimine son porteur, puis une nouvelle bombe est attribuée. Dernier survivant = gagnant. Aucun dégât. | 2+ |
| **Block Party** | Dance floor : un sol de 24×24 en béton de 16 couleurs (tuiles de 2×2, 10 dispositions aléatoires). Une couleur s'affiche dans ton inventaire (main secondaire + barre d'objets) et à l'écran : cours dessus avant la fin du minuteur, tous les autres blocs disparaissent et font tomber ceux qui sont dessus. Minuteur de 5 s qui descend de 0,25 s à chaque manche jusqu'à 2 s. Dernier debout = gagnant. | 2+ |
| **Pluie d'Enclumes** | Arène plate 21×21 : des enclumes tombent du ciel (une tache noire au sol prévient 1,5 s avant, une sur deux vise un joueur). Un impact tue. Toutes les 8 s la pluie s'intensifie : l'intervalle passe de 1,3 s à 0,15 s et jusqu'à 3 enclumes par tir. Dernier debout = gagnant. | 2+ |
| ↳ **Enclumes + sol troué** (id 42) | Même arène, mais en plus des trous 3×3 s'ouvrent régulièrement dans le sol : la zone vire au rouge 2 s, disparaît 6 s, puis le sol se referme. Le rythme s'accélère avec l'intensité (jusqu'à 3 trous à la fois). Tomber = éliminé. | 2+ |
| **Turf Wars** | Deux équipes (rouge / bleu) de part et d'autre d'une ligne de territoire : le terrain 31×25 est découpé en 31 colonnes (15 rouges, 1 neutre au centre, 15 bleues). Chaque flèche qui se plante dans une colonne adverse (ou neutre) la convertit à la couleur de ton équipe. Victoire en conquérant 28 colonnes sur 31 (90 %) — gros score affiché au centre de l’écran à chaque conquête —, ou à la majorité au bout de 6 min. Tableau Rouge/Bleu en sidebar. | 2+ |
| ↳ PvP Poussière | La carte **Poussière** (style Dust, 41×41) aussi en arène PvP : id 44 (kit classique) ou id 45 (avec classes). Dernier survivant gagne ; tomber dans le vide = éliminé. Zone z 11100 (partagée avec Quakecraft Poussière). | 2+ |
| ↳ PvP Mirage | La carte **Mirage** (style Mirage, 41×41) en arène PvP : id 47 (kit classique) ou id 48 (avec classes). Dernier survivant gagne ; tomber dans le vide = éliminé. Zone z 11300 (partagée avec Quakecraft Mirage). | 2+ |
| ↳ PvP Nuketown | La carte **Nuketown** (style Nuketown, 49×35 : maison verte et maison jaune face à face avec étage et escalier, bus et voitures dans la rue, jardins, haies, abris) en arène PvP : id 50 (kit classique) ou id 51 (avec classes). Zone z 11500 (partagée avec Quakecraft Nuketown). | 2+ |
| **Quakecraft** (8 cartes : menu → « Quakecraft : cartes ») | Arène 31×31 (pyramide centrale, piliers, murets). Chaque joueur a un railgun (champignon biscornu sur un bâton) : clic droit = rayon instantané, sans gravité, portée 70 blocs, arrêté par les blocs. Un tir qui touche élimine : la victime est spectatrice 3 s puis réapparaît ailleurs avec 3 s d’invincibilité. Rechargement 1,1 s. Premier à 25 kills gagne, sinon le meilleur après 8 min (égalité = nul). Kills en sidebar ; séries de kills annoncées à tous (Killing Spree 3, Rampage 5, Dominating 7, Unstoppable 10, Godlike 15), série perdue à la mort. **Grenade rare** : 1 chance sur 5 d’en gagner une après un kill (une à la fois, perdue à la mort) — clic droit pour la lancer, elle explose à l’impact (0,5 s) et tue tous les joueurs à moins de 4,5 blocs, sauf le lanceur. | 2+ |
| ↳ cartes Quakecraft | **Néon** (31×31, quartz, id 31) · **Volcan XL** (61×61 thème Nether, id 32, 30 kills, 10 min) · **Jungle XL** (61×61 ruines de jungle, id 33, 30 kills, 10 min) · **Désert** (31×31, temple, id 34) · **Glacier mini** (19×19, id 35, 20 kills, 6 min) · **Poussière** (41×41, style Dust : spawn T au sud, spawn CT au nord, Long A, Mid et ses portes, Short/Catwalk, tunnels B, sites A et B ; id 43, 20 kills, 6 min) · **Mirage** (41×41, style Mirage : spawn T au sud, spawn CT au nord, Appartements et balcon vers B, Mid avec Fenêtre et Marché, Jungle, Short/Catwalk, Rampe, site A avec Palace ; id 46, 20 kills, 6 min) · **Nuketown** (49×35, maisons verte et jaune à étage, bus, voitures, jardins et abris ; id 49, 20 kills, 6 min). Zones : z 7300 / 7600 / 7900 / 8200 / 8500 / 11100 / 11300 / 11500. | 2+ |
| **Paintball** (style Splatoon) | Orange contre Bleu dans une arène 49×61 en béton blanc (murs, plateformes et couverts compris). Pistolet à peinture (clic droit maintenu, 5 tirs/s) : l'impact peint un cube 3×3×3 à ta couleur, en repeignant aussi la peinture adverse. Consomme de l'encre (barre dans l'actionbar) qui se recharge 3× plus vite sur sa propre peinture, où l'on court plus vite ; sur la peinture ennemie on est ralenti. 3 touches = éclaboussé : grosse flaque ennemie sous les pieds et retour à la base (2 s d'invincibilité). Après 4 min, le plus de terrain peint gagne. Sidebar : % Orange / % Bleu / temps. **Cartes** : classique 49×61 (id 36, 4 min), **Mini-terrain** 31×41 (id 54, 3 min, zone z 12300), **Grand terrain** 81×101 (id 55, 6 min, zone z 12700). | 2+ |
| **Course de bateaux sur glace** | Circuit de glace compacte d'environ 300 blocs (virages larges et chicane), murs en béton bleu clair. Chaque joueur est placé dans un bateau sur la grille de départ (portillon qui s'ouvre au GO). 3 tours, 10 points de passage par tour à valider dans l'ordre ; le premier à finir gagne (sinon, au bout de 4 min, le plus avancé). Sidebar : progression en %. Un joueur qui quitte son bateau y est remis ; tombé hors piste, il repart du dernier point de passage. Zone z 13200 (id 56). | 2+ |
| **Build Battle** (2 modes : menu → « Build Battle ») | Chaque joueur reçoit une parcelle 25×25 (herbe, bordure de pierre, 12 max) et passe en **créativité** pendant 4 minutes pour construire le thème annoncé (barre d'action : thème + temps). Il ne peut pas quitter sa parcelle (retour automatique au centre). Ensuite chaque construction est présentée 18 s (anonyme, les joueurs passent en spectateur pour la visiter) et **tous les autres joueurs la notent de 1 à 5** (fenêtre automatique à 12 s, boutons cliquables dans le chat ou `/trigger mg.bb set 1..5`). La meilleure moyenne gagne (égalité = plusieurs vainqueurs) ; classement détaillé avec les pseudos à la fin. **Mode 57 : thème aléatoire** (≈ 150 objets/choses tirés d'une liste). **Mode 58 : Maître du mot** : un joueur tiré au sort (ou désigné avec `/tag <joueur> add mg.bmx` avant le lancement) ne construit pas : il a 60 s pour donner le thème, soit en écrivant le mot dans son livre (1re page, « Terminé » puis « Valider mon livre »), soit en cliquant une des 8 idées proposées, soit en tirant un mot au hasard ; sans réponse, le thème est tiré au sort. Il note ensuite avec les autres. Mode 58 : 3 joueurs minimum (sinon thème aléatoire). Zone z 13640 à 13768 (studio + 12 parcelles). | 2+ |
| **Mob Arena XL** (5 thèmes à 20 vagues, ids 37 à 41 : menu → « Mob Arena : thèmes ») | **Cathédrale maudite** (nef gothique, galeries d'archers, chauves-souris Wither ; boss *Comte de Sang* : téléportation dans le dos + life-steal, puis invisible 10 s + nuées de vexes) · **Laboratoire alchimique** (cuivre et fer, zombies Speed II, sorcières, creepers chargés ; boss *Abomination Toxique* : nuages de peste persistants, puis bouclier à lever en brisant 4 alambics) · **Temple des profondeurs** (prismarine inondée ; noyés au trident, gardiens ; boss *Émissaire du Kraken* : rayon laser + répulsion, puis 8 tentacules à abattre) · **Forge du Titan** (colisée de pierre noire bordé de lave qui monte aux vagues 6/11/16 ; boss *Golem de Basalte* : ondes de choc, puis météorites) · **Vaisseau cybernétique** (hangar de quartz ; shulkers, phantoms ; boss *Cœur I.A.* : gravité inversée, puis cage brisée + têtes de Wither + endermen). Zones z 9100 / 9500 / 9900 / 10300 / 10700. Bonus aux vagues 5/10/15. | 1+ |
| **TNT Run** | Le sol s'efface (rouge → orange → vide, ~1 à 1,5 s) là où tu marches. 3 étages avant le vide, murs invisibles sur les côtés. | 2+ |
| **Arène PvP** | Chacun pour soi, kit fer + arc + pommes d'or. Dernier survivant gagne. | 2+ |
| **Arène PvP : classes** | Même arène et mêmes règles que le PvP (pas de régénération, soin sur KILL), mais chacun choisit sa classe d'équipement pendant le compte à rebours : Guerrier, Archer, Tank, Assassin, Mage, Pyromane. | 2+ |
| **Bedwars** | 2 à 4 équipes, générateurs fer/or/diamant, boutique, détruis les lits ennemis ! | 2 à 8+ |
| **Sheep War** | Catapulte des moutons explosifs sur l'équipe adverse, le sol part en morceaux. Grandes plateformes ; moins de moutons quand il y a du monde ; joueurs plus résistants aux explosions ; le mouton explose 1,5 s après avoir atterri. | 2+ |
| **Sheep War 2 : Forteresses** | Mêmes règles que Sheep War, mais chaque camp est une forteresse : mur de façade avec porte et meurtrières, couverts, mezzanine sur piliers, deux escaliers, tour creuse à étage avec créneaux. Dur de viser, facile de se cacher ! | 2+ |
| **Sheep War 3 : Bastions** | Version compacte de Forteresses (plateformes 20×31, une mezzanine, une petite tour, deux escaliers) : pour peu de joueurs ou pour varier. | 2+ |
| **Sheep War 4 : Cubes Voxel** | Deux cubes de 20×20×20 suspendus dans le vide (23 blocs d'écart), 3 étages en grès / concrete, échelles au fond, grandes ouvertures face à face (14 blocs) : départ au dernier étage, les moutons creusent des ouvertures nettes. | 2+ |
| **Sheep War 5 : Pyramides Inversées** | Deux pyramides pointe en bas, surface plate au sommet : le terrain se rétrécit vers le vide à chaque impact. | 2+ |
| **Sheep War 6 : Archipel Bicolore** | Deux demi-sphères face à face : feu (netherrack / terracotta rouge) contre glace (neige / glace compacte). | 2+ |
| **Sheep War 7 : Double Canyon** | Deux blocs de terrain séparés par une crevasse de lave : falaise droite côté centre pour les tirs directs, pente douce à l'arrière pour se couvrir. | 2+ |
| **Sheep War 8 : Nuages Voxel** | Plateformes flottantes de gros blocs de laine, concrete et quartz : la laine résiste mal, la destruction est spectaculaire. | 2+ |
| **Mob Arena** | Coop : survivez à 10 vagues de monstres, boss final « LE DÉVOREUR ». Soin instantané + repas à chaque vague réussie, les joueurs tombés reviennent au début de la vague suivante ; scoreboard à droite (vague X / 10, monstres restants, joueurs en vie) et barre de vie de boss en haut de l'écran ; en Ultra Hard les joueurs sont boostés (diamant enchanté, Force, Vitesse, +PV). **5 thèmes en plus du classique** : Nether, End, Ultra Hard, Volant, Araignée (menu → « Mob Arena : thèmes »), chacun avec son décor, ses monstres et ses boss. **Classes** (tous les thèmes sauf Ultra Hard) : Guerrier, Archer, Tank, Assassin, Mage (soigneur), Pyromane (boules de feu), Berserker (hache), Poséidon (trident) — fenêtre de choix (comme le PvP classes, avec repli sur une liste cliquable dans le chat) au lancement, changement possible pendant les pauses (`/trigger mg.cls set 1..8`, 9 = rouvrir la liste). Bouclier et vision nocturne pour tous. Quand il reste 3 monstres ou moins, ils sont surlignés (visibles à travers les murs). | 1+ |

Tout se lance depuis un menu cliquable — aucun bloc de commande, aucune construction manuelle.

---

## 🗺️ 1. Créer la map vide (solo / LAN)

1. **Nouveau monde** → Onglet **Monde** → Type de monde : **Superflat** (Ultra-plat).
2. Clique **Personnaliser** → **Préréglages** → choisis **Le Néant** (*The Void*).
3. (Conseillé) Difficulté : **Normale**, mode **Créatif** pour l'installation.
4. Toujours dans l'écran de création : **Packs de données** → glisse le fichier `minijeux_void_26.2.zip` dans la fenêtre → active-le → crée le monde.

> Datapack dans un monde existant : copie le zip dans `<monde>/datapacks/` puis fais `/reload`.

## 🖥️ 1 bis. Sur un serveur dédié

Le plus simple : crée le monde en solo comme ci-dessus (avec le datapack), puis copie le dossier du monde sur le serveur (`level-name` dans `server.properties`). Le datapack voyage avec le monde dans `world/datapacks/`.

## ⚙️ 2. Installer (une seule commande)

Une fois dans le monde, un joueur **OP** tape :

```
/function mg:setup
```

Le datapack construit alors **tout** : lobby, les 9 arènes, règles de jeu, spawn. C'est prêt en ~5 secondes. Celui qui lance la commande devient **admin** et reçoit l'objet **≡ MENU** ; les autres joueurs sont simplement téléportés au lobby.

Pour nommer d'autres admins : `/function mg:admin` (en étant OP) ou `/tag <joueur> add mg.admin`.

Optionnel : `/function mg:nettoyer_plateforme` efface la petite plateforme de départ du préréglage « Le Néant ».

## ▶️ 3. Jouer

- **Clic droit sur ≡ MENU** (la carotte dorée, réservée aux admins) → choisis un jeu → tout le monde est téléporté, compte à rebours de 10 s, GO !
- Objet perdu ? `/trigger mg.menu` rouvre le menu (admins).
- Fin de partie automatique : célébration, +1 victoire au gagnant, retour au lobby.
- **Vote des joueurs** : les non-admins ont à la place un objet **☑ VOTE** (vert, hotbar) ou `/trigger mg.menu` : une fenêtre propose 20 jeux (un vote par joueur, modifiable ou retirable). Les votes s'affichent dans le tableau latéral du lobby et les admins sont prévenus à chaque vote. L'admin peut ensuite choisir lui-même, ou utiliser **☑ Votes : lancer le plus voté** dans son menu (égalité : tirage au sort entre ex æquo). Les votes sont effacés au lancement d'une partie.
- Les non-admins peuvent toujours se mettre en spectateur (`/trigger mg.opt set 1`) et afficher le classement (`/trigger mg.opt set 2`).

### Dans le menu

- **Mode spectateur ON/OFF** : ne plus participer aux parties (ou abandonner celle en cours).
- **Classement des victoires** : affiche/masque le tableau des scores à droite.
- **⛔ Arrêter la partie** : stoppe la partie en cours (admins) — marche aussi en plein Bedwars ou en mode test.

### Spécial Bedwars

Chaque île a son **VILLAGEOIS BOUTIQUE** : fais un clic droit dessus pour échanger comme au village — laine, épées, arc, pomme d'or, briquet, TNT, perle d'ender — en voyant ton inventaire. Le fer et l'or apparaissent sur ta plaque dorée, les diamants sur l'île centrale. Tant que ton lit existe, tu réapparais — mais **mourir fait perdre ressources et achats** (tu repars avec le kit de base) !

---

## 🔧 Commandes utiles

| Commande | Effet | Qui |
|---|---|---|
| `/function mg:aide` | Récapitulatif en jeu | tous (via OP) |
| `/function mg:admin` | Devenir admin des mini-jeux (reçoit ≡ MENU) | OP |
| `/function mg:setup` | Installe / reconstruit tout | OP |
| `/function mg:nettoyer_plateforme` | Efface la plateforme du préréglage | OP |
| `/function mg:desinstaller` | Retire scoreboards, équipes, zones chargées | OP |
| `/trigger mg.menu` | Ouvre le menu (fenêtre) | admins |
| `/trigger mg.menu set 2` | Ouvre le menu **texte** cliquable (plan B) | admins |
| `/function mg:menu` | Ouvre le menu sans objet ni trigger | admins/OP |
| `/function mg:diag` | Diagnostic du menu (✔/✖) | admins/OP |
| `/trigger mg.go set 1..7` | Lance un jeu (1 Spleef, 2 TNT Run, 3 PvP, 4 Bedwars, 5 Sheep War, 6 Mob Arena, 7 Sheep War 2) | admins |
| `/trigger mg.go set 14` | Sheep War 3 : Bastions (petite carte) | admins |
| `/trigger mg.go set 15..19` | Sheep War 4..8 : 15 Cubes Voxel, 16 Pyramides Inversées, 17 Archipel Bicolore, 18 Double Canyon, 19 Nuages Voxel | admins |
| `/trigger mg.opt set 8` | Ouvre le sous-menu « Sheep War : cartes » | admins |
| `/trigger mg.go set 20` | Splegg | admins |
| `/trigger mg.go set 21` | Splegg XXL | admins |
| `/trigger mg.go set 22` | Sumo | admins |
| `/trigger mg.go set 23` | The Dropper | admins |
| `/trigger mg.go set 24` | Sumo : arène complexe | admins |
| `/trigger mg.go set 25` | The Dropper : tube commun | admins |
| `/trigger mg.menu` (non-admin) | Ouvre la fenêtre de vote (objet « ☑ VOTE » de la hotbar) | tous |
| `/trigger mg.vote set 1..20` | Vote pour un jeu (98 = voir les votes, 99 = retirer son vote) | tous |
| `/trigger mg.opt set 12` / `13` | Lancer le jeu le plus voté / réinitialiser les votes | admins |
| `/trigger mg.go set 26` / `52` / `53` | One in the Chamber : classique / Château / Grande forêt | admins |
| `/trigger mg.go set 27` | TNT Tag | admins |
| `/trigger mg.go set 28` | Block Party | admins |
| `/trigger mg.go set 29` | Pluie d'Enclumes | admins |
| `/trigger mg.go set 30` | Turf Wars | admins |
| `/trigger mg.go set 31` | Quakecraft | admins |
| `/trigger mg.go set 32` … `35` | Quakecraft Volcan XL / Jungle XL / Désert / Glacier mini | admins |
| `/trigger mg.go set 43` / `46` / `49` | Quakecraft Poussière (style Dust) / Mirage / Nuketown | admins |
| `/trigger mg.go set 44` / `45` / `47` / `48` / `50` / `51` | PvP Poussière / Mirage / Nuketown (classique / classes) | admins |
| `/trigger mg.go set 36` / `54` / `55` | Paintball : classique / Mini-terrain / Grand terrain | admins |
| `/trigger mg.go set 56` | Course de bateaux sur glace | admins |
| `/trigger mg.go set 57` / `58` | Build Battle : thème aléatoire / Maître du mot | admins |
| `/trigger mg.bb set 1..5` | Noter la construction affichée (Build Battle) | tous |
| `/trigger mg.bw set 1` / `2` / `3` / `11..18` | Maître du mot : valider le livre / mot aléatoire / nouvelles idées / choisir l'idée n° | Maître |
| `/trigger mg.go set 37` … `41` | Mob Arena XL : Cathédrale / Laboratoire / Temple / Forge / Vaisseau | admins |
| `/trigger mg.go set 42` | Pluie d'Enclumes + sol troué | admins |
| `/trigger mg.go set 13` | Arène PvP à classes | admins |
| `/trigger mg.cls set 1..6` | Choisir sa classe pendant le compte à rebours (1 Guerrier, 2 Archer, 3 Tank, 4 Assassin, 5 Mage, 6 Pyromane ; 9 = rouvrir le menu) | joueurs |
| `/trigger mg.opt set 7` | Menu des thèmes de Mob Arena | admins |
| `/trigger mg.go set 8..12` | Mob Arena thème : 8 Nether, 9 End, 10 Ultra Hard, 11 Volant, 12 Araignée | admins |
| `/trigger mg.opt set 9` | Arrête la partie en cours | admins |
| `/trigger mg.opt set 1` | Mode spectateur ON/OFF | tous |

## 📝 Bon à savoir

- **Déconnexion / reconnexion** : si aucune partie n'est en cours, le joueur est renvoyé au lobby, inventaire vidé. Si une partie est en cours, il est téléporté dans le jeu en **spectateur** (sans inventaire) et retourne au lobby à la fin. Il n'est jamais réintégré comme joueur.
- **Bedwars** : le point de réapparition est réimposé à chaque mort (cliquer sur un lit ne le modifie plus) et le joueur est replacé sur son île.
- **Sheep War, murs et moutons** : toutes les arènes Sheep War sont entourées de murs invisibles (barrières de y 45 à 231 + plafond) pour que les moutons « perdus » retombent dans la carte ; les moutons sont invulnérables et insensibles au recul des explosions.
- **Sheep War, moutons spéciaux** : chaque type a son **propre objet** (donc sa propre pile) avec nom, couleur et description — regarde ce que tu tiens en main : Mouton-Fusée (poudre, normal), *espace* (éclat d'améthyste : lévitation 3 s puis explosion), *nauséeux* (boule de slime : nausée 10 s), *glacé* (cristal de prismarine : bloqué 3 s), *ténèbres* (charbon : cécité 6 s), *feu* (poudre de blaze : tapis de flammes 5 s). Trois moutons très explosifs : *super explosif* (poudre de glowstone : explose dès l'atterrissage, puissance 5), *mitraillette* (pépite de fer : 3 explosions espacées de 0,3 s, insensible à ses propres explosions) et *ULTRA explosif* (étoile du Nether : mèche de 2,5 s, explosion de puissance 9, plus du double du TNT normal de 4). Au départ : stock de moutons normaux + 1 spécial au hasard ; à chaque recharge, 40 % de chances de recevoir un spécial. Le normal, celui de l'espace, le super et l'ultra explosent. Chances à chaque recharge de spécial : 1/9 pour chacun des 5 effets, 2/9 super, 1/9 mitraillette, et seulement 1/27 pour l'ultra (sinon mouton normal).
- **Affichage des PV** : les points de vie de chaque joueur sont visibles par tous, en cœurs dans la liste des joueurs (Tab) et en nombre sous le pseudo. En Sumo, ce sont les vies restantes qui s'affichent à la place.
- **Sheep War, soin** : plus de saturation infinie ni de régénération naturelle ; un petit soin de 2 cœurs toutes les 12 s.
- **TNT Run** : les blocs piétinés disparaissent entre 9 et 18 ticks plus tard (encore plus rapide).
- **Sheep War (1 et 2)** : 1 s de délai entre deux lancers ; un lancer trop rapide ne consomme pas le mouton.
- **PvP classes** : *Guerrier* (fer, épée, bouclier), *Archer* (arc Puissance III + Recul, 40 flèches, rapide), *Tank* (diamant, +4 cœurs, bouclier, plus lent), *Assassin* (cuir noir, très rapide, épée tranchante, 2 perles d'Ender), *Mage* (potions jetables : dégâts, ralentissement, soin), *Pyromane* (mailles, épée et arc enflammés, immunisé au feu). Sans choix : Guerrier.
- **Arène PvP** : le bouclier est incassable ; plus de saturation ni de régénération naturelle — on ne se soigne que sur **KILL** (+4 cœurs) ou avec les pommes d'or.
- **Mob Arena, chat** : à chaque vague, annonce dans le chat général (n° de vague, composition, boss), « plus que N monstres » quand il en reste 3 ou moins, bilan de vague nettoyée, message de mi-parcours à la vague 5.
- **Thèmes Mob Arena** : *Nether* (piglins, blazes, hoglins, Capitaine Calciné v5, Roi Piglin v10), *End* (endermites, endermen, shulkers, phantoms, le Veilleur v5, l'Ombre du Vide v10), *Ultra Hard* (monstres armurés et boostés vitesse/force/résistance, soin réduit, le Broyeur v5, le Warden v10), *Volant* (phantoms, vex, blazes, ghasts, la Pleureuse v5, le Seigneur des Cieux v10), *Araignée* (araignées, cave spiders, jockeys, toiles, la Reine Araignée v5, l'Arachnarque v10). Pendant une Mob Arena, les monstres ne détruisent plus l'arène.
- **Sheep War** : plateformes plus grandes (la zone est rechargée à chaque `/reload`) ; stock de moutons de départ 12 / 8 / 6 / 4 selon la taille de la plus grande équipe (1 / 2 / 3-4 / 5+).

- Le datapack règle automatiquement : jour permanent, pas de météo, pas de spawn de monstres sauvages, inventaire conservé à la mort, pas de dégâts de chute, pas de drops de blocs (la neige du Spleef ne pollue pas l'inventaire).
- Les arènes sont espacées de 300 blocs le long de l'axe Z (lobby en 0/0, Spleef en z=300, TNT Run 600, PvP 900, Bedwars 1200, Sheep War 1500, Mob Arena 1800, Sheep War 2 en 2100, Sheep War 3 en 2400, puis Sheep War 4 à 8 en 2700 / 3000 / 3300 / 3600 / 3900, Splegg en 4200, Splegg XXL en 4600, Sumo en 4900, The Dropper en 5200, Sumo complexe en 5500, One in the Chamber en 5800, TNT Tag en 6100, Block Party en 6400, Pluie d'Enclumes en 6700, Turf Wars en 7000, Quakecraft en 7300, 7600, 7900, 8200 et 8500, Paintball en 8800, Mob Arena XL en 9100 / 9500 / 9900 / 10300 / 10700) et maintenues chargées en permanence (`forceload`) — c'est léger, ce sont des zones vides.
- Les arènes sont **remises à neuf automatiquement** avant chaque partie (sol du Spleef/TNT Run, ponts de Bedwars effacés, etc.).
- Un joueur qui rejoint en cours de partie attend au lobby ; il sera inclus dans la partie suivante.
- Partie lancée seul = **mode test** (pas de victoire automatique) — pratique pour visiter les arènes. Arrêt via le menu.
- Le compteur de **victoires est conservé** entre les sessions.

## 🛠 Dépannage (serveur Paper / Spigot / autre)

1. Le zip doit rester **zippé tel quel** dans `<monde>/datapacks/` (ou dossier décompressé contenant `pack.mcmeta` à la racine), puis `/reload`.
2. Si le menu ne s'ouvre pas : `/function mg:menu`, puis `/function mg:diag` et regarde les ✔/✖.
3. Si la fenêtre n'apparaît pas, le **menu texte cliquable** s'affiche automatiquement (ou `/trigger mg.menu set 2`).
4. Des plugins (EssentialsX, etc.) peuvent remplacer des commandes vanilla (`/give`, `/tp`, `/summon`…) ; teste sans eux en cas de doute et consulte `logs/latest.log` du serveur.

Amusez-vous bien ! 🎉
