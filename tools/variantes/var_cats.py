"""Catégories du menu principal (❄ Jeux de sol, ⚑ Équipes…) : titre, couleur, texte, boutons, catégorie parente.
(Combat : pvp.json, réécrit par var_menus.)

Pur : build(known) ne fait que construire les données ; known() (var_menus) doit lire un KNOWN déjà rempli.
"""
from var_common import act

OPEN = lambda o: f'trigger mg.opt set {o}'


def build(known):
    """CATS : clé → (titre, couleur, texte, actions, parent)."""
    return {
        'sols': ('❄ Jeux de sol', 'aqua', 'Casse, cours, pousse : le dernier debout gagne.', [
            act('❄ Spleef ▸', 'aqua', OPEN(37), 'Casse la neige sous les autres'),
            act('✷ TNT Run ▸', 'red', OPEN(38), 'Le sol disparaît sous tes pas'),
            known(OPEN(17), '❍ Splegg ▸', 'yellow'), known(OPEN(18), '✊ Sumo ▸', 'gold'),
            known('trigger mg.go set 28', '▦ Block Party', 'light_purple'),
            act('▦ Block Party — bandes', 'light_purple', 'trigger mg.go set 91', 'Le sol est fait de bandes de couleur'),
            act('▦ Block Party — mixte', 'light_purple', 'trigger mg.go set 92', 'Carrés ou bandes, ça change à chaque manche'), known(OPEN(20), '⚓ Pluie d\'Enclumes ▸', 'dark_gray')], 'menu'),
        'equipes': ('⚑ Équipes', 'light_purple', 'Jeux en équipes.', [
            act('⚑ Bedwars ▸', 'light_purple', OPEN(30), 'Protège ton lit, détruis les autres'),
            act('☁ Sheep War ▸', 'white', OPEN(8), 'Moutons explosifs, 8 cartes'),
            known(OPEN(21), '▓ Paintball ▸', 'gold'), known('trigger mg.go set 30', '▮ Turf Wars', 'gold'),
            act('🏰 The Towers', 'gold', 'trigger mg.go set 88', 'Saute dans le puits adverse, 5 points pour gagner'),
            act('🚚 Convoi', 'gold', 'trigger mg.go set 89', 'Escorte ou bloque le convoi, 2 manches'),
            act('🚚 Convoi — coop', 'green', 'trigger mg.go set 90', 'Tous ensemble contre les monstres'),
            act('🚩 Capture the Flag ▸', 'gold', OPEN(58), 'Ramène le drapeau adverse sur ton socle — Prairie, Nether, Banquise')], 'menu'),
        'courses': ('🏁 Courses et vol', 'gold', 'Le premier arrivé gagne.', [
            act('🏎 Kart ▸', 'gold', OPEN(46), 'Circuit Champignon, Royaume Koopa, Bataille'),
            known('trigger mg.go set 56', '⛵ Course de bateaux (glace)', 'aqua'),
            known(OPEN(28), '🪽 Course d\'élytres ▸', 'aqua'), known(OPEN(31), '🪽 Élytra ▸', 'aqua'),
            known(OPEN(19), '⬇ The Dropper ▸', 'aqua')], 'menu'),
        'arcade': ('🕹 Arcade', 'light_purple', 'Jeux d’adresse et de stratégie.', [
            act('⚡ Tron ▸', 'aqua', OPEN(50), 'À pied ou à moto, arène normale ou XXL'),
            act('👑 King of the Hill ▸', 'gold', OPEN(51), 'Solo ou équipes, 3 cartes'),
            act('⛏ Mini UHC Run ▸', 'gold', OPEN(52), '5 min : farm, PvP, zone qui rétrécit — 3 cartes'),
            act('🏹 Mini Hunger Games ▸', 'gold', OPEN(53), 'Coffres, corne d\'abondance — 3 cartes'),
            act('🧟 Zombies ▸', 'dark_green', OPEN(54), 'Coop, armes réelles, 10 manches — 3 cartes'),
            act('🧪 Infection ▸', 'green', OPEN(55), 'Survivants contre zombies contagieux — 3 cartes'),
            act('🎭 Prop Hunt', 'gold', 'trigger mg.go set 96', 'Cache-toi en objet, ou trouve les objets qui bougent'),
            act('💣 Bombardier', 'red', 'trigger mg.go set 99', 'Bombarde la ville du ciel, le plus de dégâts gagne, 2 min 30'),
            act('🦎 Meccha Chameleon', 'green', 'trigger mg.go set 198', 'Peins-toi aux couleurs du décor et cache-toi, ou chasse les caméléons'),
            act('🔴 1, 2, 3 Soleil', 'red', 'trigger mg.go set 220', 'Façon Squid Game : avance dos tourné, fige-toi quand la poupée regarde'),
            act('🚗 Autos tamponneuses ▸', 'aqua', OPEN(57), 'Bateaux sur la glace : tamponne, ne te fais pas tamponner'),
            act('🟩 Slime Jump', 'green', 'trigger mg.go set 224', 'Parkour de rebonds sur slime, le premier arrivé gagne'),
            act('🙈 Labyrinthe aveugle', 'light_purple', 'trigger mg.go set 225', 'Par paires : le marcheur est aveugle, le guide le dirige d\'en haut (au vocal)'),
            act('👑 Master dit', 'gold', 'trigger mg.go set 226', 'Ordres ultra rapides ; sans « Master dit », c\'est un piège !'),
            act('🔪 Murder Mystery', 'red', 'trigger mg.go set 227', 'Un tueur caché, un détective armé : démasquez-le avant qu\'il ne vous élimine tous'),
            act('💣 Bomberman', 'red', 'trigger mg.go set 239', 'Pose des bombes, casse les briques, ramasse les bonus : dernier debout gagne (2 à 8)'),
            act('💣 Bomberman — équipes', 'red', 'trigger mg.go set 240', 'Rouges contre bleus : la dernière équipe debout gagne'),
            act('🌀 Labyrinthe géant', 'light_purple', 'trigger mg.go set 241', 'Course dans un labyrinthe de 100 × 100 : bonus, pièges, grilles, téléporteurs'),
            act('🎾 Wii Sports ▸', 'aqua', OPEN(56), 'Bowling, golf, tennis : chacun sa piste')], 'menu'),
        'autotamp': ('🚗 Autos tamponneuses', 'aqua', 'Choisis le nombre de coups avant d\'être éliminé.', [
            act('🚗 3 coups', 'red', 'trigger mg.go set 222', 'Partie courte et brutale'),
            act('🚗 5 coups', 'aqua', 'trigger mg.go set 221', 'Le classique'),
            act('🚗 8 coups', 'green', 'trigger mg.go set 223', 'Partie longue')], 'arcade'),
        'wii': ('🎾 Wii Sports', 'aqua', 'Chacun sa piste, tout le monde joue en même temps.', [
            act('🎳 Bowling', 'light_purple', 'trigger mg.go set 214', '8 pistes, 5 frames, vraies règles (strike, spare)'),
            act('⛳ Golf', 'green', 'trigger mg.go set 215', '6 trous (par 23), chacun sa balle, le moins de coups gagne'),
            act('🎾 Tennis', 'yellow', 'trigger mg.go set 216', '1 contre 1 sur 4 courts (robot si joueur impair), 3 jeux gagnants')], 'arcade'),
        'tron': ('⚡ Tron', 'aqua', 'Choisis le mode et l\'arène.', [
            act('⚡ Tron à pied', 'aqua', 'trigger mg.go set 84', 'Arène 101×101 dans la pénombre'),
            act('🏍 Tron moto', 'gold', 'trigger mg.go set 85', 'À cheval, saut toutes les 20 s'),
            act('⚡ Tron à pied — XXL', 'aqua', 'trigger mg.go set 200', 'Arène géante 201×201'),
            act('🏍 Tron moto — XXL', 'gold', 'trigger mg.go set 201', 'Arène géante 201×201, à cheval')], 'arcade'),
        'ctf': ('🚩 Capture the Flag', 'gold', 'Rouge contre Bleu, 3 captures. Choisis la carte.', [
            act('🚩 Prairie', 'green', 'trigger mg.go set 93', 'Ravin à 3 ponts, tours de guet, tunnels'),
            act('🚩 Nether', 'red', 'trigger mg.go set 242', 'Même plan, ravin de lave, sol des forêts du Nether'),
            act('🚩 Banquise', 'aqua', 'trigger mg.go set 243', 'Même plan sur la neige : ravin gelé, allées de glace qui glissent')], 'equipes'),
        'koth': ('👑 King of the Hill', 'gold', 'Solo ou équipes, choisis la carte.', [
            act('👑 Solo — Colline', 'gold', 'trigger mg.go set 86', 'Colline en gradins, 60 points'),
            act('👑 Équipes — Colline', 'red', 'trigger mg.go set 87', 'Rouge contre Bleu, 90 points'),
            act('👑 Solo — Pyramide', 'gold', 'trigger mg.go set 206', 'Pyramide de grès dans le sable'),
            act('👑 Équipes — Pyramide', 'red', 'trigger mg.go set 207', 'Pyramide de grès, Rouge contre Bleu'),
            act('👑 Solo — Glacier', 'gold', 'trigger mg.go set 208', 'Colline de glace : ça glisse !'),
            act('👑 Équipes — Glacier', 'red', 'trigger mg.go set 209', 'Glacier, Rouge contre Bleu')], 'arcade'),
        'uhc': ('⛏ Mini UHC Run', 'gold', 'Choisis la carte.', [
            act('⛏ UHC — Plaines', 'green', 'trigger mg.go set 94', 'Plaines et forêts'),
            act('⛏ UHC — Désert', 'yellow', 'trigger mg.go set 202', 'Dunes, cactus, acacias'),
            act('⛏ UHC — Taïga enneigée', 'aqua', 'trigger mg.go set 204', 'Neige, sapins, lacs gelés')], 'arcade'),
        'hg': ('🏹 Mini Hunger Games', 'gold', 'Choisis la carte.', [
            act('🏹 HG — Plaines', 'green', 'trigger mg.go set 95', 'Plaines et forêts'),
            act('🏹 HG — Jungle', 'dark_green', 'trigger mg.go set 203', 'Jungle dense, roche moussue'),
            act('🏹 HG — Canyon', 'gold', 'trigger mg.go set 205', 'Terres cuites et sable rouge')], 'arcade'),
        'zombies': ('🧟 Zombies', 'dark_green', 'Choisis la carte.', [
            act('🧟 Zombies — Bunker', 'gray', 'trigger mg.go set 97', 'Le bunker d\'origine'),
            act('🧟 Zombies — Laboratoire', 'white', 'trigger mg.go set 210', 'Labo tout blanc'),
            act('🧟 Zombies — Manoir', 'dark_red', 'trigger mg.go set 212', 'Manoir sombre'),
            act('🧟 Zombies — Usine', 'aqua', 'trigger mg.go set 229', '7 salles, 8 portes, deux chemins vers la salle des machines'),
            act('🧟 Zombies — Station', 'light_purple', 'trigger mg.go set 231', 'Quais, galerie et réacteur : 7 salles en boucle'),
            act('🧟 Zombies — Hôpital', 'green', 'trigger mg.go set 235', 'Deux étages, cage d\'escalier, galerie au-dessus des urgences'),
            act('🧟 Zombies — Mine', 'gold', 'trigger mg.go set 237', 'Rampe, terrasses, puits avec un trou vers la galerie basse')], 'arcade'),
        'infection': ('🧪 Infection', 'green', 'Choisis la carte et le mode.', [
            act('🧪 Infection — Bunker', 'gray', 'trigger mg.go set 98', 'Le bunker d\'origine'),
            act('🧪 Infection — Laboratoire', 'white', 'trigger mg.go set 211', 'Labo tout blanc'),
            act('🧪 Infection — Manoir', 'dark_red', 'trigger mg.go set 213', 'Manoir sombre'),
            act('🧪 Infection — Usine', 'aqua', 'trigger mg.go set 230', 'Usine à 7 salles, tout ouvert'),
            act('🧪 Infection — Station', 'light_purple', 'trigger mg.go set 232', 'Station à 7 salles, tout ouvert'),
            act('🧪 Infection — Hôpital', 'green', 'trigger mg.go set 236', 'Hôpital sur deux étages, tout ouvert'),
            act('🧪 Infection — Mine', 'gold', 'trigger mg.go set 238', 'Mine à niveaux, tout ouvert'),
            act('🧟 Joueurs vs mobs — Bunker', 'red', 'trigger mg.go set 217', 'Tous survivants contre des zombies mobs ; touché = infecté'),
            act('🧟 Joueurs vs mobs — Laboratoire', 'red', 'trigger mg.go set 218', 'Tous survivants contre des zombies mobs ; touché = infecté'),
            act('🧟 Joueurs vs mobs — Manoir', 'red', 'trigger mg.go set 219', 'Tous survivants contre des zombies mobs ; touché = infecté')], 'arcade'),
        'kart': ('🏎 Kart', 'gold', 'Choisis le circuit.', [
            known('trigger mg.go set 61', '🏎 KART : Circuit Champignon', 'gold'), known('trigger mg.go set 62', '🏎 KART : Royaume Koopa', 'red'),
            known('trigger mg.go set 63', '🎈 KART : Bataille', 'light_purple')], 'courses'),
        'fete': ('🎉 Fête et création', 'green', 'Les grands formats.', [
            known(OPEN(16), '★ Mini Party ▸', 'gold'), known(OPEN(22), '✎ Build Battle ▸', 'green'),
            act('📞 Téléphone (5+)', 'gold', 'trigger mg.go set 83', 'Mot → construction → devinette → construction → devinette. 5 à 12 joueurs.')], 'menu'),
        'votes': ('☑ Votes', 'green', 'Vote pour le prochain jeu.', [
            known('trigger mg.vote set 98', '☑ Votes : voir', 'green'), known(OPEN(12), '☑ Votes : lancer le plus voté', 'green'),
            known(OPEN(13), '☑ Votes : réinitialiser', 'green')], 'menu'),
        'joueur': ('👤 Joueur et plots', 'aqua', 'Tes options et ton plot.', [
            known(OPEN(1), 'Mode spectateur ON/OFF', 'gray'), known(OPEN(2), 'Classement des victoires', 'gold'),
            known('trigger mg.pl set 1', '⌂ Aller sur mon plot', 'green'), known('trigger mg.pl set 2', '↩ Quitter mon plot', 'yellow'),
            known('trigger mg.pl set 3', '◎ Visiter les plots', 'aqua')], 'menu'),   # le duel est dans la fenêtre de vote (voir var_votemaps.py)
    }
