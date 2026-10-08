"""Branche la Course d'elytres (id 66) dans le moteur et les menus : python wire_elyrace.py <racine du depot>. Une seule fois
(les ancres ne se retrouvent plus apres le premier passage : relancer s'arrete sur la premiere).
Chaque ancre doit exister EXACTEMENT une fois : les modifications sont d'abord faites en memoire (wirelib.Patcher) et rien
n'est ecrit si une ancre manque ; les fins de ligne de chaque fichier (CRLF ou LF) sont conservees. Les fichiers generes
(elyrace/**, sub, dialog sub_elyrace, avancement, tag de degats) viennent de gen_elyrace.py, le hall (plaque, classement)
de tools/hall/gen_hall.py. Le branchement des parcours multiples (66 au hasard, 81, 82) est fait ensuite par wire_elyrace2.py.
"""
import os
import sys

from wirelib import Patcher


def tick_net(p):
    """core/tick : filet qui retire les elytres et fusees de la course aux joueurs qui ne sont pas en course."""
    anchor = 'execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]'
    p.after_fn('core/tick', anchor,
               'execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play] minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]\n'
               'execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play] minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]\n')


def request_guard(p):
    """core/request : si prepare a annule la partie (parcours pas construit : core/draw met l'etat a 3), on ne poursuit pas
    le lancement (compte a rebours, gel, titre)."""
    p.after_fn('core/request', 'execute if score $game mg.st matches 66 run function mg:elyrace/prepare',
               'execute if score $state mg.st matches 3 run return 0\n')


def menu_wiring(p):
    """Menu d'options (28 = sous-menu Course d'elytres, meme garde admin que 16..24), menu texte, fenetre du menu."""
    path = p.fn_path('core/opt')
    s, nl = p.text(path)
    lock = [l for l in s.split('\n') if l.startswith('execute if score @s mg.opt matches 16..24 unless entity @s[tag=mg.admin] run tellraw')]
    if len(lock) != 1:
        raise SystemExit('core/opt : %d lignes de verrou admin 16..24 (1 attendue)' % len(lock))
    p.patch(path, lock[0] + '\n', lock[0] + '\n' + lock[0].replace('matches 16..24', 'matches 28', 1) + '\n')
    p.after(path, 'execute if score @s mg.opt matches 24 if entity @s[tag=mg.admin] run function mg:core/sub/oitc',
            'execute if score @s mg.opt matches 28 if entity @s[tag=mg.admin] run function mg:core/sub/elyrace\n')
    p.patch_fn('core/menu_chat', 'tellraw @s ["",{"text":" [⬇ The Dropper ▸]"',
               'tellraw @s ["",{"text":" [🪽 Course d\'élytres ▸]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.opt set 28"},'
               '"hover_event":{"action":"show_text","value":"Plane à travers des anneaux : choisis le parcours."}}]\n'
               'tellraw @s ["",{"text":" [⬇ The Dropper ▸]"')

    def add_entry(d):
        idx = [i for i, a in enumerate(d['actions']) if a['label'][0]['text'] == '⬇ The Dropper ▸']
        if len(idx) != 1:
            raise SystemExit('dialog/menu.json : %d entrees « The Dropper » (1 attendue)' % len(idx))
        d['actions'].insert(idx[0] + 1, {
            "label": [{"text": "🪽 Course d'élytres ▸", "color": "aqua"}],
            "tooltip": [{"text": "Plane à travers des anneaux : choisis le parcours.", "color": "gray"}],
            "action": {"type": "minecraft:run_command", "command": "trigger mg.opt set 28"}})
    p.edit_json(p.path('data', 'mg', 'dialog', 'menu.json'), add_entry)


