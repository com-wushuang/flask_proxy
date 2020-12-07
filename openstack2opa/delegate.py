import json

with open("../test/keystone_policy.json", "r") as load_f:
    load_dict = json.load(load_f)
    for ke in load_dict:
        load_dict[ke] = "http://policy.delegate.server:1323/stack/policy/check"
with open("../test/policy.json", "w") as dump_f:
    json.dump(load_dict, dump_f)
