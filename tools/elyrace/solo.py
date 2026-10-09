"""Contre-la-montre solo de la Course d'elytres, partie LANCEMENT : tout joueur (admin ou non) peut courir seul, pendant n'importe quelle
partie sauf une course d'elytres de groupe (4 solos au plus en meme temps, sur le meme parcours ou non). Acces par le trigger mg.xs
(menus.SOLO_*), jamais par mg.go (reserve aux admins). Le solo ne touche jamais la machine a etats ($state, $game, $timer, mg.play) :
tout son etat est PAR JOUEUR (tag mg.xso, scores mg.xph / xst / xcr / xse / xsl, voir game.EXTRA_OBJECTIVES). Lancer un solo met le joueur
en PAUSE (tag mg.spectate : votes et lancements l'ignorent d'eux-memes) ; la pause d'avant est memorisee dans le tag mg.xsp0.
Fonctions generees ici : elyrace/solo/{cmd, start, announce, quit, stop_all, menu}. Le tick, le decompte, le depart, l'arrivee et la sortie
sont dans solo_run.py (solo/go est la seule entree en course, solo/stop la seule sortie).
Branchements dans le moteur : wire_elyrace4.py (core/tick). Python stdlib uniquement (compatible 3.8).
"""
import game as G
import menus as M

COOLDOWN = 600           # ticks (30 s) apres la fin du dernier solo DU JOUEUR (mg.xse) ; admins exemptes
MAX_SOLO = 4             # solos simultanes (une place de depart chacun : mg.ri 1..MAX_SOLO)
ACTIVITY_TAGS = ('mg.ely', 'mg.elyf', 'mg.lk', 'mg.pkr')    # parcours d'elytra, elytres libres, kart libre, parkour du lobby
PLOT_TAGS = ('mg.inplot', 'mg.visit')                       # plot (le sien ou en visite)
QUIT_LINK = ('{"text":"[✖ Abandonner]","color":"red","click_event":{"action":"run_command","command":"trigger mg.xs set %d"},'
             '"hover_event":{"action":"show_text","value":"Quitter le contre-la-montre"}}' % M.SOLO_QUIT)


def refuse(cond, text):
    """Refus : message au demandeur puis fin de la fonction, sans effet de bord."""
    return 'execute %s run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"%s","color":"red"}]' % (cond, text)


def cmd_lines():
    return ['# @s = joueur qui a utilise /trigger mg.xs : %d = fenêtre, %d = abandon, %d = ses records, %d = (admin) arrêter tous les solos, %d = solo au hasard, %d + NUM = solo sur le parcours NUM'
            % (M.SOLO_MENU, M.SOLO_QUIT, M.SOLO_RECORDS, M.SOLO_STOP, M.SOLO_RANDOM, M.SOLO_RANDOM),
            '# la valeur est lue dans #xv, puis le trigger est remis à zéro d\'abord (core/tick le réactive à chaque tick)',
            'scoreboard players operation #xv mg.st = @s mg.xs',
            'scoreboard players reset @s mg.xs',
            'execute if score #xv mg.st matches %d run function mg:elyrace/solo/menu' % M.SOLO_MENU,
            'execute if score #xv mg.st matches %d run function mg:elyrace/solo/quit' % M.SOLO_QUIT,
            'execute if score #xv mg.st matches %d run function mg:elyrace/records' % M.SOLO_RECORDS,
            'execute if score #xv mg.st matches %d run function mg:elyrace/solo/stop_all' % M.SOLO_STOP,
            'execute if score #xv mg.st matches %d.. run function mg:elyrace/solo/start' % M.SOLO_RANDOM]


