
def calcola_punteggio(tiri: list[int]) -> int:
    punteggio = 0
    num_frame = 1
    num_tiro = 0
    tot_frame = 0

    for idx in range(0, len(tiri)):
        tiro = tiri[idx]
        print(f"Frame: {num_frame}, Tiro: {num_tiro}, Birilli: {tiro},Punteggio: {punteggio}")
        if num_frame > 10:
            break

        if tiro == 10:
            punteggio  += 10
            num_frame += 1
            num_tiro = 1
            tot_frame = 0
            print("STRIKE!")
            punteggio+= tiri[idx+1] + tiri[idx+2]
            continue
        punteggio += tiro
        tot_frame += tiro
        num_tiro+=1
        if num_tiro == 2:
            num_tiro = 0
            num_frame += 1
            tot_frame = 0
        if tot_frame == 10:
            print("SPARE!")
            punteggio += tiri[idx+1]
        
    return punteggio
