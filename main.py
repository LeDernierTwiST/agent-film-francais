# AGENT FILM FRANCAIS - 100% GRATUIT
# Usage: python main.py "Anatomie d'une chute"
import sys
import asyncio
import edge_tts

FILMS_DB = {
    "Anatomie d'une chute": {
        "script": """Un homme est mort. Il est tombe de sa maison, dans la neige.
        Sa femme dit que c'est un accident. Son fils, aveugle, dit qu'il n'a rien vu.
        Alors, qui a dit la verite ?
        Sandra, une ecrivaine, vit avec Samuel, son mari, et Daniel, leur fils.
        Un jour, Daniel retrouve son pere mort devant la maison.
        La police ne sait pas : suicide, accident, ou meurtre ?
        Sandra devient la suspecte numero 1.
        Le film n'est pas un film policier. C'est un film sur le couple.
        Pendant le proces, on decouvre les disputes, la jalousie, le succes de Sandra et l'echec de Samuel.
        Justine Triet ne nous dit jamais la verite. Elle nous laisse choisir.
        Ce n'est pas 'Qui a tue Samuel ?' C'est 'Est-ce qu'on peut vraiment connaitre quelqu'un ?'
        A la fin, Sandra est libre. Mais est-elle innocente ? Le film ne repond pas.
        C'est pour ca qu'il a gagne la Palme d'Or a Cannes. Note : 9 sur 10. A voir absolument.
        """,
    },
    "Intouchables": {
        "script": """Philippe est riche, mais il est paralyse. Driss vient de banlieue, il n'a rien.
        Quand Driss devient son aide a domicile, tout change.
        Ce n'est pas une histoire de handicap. C'est une histoire d'amitie.
        Deux mondes qui ne devaient jamais se rencontrer.
        Le film le plus vu en France. Une lecon de vie. Note : 9 sur 10.
        """,
    }
}

async def generer_voix(texte, output="voix.mp3"):
    communicate = edge_tts.Communicate(texte, "fr-FR-DeniseNeural", rate="+5%")
    await communicate.save(output)
    print(f"Voix creee : {output}")

def main():
    if len(sys.argv) < 2:
        print('Utilise : python main.py "Anatomie d\'une chute"')
        return
    nom = sys.argv[1]
    film = FILMS_DB.get(nom)
    if not film:
        print(f"Film {nom} pas trouve. Ajoute-le dans FILMS_DB")
        return
    print(f"Creation pour : {nom} ...")
    asyncio.run(generer_voix(film["script"]))
    print("Termine ! Tu as ton audio en francais.")

if __name__ == "__main__":
    main()
