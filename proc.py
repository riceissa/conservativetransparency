#!/usr/bin/env python3

import csv
import sys


def main():
    if len(sys.argv) != 1+1:
        print("Please include the input CSV file as argument one.",
              file=sys.stderr)
        sys.exit()

    with open(sys.argv[1], "r") as f:
        reader = csv.DictReader(f)

        print("""insert into donations (donor, donee, amount, donation_date,
        donation_date_precision, donation_date_basis, cause_area, url,
        donor_cause_area_url, notes, affected_countries, affected_states,
        affected_cities, affected_regions) values""")

        first = True
        for row in reader:
            donation_date = row["year"] + "-01-01"
            print(("    " if first else "    ,") + "(" + ",".join([
                mysql_quote(fix_encoding(row["donor_name"])),  # donor
                mysql_quote(fix_encoding(row["recipient_name"])),  # donee
                str(int(row["contribution"])),  # amount
                mysql_quote(donation_date),  # donation_date
                mysql_quote("year"),  # donation_date_precision
                mysql_quote("donation log"),  # donation_date_basis
                mysql_quote(""),  # cause_area
                mysql_quote(""),  # url
                mysql_quote(""),  # donor_cause_area_url
                mysql_quote(""),  # notes
                mysql_quote(""),  # affected_countries
                mysql_quote(""),  # affected_states
                mysql_quote(""),  # affected_cities
                mysql_quote(""),  # affected_regions
            ]) + ")")
            first = False
        print(";")


def fix_encoding(x):
    return x.replace("&amp;", "&")


def csv_to_url(csv_filename):
    urls = [
            "http://conservativetransparency.org/donor/john-m-olin-foundation/",
            "http://conservativetransparency.org/donor/the-lynde-and-harry-bradley-foundation/",
            "http://conservativetransparency.org/donor/walton-family-foundation",
            "http://conservativetransparency.org/donor/earhart-foundation/",
            "http://conservativetransparency.org/donor/donorstrust/",
            "http://conservativetransparency.org/donor/f-m-kirby-foundation/",
            "http://conservativetransparency.org/donor/william-e-simon-foundation/",
            "http://conservativetransparency.org/donor/smith-richardson-foundation/",
            ]
    base = csv_filename.split("/")[-1]
    donor_slug = re.match("[a-z-]+[a-z]", base).group(0)
    for url in urls:
        if donor_slug in url:
            return url
    raise ValueError("Unknown donor: %s not among the donors for which we know URLs" % csv_filename)


def mysql_quote(x):
    '''
    Quote the string x using MySQL quoting rules. If x is the empty string,
    return "NULL". Probably not safe against maliciously formed strings, but
    whatever; our input is fixed and from a basically trustable source..
    '''
    if not x:
        return "NULL"
    x = x.replace("\\", "\\\\")
    x = x.replace("'", "''")
    x = x.replace("\n", "\\n")
    return "'{}'".format(x)


if __name__ == "__main__":
    main()
