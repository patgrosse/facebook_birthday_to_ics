import sys
import uuid
from pyquery import PyQuery
import re


def main():
    if len(sys.argv) != 2:
        print("Usage: %s <HTML_FILE>" % sys.argv[0])
        exit(1)

    ics = "BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//patgrosse//NONSGML birthday gen//EN\r\n"

    d = PyQuery(filename=sys.argv[1])
    birthdays = {}
    elems = d("._43q7 > a")
    for elem in elems.items():
        data = elem.attr("data-tooltip-content")

        # try English format
        m_en = re.search("^(.+) \\((\\d+)/(\\d+)\\)$", data)
        # noinspection PyBroadException
        try:
            birthdays[m_en.group(1)] = [int(m_en.group(3)), int(m_en.group(2))]
            continue
        except:
            pass

        # try German format
        m_de = re.search("^(.+) \\((\\d+)\\.(\\d+)\\.\\)$", data)
        # noinspection PyBroadException
        try:
            birthdays[m_de.group(1)] = [int(m_de.group(2)), int(m_de.group(3))]
            continue
        except:
            pass

        print("Could not parse: %s" % data)

    for name, d in birthdays.items():
        ics += "BEGIN:VEVENT\r\nDTSTAMP:20010901T130000Z\r\nDTSTART:2000%02d%02d\r\nDTEND:2000%02d%02d\r\nUID:%s\r\n" \
               "SEQUENCE:0\r\nSUMMARY:%s birthday\r\nRRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=%d;BYMONTHDAY=%d\r\n" \
               "END:VEVENT\r\n" % (d[1], d[0], d[1], d[0], uuid.uuid4(), name, d[1], d[0])
    ics += "END:VCALENDAR"
    with open("birthdays.ics", "w") as ics_file:
        ics_file.write(ics)

    print("Exported %d birthdays from HTML file %s to ICS file birthdays.ics" % (len(birthdays), sys.argv[1]))


if __name__ == '__main__':
    main()
