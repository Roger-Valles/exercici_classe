def main():
    print("Benvingut al detector de gerrymanderings!")
    print("Aquest programma analitza si hi ha hagut gerrymanderings i alhora et dona informació de les eleccions.\n")

    estat = input("Quin estat vols buscar? ").strip().lower()

    districts_file = "districts.txt"
    eligible_voters_file = "eligible_voters.txt"

    informacio_districtes = llegir_document(districts_file)
    informacio_votants = llegir_document(eligible_voters_file)

    estat_del_districte = trobar_informacio_estat(informacio_districtes, estat)
    eligible_voters = trobar_votants_del_estat(informacio_votants, estat)

    if not estat_del_districte:
        print(f'L\'estat "{estat}" no ha estat trobat.')
        return

    if not eligible_voters:
        print(f'No hi ha informació dels votants en l\'estat "{estat}".')
        return

    total_dem_perduts, total_rep_perduts = calcular_vots_perduts(estat_del_districte)

    print(f"\nResultats per a {estat.capitalize()}:")
    print(f"Total vots Democrates perduts: {total_dem_perduts}")
    print(f"Total vots Republicans perduts: {total_rep_perduts}")
    print(f"Total votants possibles: {eligible_voters}")

    total_perdut = total_dem_perduts + total_rep_perduts
    if total_perdut > 0:
        gerrymandered = abs(total_dem_perduts - total_rep_perduts) / total_perdut >= 0.07
        partit_avantatjat = "Democrates" if total_dem_perduts < total_rep_perduts else "Republicans"

        if gerrymandered:
            print(f"L'estat ha estat beneficiat amb mètodes de gerrymandering per a avantatjar al {partit_avantatjat}.")
        else:
            print("L'estat no ha patit de gerrymandering.")
    else:
        print("Cap vot perdut detectat.")


def llegir_document(nom_fitxer):
    try:
        with open(nom_fitxer, "r") as fitxer:
            return fitxer.readlines()
    except FileNotFoundError:
        print(f"Error: Fitxer '{nom_fitxer}' no trobat.")
        return []


def trobar_informacio_estat(informacio, estat):
    for line in informacio:
        parts = line.strip().split(",")
        if parts[0].strip().lower() == estat:
            return parts[1:]
    return None


def trobar_votants_del_estat(informacio, estat):
    for line in informacio:
        parts = line.strip().split(",")
        if parts[0].strip().lower() == estat:
            return int(parts[1])
    return None


def calcular_vots_perduts(districts):
    total_dem_perduts = 0
    total_rep_perduts = 0

    for i in range(0, len(districts), 3):
        dem_votes = int(districts[i + 1])
        rep_votes = int(districts[i + 2])
        total_votes = dem_votes + rep_votes

        if dem_votes > rep_votes:
            perduts_dem = dem_votes - (rep_votes + 1)
            perduts_rep = rep_votes
        else:
            perduts_rep = rep_votes - (dem_votes + 1)
            perduts_dem = dem_votes

        total_dem_perduts += perduts_dem
        total_rep_perduts += perduts_rep

    return total_dem_perduts, total_rep_perduts


main()