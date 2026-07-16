leads= [200,100,150,400,560,300,700,800,900,1000]
for index, lead in enumerate(leads):
    if lead > 500:
        print(f"Lead {index} is a high value lead with score {lead}")
    else:
        print(f"Lead {index} is a low value lead with score {lead}")