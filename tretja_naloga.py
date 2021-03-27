def listtostringwithslash(seznam):
    output = ""
    for x in seznam[1:]:
        output = output + "/" + x
    
    return output


cur_dir = [" "]
while True:
    new_input = input()
    new_input = new_input.split()
    if int(new_input[1]) > len(cur_dir):
        print("Napaka!")
        break
    elif int(new_input[1]) < len(cur_dir):
        cur_dir = cur_dir[:int(new_input[1])]
        cur_dir.append(new_input[0])
    else:
        cur_dir.append(new_input[0])
    print(listtostringwithslash(cur_dir))




# program bere s standardnega vhoda
# vhod najprej razdeli: v prvem delu je ime mape v drugem "globina" v drevesu
# seznam cur_dir pove v kateri mapi se trenutno nahajamo
# če je dolžina tega seznama manjša od globine v drevesu program javi napako, saj nam manjka vsaj ena raven (mapa)
# če je globina manjša od dolžine seznama vse elemente pred tem odstrani in nato doda ime mape v seznam
# če sta globina, in dolžina seznama enaki pa v seznam doda ime nove mape.

# funkcija listtostringwithslash nam izhod samo grafično oblikuje(iz seznama naredi string v katerega med elemente sezmama dodaja /)