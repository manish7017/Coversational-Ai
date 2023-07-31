from bardapi import Bard
import os
import time

os.environ[
    "_BARD_API_KEY"
] = "----------"  # Enter your _Secure-1PSID from www.bard.google.com -> Inspect -> Application -> Cookies

input_text = input("Ask Me Anything!!!  \n")
output_text = Bard().get_answer(input_text)["content"]

with open("myfile.txt", "w") as file1:
    file1.write(input_text + "\n")
    file1.write(output_text)
