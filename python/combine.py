def combine():
  with open("./created", "r") as f:
    created = f.read()

  with open("./settings/template.cc", "r") as f:
    template = f.read()

  createdcc = template.replace("///INSERT///", created)

  with open("./ns-3/scratch/created.cc","w") as f:
    print(createdcc, file=f)

combine()

