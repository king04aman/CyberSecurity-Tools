import crypt

password = open("password.txt", 'r')
for passwd in password.readlines():
    passwd = passwd.strip("\n").strip("\r")
    var = crypt.crypt(passwd,"$6$"+"8HOLitkI")
    if var == "$6$8HOLitkI$9HECw2MBzISI1O.RoyJdfugy4VHsTOU4RDTewcFECnZdWLpmtVwNo5a1/hg2kw4Qu74F08eMEwpLdK1eovfEd/":
        print("password found: ", passwd )
        break
    else:
        print("trying....")