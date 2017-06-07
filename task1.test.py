__author__ = 'dinesh'

from task1 import compute_hash, compute_string


print compute_string(compute_hash("dines")) == "dines"
print compute_string(compute_hash("acdegilmnoprstuw")) == "acdegilmnoprstuw"
print compute_string(compute_hash("")) == ""
print compute_string(compute_hash("lotra")) == "lotra"
print compute_string(compute_hash("program")) != "programs"
print compute_string(compute_hash("cut")) == "cut"
print compute_string(compute_hash("aaaaaaaaaaaaaa")) == "aaaaaaaaaaaaaa"
print compute_string(compute_hash("wwww")) != "www"