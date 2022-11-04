# from importlib.util import spec_from_file_location, module_from_spec
# import os
# import sys
# from os.path import dirname, abspath
#
#
# def load_db_driver(db_type):
#     db_dir = os.path.join(dirname(abspath(__file__)), 'db')
#     spec = spec_from_file_location(db_type, os.path.join(db_dir, db_type + "_db.py"))
#     db_driver = module_from_spec(spec)
#     sys.modules[f"$(db_type)_db"] = db_driver
#     spec.loader.exec_module(db_driver)
#     return db_driver

from platzky.db import json_file_db, graph_ql_db, google_json_db


def load_db_driver(db_type):
    db_type_to_db_loader = {
        "json_file": json_file_db,
        "google_json": google_json_db,
        "graph_ql": graph_ql_db
    }

    return db_type_to_db_loader[db_type]