def docs(p):
    """aide, README et table des IDs."""
    p.patch_fn('aide', 'tellraw @s [{"text":"• Bataille de karts (admins) : ","color":"gray"}',
               'tellraw @s [{"text":"• Course d\'élytres (admins) : ","color":"gray"},{"text":"/trigger mg.go set 66","color":"yellow"},'
               '{"text":" ; Canyon du Couchant, 18 anneaux (reconstruire : /function mg:elyrace/build)","color":"gray"}]\n'
               'tellraw @s [{"text":"• Bataille de karts (admins) : ","color":"gray"}')
    readme = p.path('README.md')
    row = ("| **🪽 Course d'élytres : Canyon du Couchant** (id 66) | Course aérienne en élytres sur un parcours Far West d'environ 1 000 blocs (z 27000) : saut depuis une falaise, "
           "slalom entre cheminées de fée, 3 arches, viaduc ferroviaire, gorge en S, crête à franchir en montée, ville fantôme. **18 anneaux** à franchir dans l'ordre par leur trou de 9 × 9 "
           "(un anneau raté renvoie au dernier point de reprise), **4 points de reprise** (colonnes lumineuses), **3 anneaux d'or** en détour qui donnent chacun une fusée (aucune au départ), "
           "**3 cœurs** (chaque choc contre un mur en retire un ; à zéro, au sol, dans l'eau ou après trop de temps sans planer : retour en l'air au point de reprise). "
           "Le premier arrivé gagne, les autres sont classés pendant 20 s ; au bout de 3 minutes le plus avancé gagne. Parcours vérifié par un pilote automatique simulé. "
           "Générateur : `tools/elyrace/gen_elyrace.py`. | 1+ |\n")
    p.patch(readme, '| **⬇ The Dropper : Aventure** (id 64)', row + '| **⬇ The Dropper : Aventure** (id 64)')
    p.patch(readme, '| `/trigger mg.go set 25` | The Dropper : tube commun | admins |\n',
            '| `/trigger mg.go set 25` | The Dropper : tube commun | admins |\n| `/trigger mg.go set 66` | Course d\'élytres : Canyon du Couchant | admins |\n')
    p.patch(p.path('docs', 'GAMES.md'), '| 65 | `mg:dropadv/c_tick` |\n', '| 65 | `mg:dropadv/c_tick` |\n| 66 | `mg:elyrace/tick` |\n')


def wire_all(p):
    g = 'execute if score $game mg.st matches %s run function mg:%s\n'

    def hook(rel, anchor_match, anchor_fn, match, fn):
        p.after_fn(rel, g.rstrip('\n') % (anchor_match, anchor_fn), g % (match, fn))

    p.patch_fn('core/go', 'matches 1..65', 'matches 1..66')
    hook('core/request', '65', 'dropadv/c_prepare', '66', 'elyrace/prepare')
    request_guard(p)
    p.patch_fn('core/request', 'execute if score $game mg.st matches 64 run tellraw',
               'execute if score $game mg.st matches 66 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance la ","color":"gray"},'
               '{"text":"🪽 COURSE D\'ÉLYTRES","color":"aqua","bold":true},{"text":" : Canyon du Couchant (18 anneaux, le premier arrivé gagne) !","color":"gray"}]\n'
               'execute if score $game mg.st matches 64 run tellraw')
    hook('core/begin', '65', 'dropadv/c_go', '66', 'elyrace/go')
    hook('core/game_tick', '65', 'dropadv/c_tick', '66', 'elyrace/tick')
    hook('core/return_lobby', '64..65', 'dropadv/cleanup', '66', 'elyrace/cleanup')
    p.after_fn('core/setup_build', 'schedule function mg:dropadv/build 30s',
               'data remove storage mg:elyrace v1\nschedule function mg:elyrace/build 45s\n')
    p.after_fn('core/load', 'function mg:core/load_hp', 'function mg:elyrace/objectives\n')
    p.after_fn('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:dropadv v3 run schedule function mg:dropadv/build 40s',
               'execute if score $setup mg.st matches 1 unless data storage mg:elyrace v1 run schedule function mg:elyrace/build 60s\n'
               'execute if score $setup mg.st matches 1 unless data storage mg:hall v2 run schedule function mg:hall/build 20s\n')
    p.patch_fn('desinstaller', 'scoreboard objectives remove mg.erb2', 'scoreboard objectives remove mg.erb2\nfunction mg:elyrace/uninstall')
    tick_net(p)
    menu_wiring(p)
    docs(p)


def main():
    if len(sys.argv) != 2 or not os.path.isdir(os.path.join(sys.argv[1], 'data', 'mg', 'function')):
        raise SystemExit(__doc__)
    p = Patcher(os.path.abspath(sys.argv[1]))
    wire_all(p)
    print('%d fichiers modifies' % p.commit())


if __name__ == '__main__':
    main()
