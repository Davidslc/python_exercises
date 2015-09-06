import xml.dom.minidom


def main():

    doc = xml.dom.minidom.parse("samplexml.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # Get a list of XML tags from the document and print each one.
    skills = doc.getElementsByTagName("skill")
    print("%d skills:" % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

if __name__ == "__main__":
    main()