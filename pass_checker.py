while True:
    p=input("Enter your password:")
    if p.lower()=="exit":
        break
    u=any(a.isupper() for a in p)
    l=any(a.islower() for a in p)
    d=any(a.isdigit() for a in p)
    s=any(not a.isalnum() for a in p)
    c=0
    if len(p)>=6:
        c+=2
    if u:
        c+=2
    if l:
        c+=2
    if d:
        c+=2
    if s:
        c+=2
    if c<=4:
        h="Weak"
    elif c<=7:
        h="Moderate"
    else:
        h="Strong"
    n=[]
    if len(p) < 6:
        n.append("Increase length to at least 6")
    if not u:
        n.append("Add uppercase letters")
    if not l:
        n.append("Add lowercase letters")
    if not d:
        n.append("Add numbers")
    if not s:
        n.append("Add special characters")
    if c <= 4:
        t = "Few seconds"
    elif c <= 7:
        t = "Few hours"
    else:
        t = "Years"
    print("\n" + "="*30)
    print(" PASSWORD ANALYSIS ")
    print("="*30)
    print("\nStrength:", h)
    print("Score:", c, "/10")
    print("Estimated crack time:", t)
    if n:
        print("Suggestions:")
        for j in n:
            print("-", j)
    print()
    print("Type exit to stop")
    print()
        