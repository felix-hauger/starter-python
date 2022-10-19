xml_file = open("domains.xml").read()

print(xml_file.count("name=\"domain\""))