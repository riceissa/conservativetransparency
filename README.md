# conservativetransparency.org processing

This is for Vipul Naik's [Donations List Website](https://github.com/vipulnaik/donations).

See https://github.com/vipulnaik/donations/issues?utf8=%E2%9C%93&q=conservativetransparency.org for the issues on DLW repo.

## Instructions for doing a run

First, go to the conservativetransparency.org page for the donor, e.g. http://conservativetransparency.org/donor/earhart-foundation/

Download the CSV file by clicking on "Export CSV".

Save the CSV file in the `data/` directory. Make sure that the slug for the
donor (e.g. `earhart-foundation`) is at the start of the CSV file name (e.g.
`earhart-foundation-2019-01-20-0-37-49.csv`); this is how we identify which CSV
goes with which URL.

If this was a new donor/URL, then record the URL in `proc.py`.

To get the SQL, run like this:

```bash
./proc.py data/earhart-foundation-2019-01-20-0-37-49.csv > blah.sql
```
