from html.parser import HTMLParser


class MyHtmlParser(HTMLParser):
    # Function to handle an opening tag in the doc.
    # This will be called when the closing ">" of the tag is reached.
    def handle_starttag(self, tag, attrs):
        pos = self.getpos()  # Returns a tuple indication line and character
        print("At line: ", pos[0], " position ", pos[1])
        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    # Function to handle the ending tag.
    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)
        pos = self.getpos()
        print("At line: ", pos[0], " position ", pos[1])

    # Function to handle character and text data (tag contents)
    def handle_data(self, data):
        print("Encountered some data:", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position ", pos[1])

    # Function to handle the processing of HTML comments.
    def handle_comment(self, data):
        print("Encountered comment:", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position ", pos[1])

def main():

    parser = MyHtmlParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)


if __name__ == "__main__":
    main()
