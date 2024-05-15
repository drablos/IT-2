# Dette er en kommentar i python

"""
Dette er en kommentar som går 
over flere linjer
"""

# En kommentar skal maks være 72 tegn
# i følge pythons stilguide (PEP)
# Hvis en kommentar må gå over to linjer fordi den er 
# over 72 tegn, bruker vi som regel hashtags og ikke triple anførselstegn

# Triple anførselstegn bruker vi som
# regel bare i spesielle kommentarer, som f.eks. docstrings


# -- Eksempel --

""" Dette er en docstring, som gr en overordnet 
    forklaring på hva programmet gjør.
    De skrives med tre anførselstegn.

    Et program som kaster en terning
"""


import random

# et tilfeldig tall fra og med 1 til og med 6
tilfeldig = random.randint(1, 6)
print(f"Du fikk {tilfeldig}")




