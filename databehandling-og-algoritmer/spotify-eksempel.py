# Penger tjent per sang
land = input("Hvilket land er du fra?")
if land.lower() == "Norge":
    print("$0.44 per sang")
elif land.lower() == "Sverige":
    print("$0.34 per sang")
else:
    print("$0.22 per sang")

# Andel penger tjent per sang
streams = input("Hva er dine antall streams?")
if streams > 30000000:
    print("Penger tjent per sang lik 70%")
elif streams > 1400000:
    print("Penger tjent per sang lik 40%")
else:
    print("Penger tjent per sang lik 0%")



