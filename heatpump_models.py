#!/usr/bin/env python3

import requests
import re
from rich.table import Table
from rich.console import Console

data = []

mfrs = [
    {"mfrid": 1, "manufacturer": "Alpha Innotec"},
    {"mfrid": 2, "manufacturer": "Siemens Novelan"},
    {"mfrid": 3, "manufacturer": "CTA"},
]


def get_vendor_types():
    """Scrapes all Heatpump types togehther with their IDs from the downloads page"""
    for mfr in mfrs:
        r = requests.get(
            f"https://www.heatpump24.com/DownloadArea.php?layout={mfr['mfrid']}&lang=5"
        )
        typeids = re.findall(
            r"<option value='(?P<id>\d+)'>(?P<type>[^<]*)</option>", r.text
        )
        for typeid, type in typeids:
            data.append(
                {
                    "manufacturer": mfr["manufacturer"],
                    "manufacturer_id": mfr["mfrid"],
                    "type_id": typeid,
                    "type": type,
                }
            )

            
def get_details():
    for heatpump in data:
        r = requests.post(
            "https://www.heatpump24.com/software/fetchSoftware.php",
            data={"idTyp": heatpump["type_id"]},
        )
        heatpump["models"] = r.json()

        
def dump_data():
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Manufacturer", style="dim")
    table.add_column("Manufacturer ID")
    table.add_column("Type")
    table.add_column("Type ID")
    table.add_column("Name")
    table.add_column("Article Number")
    table.add_column("Software")
    table.add_column("Eencoding")
    table.add_column("ID")
    for mfr in data:
        for model in mfr["models"]:
            table.add_row(
                mfr["manufacturer"],
                str(mfr["manufacturer_id"]),
                mfr["type"],
                str(mfr["type_id"]),
                model["name"],
                model["Art_Nr"],
                model["software"],
                model["encoding"],
                model["id"],
            )
    console.print(table)


get_vendor_types()
get_details()
dump_data()