def checks_lines(specs):
    """Refus dans l'ordre : installation, joueur, partie en cours, solos, delai, puis parcours construit (le seul qui touche a $xc)."""
    out = [refuse('unless score $setup mg.st matches 1', 'Installation manquante : un OP doit d\'abord lancer /function mg:setup.'),
           refuse('unless entity @s[tag=mg.init]', 'Pas encore prêt : réessaie dans un instant.'),
           refuse('if entity @s[tag=mg.surv]', 'Impossible depuis la survie : reviens d\'abord au lobby (/trigger mg.sv set 2).'),
           refuse('if entity @s[tag=mg.play]', 'Impossible pendant que tu participes à une partie.'),
           refuse('if entity @s[tag=mg.out]', 'Impossible : tu regardes la partie en cours en spectateur.'),
           refuse('if entity @s[tag=mg.xso]', 'Tu es déjà en contre-la-montre solo.'),
           refuse('if entity @s[gamemode=spectator]', 'Impossible en mode spectateur.')]
    out += [refuse('if entity @s[tag=%s]' % t, 'Termine d\'abord ton activité en cours (parcours d\'élytra, élytres libres, kart libre ou parkour).') for t in ACTIVITY_TAGS]
    out += [refuse('if entity @s[tag=%s]' % t, 'Impossible depuis un plot : reviens d\'abord au lobby.') for t in PLOT_TAGS]
    out += [refuse('if score $mp mg.st matches 1 if entity @s[tag=mg.mpp]', 'Tu participes à la Mini Party : attends sa fin.'),
            refuse('if score $game mg.st matches %d if score $state mg.st matches 1..3' % G.GAME_ID, 'Une course d\'élytres de groupe est en cours : attends sa fin.'),
            'execute store result score #xn mg.st if entity @a[tag=mg.xso]',
            refuse('if score #xn mg.st matches %d..' % MAX_SOLO, 'Déjà %d contre-la-montre solo en cours : attends qu\'un se termine.' % MAX_SOLO),
            '# délai depuis la fin du dernier solo du joueur (@s mg.xse, en ticks de $tc) : #xd = ticks écoulés (600 = pas d\'attente) ; les admins en sont exemptés',
            'scoreboard players set #xd mg.st %d' % COOLDOWN,
            'execute if score @s mg.xse matches 1.. run scoreboard players operation #xd mg.st = $tc mg.st',
            'execute if score @s mg.xse matches 1.. run scoreboard players operation #xd mg.st -= @s mg.xse',
            'scoreboard players set #xr mg.st %d' % COOLDOWN,
            'scoreboard players operation #xr mg.st -= #xd mg.st',
            'scoreboard players operation #xr mg.st /= #k20 mg.st',
            'scoreboard players add #xr mg.st 1',
            'execute unless entity @s[tag=mg.admin] if score #xd mg.st matches 0..%d run return run tellraw @s '
            '[{"text":"⚠ Attends encore ","color":"red"},{"score":{"name":"#xr","objective":"mg.st"},"color":"red"},{"text":" s avant un nouveau solo.","color":"red"}]' % (COOLDOWN - 1),
            '# parcours : #xv = 10 (au hasard, tiré parmi les construits par pick) ou 10 + NUM ; refusé s\'il n\'est pas construit',
            '# ($xc sert de brouillon à pick : jamais lu pendant un solo, remis à 0 plus bas ; un lancement de groupe le repose lui-même)',
            'scoreboard players set $xc mg.st 0',
            'execute if score #xv mg.st matches %d.. run scoreboard players operation $xc mg.st = #xv mg.st' % (M.SOLO_RANDOM + 1),
            'execute if score #xv mg.st matches %d.. run scoreboard players remove $xc mg.st %d' % (M.SOLO_RANDOM + 1, M.SOLO_RANDOM),
            'execute if score $xc mg.st matches 0 run function mg:elyrace/pick',
            refuse('if score $xc mg.st matches 0', 'Aucun parcours n\'est construit pour le moment : réessaie plus tard.')]
    out += [refuse('if score $xc mg.st matches %d unless data storage mg:elyrace %s' % (s.NUM, s.FLAG),
                   'Le parcours %d (%s) n\'est pas encore construit : réessaie plus tard.' % (s.NUM, s.NAME)) for s in specs]
    return out


