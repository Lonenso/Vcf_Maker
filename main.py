template = """BEGIN:VCARD
VERSION:3.0
N:;{name};;;
FN:{firstname}
TEL;TYPE=CELL:{phone1}
TEL;TYPE=HOME:{phone2}
END:VCARD
"""

l = [
    {"name":"", "phone1":"", "phone2":""}
]

s = ""
for contact in l:
    name=contact["name"]
    phone1=contact["phone1"]
    phone2=contact["phone2"]
    s += template.format(name=name, firstname=name, phone1=phone1, phone2=phone2)

with open("my.vcf", "w", encoding="utf8") as f:
    f.write(s)

print(s)
