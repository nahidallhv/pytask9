cumle = input("bir cumle daxil edin: ")
with open("input.txt", "w") as f:
    f.write(cumle)
with open("input.txt", "r") as f:
    ilk_setir = f.readline().upper()
with open("output.txt", "w") as f:
    f.write(ilk_setir)
