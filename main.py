import random


def luoSekvenssi(edellinen=[]):
    def randomVäri(paletti=['punainen', 'sininen', 'keltainen', 'vihreä', 'valkoinen']):
        """
        ottaa
            kwarg lista paletti := halutut värit
        antaa
            random alkio paletista.
        nostaa
            ei mitään
        """
        return paletti[random.randint(0, len(paletti) - 1)]
    """
    ottaa:
        list edellinen := olemassa oleva sekvenssi, saa tältä funktiolta.
    antaa:
        liss := uusi sekvenssi
    nostaa:
        ei mitään
    """
    if len(edellinen) == 0:
        edellinen = []
    edellinen.append(randomVäri())
    return edellinen

# sekvenssi = []
#
# for i in range(10):
#     sekvenssi = luoSekvenssi(sekvenssi)
#     print(sekvenssi)