def start_lines(specs):
    top = M.SOLO_RANDOM + len(specs)
    out = ['# @s = joueur qui lance un contre-la-montre solo (#xv = %d : parcours au hasard, %d + NUM : parcours NUM). Rien de global : ni $state, ni vote effacé,' % (M.SOLO_RANDOM, M.SOLO_RANDOM),
           '# ni objets retirés aux autres, ni annonce de jeu ; le joueur est mis en pause (mg.spectate), seul son état change',
           'execute unless score #xv mg.st matches %d..%d run return 0' % (M.SOLO_RANDOM, top)]
    out += checks_lines(specs)
    out += ['# lancement (plus aucun refus après ce point). La pause d\'avant est mémorisée, puis le joueur passe en pause SANS opt_spec (il bascule,',
            '# affiche des messages trompeurs et élimine un participant) ; son vote éventuel ne compte plus',
            'execute if entity @s[tag=mg.spectate] run tag @s add mg.xsp0',
            'tag @s add mg.spectate',
            'scoreboard players reset @s mg.vc',
            'execute if score $state mg.st matches 0 run function mg:vote/refresh',
            'tag @s add mg.xso',
            'scoreboard players operation @s mg.xcr = $xc mg.st',
            'scoreboard players set $xc mg.st 0',
            '# état du solo : phase 1 (décompte), chrono à 0 ; mg.xsl = tick précédent (le tick de ce lancement compte comme « vu »)',
            'scoreboard players set @s mg.xph 1',
            'scoreboard players set @s mg.xst 0',
            'scoreboard players operation @s mg.xsl = $tc mg.st',
            'scoreboard players remove @s mg.xsl 1',
            'scoreboard players set @s mg.deaths 0']
    out += ['scoreboard players set @s mg.%s %d' % (n, G.HEARTS if n == 'xh' else 0) for n, _, _ in G.OBJECTIVES]
    out += ['scoreboard players reset @s mg.qs', 'scoreboard players reset @s mg.fw', 'scoreboard players reset @s mg.wc',
            'scoreboard players reset @s mg.wd', 'scoreboard players reset @s mg.us',
            '# place de départ libre : la plus petite que les autres solos n\'occupent pas (au plus %d solos : il y en a toujours une)' % MAX_SOLO,
            'scoreboard players set @s mg.ri 0']
    out += ['execute if score @s mg.ri matches 0 unless entity @a[tag=mg.xso,scores={mg.ri=%d}] run scoreboard players set @s mg.ri %d' % (k, k)
            for k in range(1, MAX_SOLO + 1)]
    out += ['gamemode adventure @s', 'effect clear @s', 'clear @s',
            'function mg:elyrace/equip']
    out += ['execute if score @s mg.xcr matches %d run spawnpoint @s 24 %d %d' % (s.NUM, s.START_Y, s.CZ) for s in specs]
    out += ['function mg:elyrace/place_tp',
            'function mg:core/freeze',
            'effect give @s minecraft:resistance 7 255 true',
            'function mg:elyrace/solo/announce',
            'title @s title [{"text":"Prépare-toi !","color":"gold"}]',
            'title @s subtitle [{"text":"Début dans 5 secondes...","color":"gray"}]',
            'execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8']
    return out


def announce_lines(specs):
    head = ('tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance un ","color":"gray"},{"text":"⏱ CONTRE-LA-MONTRE","color":"aqua","bold":true},'
            '{"text":" solo : %s","color":"gray"}]')
    out = ['# Annonce du solo (@s = joueur, son parcours est mg.xcr) et lien d\'abandon pour lui seul']
    out += ['execute if score @s mg.xcr matches %d run %s' % (s.NUM, head % ('%s (%d anneaux) !' % (s.NAME, len(s.RINGS)))) for s in specs]
    out.append('tellraw @s [{"text":"⏱ Seul en piste : ton meilleur temps est enregistré. Tu es en pause pendant le solo : reprendre la pause l\'arrête. ","color":"gray"},%s]' % QUIT_LINK)
    return out


def quit_lines():
    return ['# @s = joueur qui abandonne (mg.xs %d, lien du message de lancement)' % M.SOLO_QUIT,
            'execute unless entity @s[tag=mg.xso] run return run tellraw @s [{"text":"⚠ Tu n\'as pas de contre-la-montre en cours.","color":"red"}]',
            'tellraw @a [{"selector":"@s","color":"yellow"},{"text":" abandonne le contre-la-montre.","color":"gray"}]',
            'function mg:elyrace/solo/stop']


def stop_all_lines():
    return ['# @s = admin (mg.xs %d) : arrête tous les contre-la-montre solo (sans toucher à core/abort : le solo n\'est pas une partie)' % M.SOLO_STOP,
            'execute unless entity @s[tag=mg.admin] run return run tellraw @s [{"text":"⚠ Réservé aux admins.","color":"red"}]',
            'execute unless entity @a[tag=mg.xso] run return run tellraw @s [{"text":"Aucun contre-la-montre solo en cours.","color":"gray"}]',
            'tellraw @a[tag=mg.xso] [{"selector":"@s","color":"yellow"},{"text":" a arrêté les contre-la-montre solo.","color":"red"}]',
            'execute as @a[tag=mg.xso] run function mg:elyrace/solo/stop']


def menu_lines(specs):
    return (['# @s = joueur : fenêtre du contre-la-montre solo (ouverte à tous), sinon menu texte',
             'scoreboard players set $dlg mg.st 0',
             'execute store success score $dlg mg.st run ' + M.rate_call('sub_elyrace_solo', False),
             'execute if score $dlg mg.st matches 1 run return 0']
            + M.solo_text_lines(specs)
            + ['tellraw @s ["",{"text":" [« Retour]","color":"yellow","click_event":{"action":"run_command","command":"%s"}}]' % M.SOLO_BACK_MENU])


def functions(specs):
    return {'solo/cmd': cmd_lines(), 'solo/start': start_lines(specs), 'solo/announce': announce_lines(specs),
            'solo/quit': quit_lines(), 'solo/stop_all': stop_all_lines(), 'solo/menu': menu_lines(specs)}
