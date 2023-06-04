from configparser import ConfigParser

parser = ConfigParser()
parser.read("multisection.ini")

for section in ("bug_tracker", "wiki", "none"):
    print("%s section exists: %s" % (section, parser.has_section(section)))
    if parser.has_section(section):
        for candidate in ("username", "password", "url", "description"):
            print(
                "%s.%-12s  : %s"
                % (section, candidate, parser.has_option(section, candidate))
            )
        print()

    