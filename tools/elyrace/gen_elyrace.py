"""Course d'elytres (id 66 = parcours au hasard, ids 81 et suivants = un parcours) : moteur multi-parcours. Usage (depuis la racine du depot) :
    python tools/elyrace/gen_elyrace.py <racine du depot>            ecrit les fichiers generes
    python tools/elyrace/gen_elyrace.py <racine du depot> --check    ne ecrit rien : budget de commandes, vol de verification
                                                                     du pilote automatique, references de fonctions, desinstallation,
                                                                     zones, ouvertures de fenetre (forme gen_rating), drapeaux du suivi
                                                                     de mg:setup, et fichiers du depot identiques a ce que le generateur produirait
Sortie : data/mg/function/elyrace/** (un sous-dossier c<N>/ par parcours ; solo/ = contre-la-montre solo par joueur, records), core/sub/elyrace,
dialog/sub_elyrace.json, dialog/sub_elyrace_solo.json, advancement/elyrace_wall.json, tags/damage_type/elyrace_wall.json.
Les fichiers generes ne se modifient jamais a la main. Les branchements dans le moteur (wire_elyrace*.py) se font apres la generation.
Ordre de la chaine : ce generateur, puis tools/variantes/gen_variants.py (PYTHONUTF8=1 ; il relance tools/rating/gen_rating.py, qui reecrit
les fenetres en rate/d/<nom>). Les ouvertures de fenetre sont donc ecrites ici sous leur forme finale (menus.rate_call) et --check le verifie.
Pour ajouter un parcours : ecrire son module « spec » (voir course_common.py), l'ajouter a SPECS.
Python stdlib uniquement (compatible 3.8).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_chain as B            # noqa: E402
import checks as K                 # noqa: E402
import course_blanc                # noqa: E402
import course_canyon               # noqa: E402
import course_common as CC         # noqa: E402
import course_fns as F             # noqa: E402
import dispatch as D               # noqa: E402
import game as G                   # noqa: E402
import menus as M                  # noqa: E402
import records as RC               # noqa: E402
import rings as R                  # noqa: E402
import solo as S                   # noqa: E402
import solo_run as SR              # noqa: E402
import sweep as SW                 # noqa: E402

SPECS = [course_canyon, course_blanc]          # un module par parcours, dans l'ordre des NUM


def all_files(courses):
    """Tous les fichiers generes : {chemin relatif a la racine: texte}. `courses` = [Course] (un par spec de SPECS)."""
    specs = [c.spec for c in courses]
    files = {}
    fns = G.functions(specs)
    fns.update(D.functions(specs))
    fns.update(SW.functions())
    fns.update(B.common_files(specs))
    fns.update(S.functions(specs))
    fns.update(SR.functions(specs))
    fns.update(RC.functions(specs))
    for c in courses:
        sub = {}
        sub.update(F.functions(c))
        sub.update(R.functions(c))
        sub.update(B.course_files(c))
        sub.update(RC.course_files(c.spec))
        fns.update(('c%d/%s' % (c.spec.NUM, name), lines) for name, lines in sub.items())
    for name, lines in fns.items():
        files[CC.FN + name + '.mcfunction'] = CC.lines_to_text(lines)
    files['data/mg/function/core/sub/elyrace.mcfunction'] = CC.lines_to_text(M.sub_lines(specs))
    files['data/mg/dialog/sub_elyrace.json'] = M.dumps(M.dialog_json(specs))
    files['data/mg/dialog/sub_elyrace_solo.json'] = M.dumps(M.solo_dialog_json(specs))
    files['data/mg/advancement/elyrace_wall.json'] = M.dumps(M.advancement_json())
    files['data/mg/tags/damage_type/elyrace_wall.json'] = M.dumps(M.damage_tag_json())
    return files


def write_all(root, files):
    d = os.path.join(root, CC.FN)
    os.makedirs(d, exist_ok=True)
    for base, dirs, names in os.walk(d, topdown=False):         # parcours ou tranches disparus : on repart d'un dossier propre
        for n in names:
            if n.endswith('.mcfunction'):
                os.remove(os.path.join(base, n))
        if base != d and not os.listdir(base):
            os.rmdir(base)
    for rel, text in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1:
        raise SystemExit(__doc__)
    root = os.path.abspath(args[0])
    courses = [s.build() for s in SPECS]
    files = all_files(courses)
    print('%d fichiers, %d parcours' % (len(files), len(courses)))
    if '--check' in sys.argv:
        bad = K.check(root, courses, files)
        print('\n'.join(bad) if bad else 'CHECK OK (budget, pilote automatique, references, desinstallation, zones, ouvertures de fenetre, drapeaux du suivi de mg:setup, fichiers a jour)')
        sys.exit(1 if bad else 0)
    write_all(root, files)
    print('ecrit dans', os.path.join(root, 'data', 'mg'))


if __name__ == '__main__':
    main()
