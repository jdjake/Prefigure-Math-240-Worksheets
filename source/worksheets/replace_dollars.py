import re

def replace_dollars(string):
  a_list = string.split("$")

  new_string = a_list[0]
  for i in range(1,len(a_list)-1):
    if i % 2 == 1:
      new_string += "<m>" + a_list[i]
    else:
      new_string += "</m>" + a_list[i]
  new_string += "</m>" + a_list[-1]

  return new_string

def replace_brackets(string):
  return string.replace("\\[","<me>").replace("\\]","</me>")

def replace_bb(string):
  return string.replace("\\mathbb{R}","\\R").replace("\\mathbb{Z}","\\Z").replace("\\mathbb{N}","\\N").replace("\\mathbb{Q}","\\Q")

def replace_less_than(string):
  return string.replace("<", "\\lt")

file = open("worksheet8Latex","r+")
file_string = file.read()
file.close()
file = open("worksheet8Latex","r+")
file.write(replace_bb(replace_brackets(replace_dollars(replace_less_than(file_string)))))
print(replace_dollars(file_string))