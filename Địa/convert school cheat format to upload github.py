# read input text from the shell
input_text = """

"""

# replace the numbered lines with arrows
output_text = input_text.replace("\n","\n\n\n").replace("\n1. ", "\n==> ")

# replace \n to none for ==>
output_text = output_text.replace("\n\n==>","==>")

# replace number to none
#for i in range(0,90):
#	output_text = output_text.replace(str(i)+". ", "")

# print the converted text to the shell
# print("Converted text:")
print(output_text)
