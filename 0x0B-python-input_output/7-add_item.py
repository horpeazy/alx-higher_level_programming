#!/usr/bin/python3
sys = __import__("sys")
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

new_list = []
for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

try:
    old_list = load_from_json_file("add_item.json")
    old_list.extend(new_list)
    save_to_json_file(old_list, "add_item.json")
except Exception:
    save_to_json_file(new_list, "add_item.json")
