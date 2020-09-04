from os import system, name
import sys
import time
import os
import shutil

default_cc = """
8107EC40 0000
8107EC42 FF00
8107EC38 0000
8107EC3A FF00
8107ECA0 7306
8107ECA2 0000
8107EC98 3903
8107EC9A 0000
8107EC88 FEC1
8107EC8A 7900
8107EC80 7F60
8107EC82 3C00
8107EC58 FFFF
8107EC5A FF00
8107EC50 7F7F
8107EC52 7F00
8107EC28 0000
8107EC2A 0000
8107EC68 2F0E
8107EC6A 0700
8107EC20 0000
8107EC22 0000
8107EC70 721C
8107EC72 0E00
"""

current_path = os.getcwd()
all_true_files=os.listdir(current_path)
#os.rename()

#list directories.

#uses the default color code if there isn't a color code(yes it checks everytime)

default_color_codes=default_cc.split("\n")

double_check=len(default_color_codes)

number_required = 0

not_safe = 0

useful_info666 = ""

while number_required < double_check:

  check_values=default_color_codes[number_required]

  if  check_values== '':

    number_required = number_required + 1

    not_safe = not_safe + 1
  
  if not check_values == '':

    number_required = number_required + 1

number_required99 = 0


while number_required99  < double_check:

  if default_color_codes[number_required99] == "":

    number_required99 = number_required99 + 1

  if not default_color_codes[number_required99] == "":

    break

while number_required99 < len(default_color_codes):

  required_info = (default_color_codes[number_required99]+"\n")

  useful_info666 = useful_info666+required_info
    

  number_required99 = number_required99 + 1

default_cc99 = str(useful_info666)

default_cc99=default_cc99.strip()

#it's here so you don't need to worry about Possible issues.


class Logger():
    stdout = sys.stdout
    messages = []

    def start(self): 
        sys.stdout = self

    def stop(self): 
        sys.stdout = self.stdout

    def write(self, text): 
        self.messages.append(text)

log = Logger()

log.start()

# define our clear function 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#Thank you https://www.geeksforgeeks.org/clear-screen-python/

can_countie= os.path.exists("color_code.txt")

if can_countie == True:

  run_rest = "True"

if can_countie == False:

  print("\n Since Color_code.txt was non existence, it's using a default color code.)")

  complete_color_code_998 = open("color_code.txt", "w")
  complete_color_code_998.close()

  run_rest = "True"


if run_rest == "True":

  if os.stat("color_code.txt").st_size == 0:

    file_required = open("color_code.txt","w")
    file_required.write(default_cc99)
    file_required.close()

  complete_color_code_99 = open("color_code.txt", "r")

  lines = complete_color_code_99.readlines()


  #insert the color code into the color_code.txt file.

  clear()

  #function version: https://repl.it/@JDJGInc_Offical/InvertRecolorProgram-function#main.py

  #the first digits like 8(refer to N64 usually, the only color bit is the 4 digits on the right.... - we still need to reinsert them imnto memory)

  #explained to me by: https://www.youtube.com/watch?v=5lZ31AlgNzw



  Inverted_color_code = [
    
  ]

  Inverted_color_code_inverted = [
    
  ]

  #here to check if both color codes match

  start_needed = ""

  times_running64 = 0

  while times_running64 < len(lines):

    needed_file=lines[times_running64]

    start_needed = start_needed+needed_file

    times_running64 = times_running64 + 1


  #used orginally when the color code was in the main.py

  times_ran_1 = 0

  complete_color_code = str(start_needed)

  complete_color_code_99.close()

  lines=complete_color_code.split("\n")


  while times_ran_1 < len(lines):

    if '' == lines[times_ran_1]:

      times_ran_1 = times_ran_1+1

      Inverted_color_code.append('')

      Inverted_color_code_inverted.append('')

      #it should always be correct, unless the hexcode doesn't work, right

    if not '' == lines[times_ran_1]:

      break

  x = int(times_ran_1)

  color_counter = 0

  times_ran_program_1 = 0

  #to check to make sure it doesn't go over, and sees if the first slot has a blank spot or not(and finds the first one, without a blank spot)

  RGB_info = ""

  hexadecimal_info  = ""

  while x < len(lines):

    color_value = lines[x]

    color_value2 = lines[x+1]

    colored_bit=color_value.split(" ")

    colored_bit2 = color_value2.split(" ")

    color_code_front = colored_bit[0]

    color_code_front2 = colored_bit2[0]

    color_section = colored_bit[1]

    color_section2 = colored_bit2[1]


    r = int(color_section[0:2], 16)
    g = int(color_section[2:4], 16)
    b = int(color_section2[0:2], 16)

    hexadecimal_info = hexadecimal_info+"\nHexadecimal Value "+str(color_counter)+": #"+str(color_section[0:2])+str(color_section[2:4])+str(color_section2[0:2])

    RGB_info = RGB_info+"\nRGB Value "+str(color_counter)+": ("+str(r)+","+str(g)+","+str(b)+")"

    r = 0xFF - r
    g = 0xFF - g
    b = 0xFF - b

    #solution suggested by John10v10#5883

    bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

    first_color_line =  bits_used998[0:4].upper()

    second_color_line = bits_used998[4:6].upper()

    color_code_needed = color_code_front+" "+first_color_line

    color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]

    Inverted_color_code.append(color_code_needed)

    Inverted_color_code.append(color_code_needed_2)

    x = x +2

    color_counter = color_counter + 1

    times_ran_program_1 = times_ran_program_1 + 1

  print("all",x-times_ran_1,"of the color code lines ran!")

  times_ran_1 = 0


  while times_ran_1 < len(Inverted_color_code):

    if '' == Inverted_color_code[times_ran_1]:

      times_ran_1 = times_ran_1+1

    if not '' == Inverted_color_code[times_ran_1]:

      break

  z = int(times_ran_1)

  RGB_info99 = ""

  RGB_back99 = ""

  hexadecimal_info99 = ""

  hexadecimal_info98 = ""

  color_counter2 = 0

  while z < len(Inverted_color_code):

    color_value = Inverted_color_code[z]

    color_value2 = Inverted_color_code[z+1]

    colored_bit=color_value.split(" ")

    colored_bit2 = color_value2.split(" ")

    color_code_front = colored_bit[0]

    color_code_front2 = colored_bit2[0]

    color_section = colored_bit[1]

    color_section2 = colored_bit2[1]

    hexadecimal_info99 = hexadecimal_info99+"\nHexadecimal Value "+str(color_counter2)+": #"+str(color_section[0:2])+str(color_section[2:4])+str(color_section2[0:2])


    r = int(color_section[0:2], 16)
    g = int(color_section[2:4], 16)
    b = int(color_section2[0:2], 16)

    RGB_info99 = RGB_info99+"\nRGB Value "+str(color_counter2)+": ("+str(r)+","+str(g)+","+str(b)+")"

    r = 0xFF - r
    g = 0xFF - g
    b = 0xFF - b

    RGB_back99 = RGB_back99+"\nRGB Value "+str(color_counter2)+": ("+str(r)+","+str(g)+","+str(b)+")"

    #solution suggested by John10v10#5883

    bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

    hexadecimal_info98 = hexadecimal_info98+"\nHexadecimal Value "+str(color_counter2)+": #"+bits_used998

    first_color_line =  bits_used998[0:4].upper()

    second_color_line = bits_used998[4:6].upper()

    color_code_needed = color_code_front+" "+first_color_line

    color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]

    Inverted_color_code_inverted.append(color_code_needed)

    Inverted_color_code_inverted.append(color_code_needed_2)

    z = z +2

    color_counter2 = color_counter2 + 1


  if Inverted_color_code_inverted == lines:

    print("\nYour color code was succesfully inverted")

    want_it = "yes"

    want_it2 = "yes"

  if not Inverted_color_code_inverted == lines:

    print("\nColor failed....")

    want_it = "yes"

    want_it2 = "yes"




  j = int(times_ran_1)

  test_string99 = ""


  if want_it == "yes":

    print("\nInverted Color Code:")


    while j < len(Inverted_color_code):

      test_string99 = test_string99+(Inverted_color_code[j]+"\n")


      j = j + 1

    print(test_string99)

  jdjg = int(times_ran_1)

  if want_it2 == "yes":

    print("\nOrginal Color Code that was inverted and was inverted back: ")

    test_string = ""

    while jdjg < len(Inverted_color_code_inverted):

      test_string = test_string+(Inverted_color_code_inverted[jdjg]+"\n")

      jdjg = jdjg + 1

    print(test_string)

    print("\nOrginal color code:")



  jdjg_2 = times_ran_1

  test_string998 = ""

  while jdjg_2 < len(lines):

    test_string998 = test_string998+(lines[jdjg_2]+"\n")

    jdjg_2 = jdjg_2 + 1

  print(test_string998)

  if test_string == test_string998:

    print("\nran 100% succesfully")

  if not test_string == test_string998:

    print("\ndidn't run successfully")




  #Old inverters(don't work as well):

  #https://repl.it/@JDJGInc_Offical/RecolorInverter#main.py

  #https://repl.it/@JDJGInc_Offical/RecolorInverter-optimized

  path = os.getcwd()

  path99 = path+"/logs"

  path64 = path+"/inverted_colors"

  path_rgb = path+"/rgb_logs"

  path_hex = path+"/hexadecimal_logs"

  if os.path.exists(path99) == True:

    pass

  if os.path.exists(path99) ==False:

    try:
      os.mkdir(path99)
    except OSError:
        print ("Creation of the directory %s failed" % path99)
    else:
        print ("Successfully created the directory %s " % path99)

  if os.path.exists(path64) == True:

    pass

  if os.path.exists(path64) == False:

    try:
        os.mkdir(path64)
    except OSError:
        print ("Creation of the directory %s failed" % path64)
    else:
        print ("Successfully created the directory %s " % path64)

  if os.path.exists(path_rgb) == True:

    pass
  
  if os.path.exists(path_rgb) == False:
    try:
        os.mkdir(path_rgb)
    except OSError:
        print ("Creation of the directory %s failed" % path_rgb)
    else:
        print ("Successfully created the directory %s " % path_rgb)

  if os.path.exists(path_hex) == True:

    pass
  
  if os.path.exists(path_hex) == False:
    try:
        os.mkdir(path_hex)
    except OSError:
        print ("Creation of the directory %s failed" % path_hex)
    else:
        print ("Successfully created the directory %s " % path_hex)

  times_to_run = 0

  log.stop()

  final_console_output = ""

  while times_to_run < len(log.messages):

    final_console_output = final_console_output+log.messages[times_to_run]

    times_to_run = times_to_run + 1



  time_usage=time.struct_time(time.localtime())

  time_usage_formatted = time.strftime("\nCreation:[%m/%d/%Y, %H:%M:%S]",time_usage)


  f = open("logs/console_output.txt", "a")
  f.write(final_console_output)
  f.write(time_usage_formatted)
  f.write("\n")
  f.close()

  while True:

    g = open("inverted_colors/inverted_cc.txt","a")
    g.write("Inverted Color Code:\n")
    g.write(test_string99)
    g.write("\n")
    g.write(time_usage_formatted)
    g.write("\n")
    g.close()




    fo = open("logs/console_output99.txt", "w")
    fo.write(final_console_output)
    fo.write(time_usage_formatted)
    fo.close()

    go = open("inverted_colors/inverted_cc99.txt","w")
    go.write("Inverted Color Code:\n")
    go.write(test_string99)
    go.write("\n")
    go.write(time_usage_formatted)
    go.close()

    rgb_log_one = open("rgb_logs/orginal_cc.txt","a")
    rgb_log_one.write("Orginal Color code(RGB): \n")
    rgb_log_one.write(RGB_info)
    rgb_log_one.write("\n")
    rgb_log_one.write(time_usage_formatted)
    rgb_log_one.write("\n")
    rgb_log_one.close()

    rgb_log_one_99 = open("rgb_logs/orginal_cc99.txt","w")
    rgb_log_one_99.write("Orginal Color code(RGB): \n")
    rgb_log_one_99.write(RGB_info)
    rgb_log_one_99.write("\n")
    rgb_log_one_99.write(time_usage_formatted)
    rgb_log_one_99.close()

    rgb_log_two = open("rgb_logs/inverted_cc.txt","a")
    rgb_log_two.write("Inverted Color code(RGB): \n")
    rgb_log_two.write(RGB_info99)
    rgb_log_two.write("\n")
    rgb_log_two.write(time_usage_formatted)
    rgb_log_two.write("\n")
    rgb_log_two.close()

    rgb_log_two_99 = open("rgb_logs/inverted_cc99.txt","w")
    rgb_log_two_99.write("Inverted Color code(RGB): \n")
    rgb_log_two_99.write(RGB_info99)
    rgb_log_two_99.write("\n")
    rgb_log_two_99.write(time_usage_formatted)
    rgb_log_two_99.close()

    rgb_log_three = open("rgb_logs/inverted_back.txt","a")
    rgb_log_three.write("Inverted Back to orginal(RGB): \n")
    rgb_log_three.write(RGB_back99)
    rgb_log_three.write("\n")
    rgb_log_three.write(time_usage_formatted)
    rgb_log_three.write("\n")
    rgb_log_three.close()

    rgb_log_three_99 = open("rgb_logs/inverted_back99.txt","w")
    rgb_log_three_99.write("Inverted Back to orginal(RGB): \n")
    rgb_log_three_99.write(RGB_back99)
    rgb_log_three_99.write("\n")
    rgb_log_three_99.write(time_usage_formatted)
    rgb_log_three_99.close()

    hex_log_one = open("hexadecimal_logs/orginal_color_code.txt","a")
    hex_log_one.write("Orginal Color Code (Hexadecimal):\n")
    hex_log_one.write(hexadecimal_info)
    hex_log_one.write("\n")
    hex_log_one.write(time_usage_formatted)
    hex_log_one.write("\n")
    hex_log_one.close()

    hex_log_two = open("hexadecimal_logs/inverted_color_code.txt","a")
    hex_log_two.write("Inverted Color Code (Hexadecimal):\n")
    hex_log_two.write(hexadecimal_info99)
    hex_log_two.write("\n")
    hex_log_two.write(time_usage_formatted)
    hex_log_two.write("\n")
    hex_log_two.close()

    hex_log_three = open("hexadecimal_logs/inverted_again_color_code.txt","a")
    hex_log_three.write("Inverted Back Color Code (Hexadecimal):\n")
    hex_log_three.write(hexadecimal_info98)
    hex_log_three.write("\n")
    hex_log_three.write(time_usage_formatted)
    hex_log_three.write("\n")
    hex_log_three.close()

    hex_log_one_99 = open("hexadecimal_logs/orginal_color_code99.txt","w")
    hex_log_one_99.write("Orginal Color Code (Hexadecimal):\n")
    hex_log_one_99.write(hexadecimal_info)
    hex_log_one_99.write("\n")
    hex_log_one_99.write(time_usage_formatted)
    hex_log_one_99.close()

    hex_log_two_99 = open("hexadecimal_logs/inverted_color_code99.txt","w")
    hex_log_two_99.write("Inverted Color Code (Hexadecimal):\n")
    hex_log_two_99.write(hexadecimal_info99)
    hex_log_two_99.write("\n")
    hex_log_two_99.write(time_usage_formatted)
    hex_log_two_99.close()

    hex_log_three_99 = open("hexadecimal_logs/inverted_again_color_code99.txt","w")
    hex_log_three_99.write("Inverted Back Color Code (Hexadecimal):\n")
    hex_log_three_99.write(hexadecimal_info98)
    hex_log_three_99.write("\n")
    hex_log_three_99.write(time_usage_formatted)
    hex_log_three_99.close()

    print("\ntype clear to clear the text files.. or clear all to clear the text files and the color_code.txt( will not work without a color code) or you can always use delete all, use print to print the contents of the console.")

    clear_files_option=input("\npress any button to close this window: ")

    break

  if clear_files_option.lower() == "clear":

    g2  = open("inverted_colors/inverted_cc.txt","w")
    g2.truncate()
    g2.close()

    f2 = open("logs/console_output.txt","w")
    f2.truncate()
    f2.close()

    fo2 = open("logs/console_output99.txt","w")
    fo2.truncate()
    fo2.close()

    go2 = open("inverted_colors/inverted_cc99.txt","w")
    go2.truncate()
    go2.close()

    rgb_log_one = open("rgb_logs/orginal_cc.txt","w")
    rgb_log_one.truncate()
    rgb_log_one.close()

    rgb_log_one_99 = open("rgb_logs/orginal_cc99.txt","w")
    rgb_log_one_99.truncate()
    rgb_log_one_99.close()

    rgb_log_two = open("rgb_logs/inverted_cc.txt","w")
    rgb_log_two.truncate()
    rgb_log_two.close()

    rgb_log_two_99 = open("rgb_logs/inverted_cc99.txt","w")
    rgb_log_two_99.truncate()
    rgb_log_two_99.close()

    rgb_log_three = open("rgb_logs/inverted_back.txt","w")
    rgb_log_three.write("\n")
    rgb_log_three.truncate()
    rgb_log_three.close()

    rgb_log_three_99 = open("rgb_logs/inverted_back99.txt","w")
    rgb_log_three_99.truncate()
    rgb_log_three_99.close()

    hex_log_one = open("hexadecimal_logs/orginal_color_code.txt","w")
    hex_log_one.truncate()
    hex_log_one.close()

    hex_log_two = open("hexadecimal_logs/inverted_color_code.txt","w")
    hex_log_two.truncate()
    hex_log_two.close()

    hex_log_three = open("hexadecimal_logs/inverted_again_color_code.txt","w")
    hex_log_three.truncate()
    hex_log_three.close()


    hex_log_one_99 = open("hexadecimal_logs/orginal_color_code99.txt","w")
    hex_log_one_99.truncate()
    hex_log_one_99.close()


    hex_log_two_99 = open("hexadecimal_logs/inverted_color_code99.txt","w")
    hex_log_two_99.truncate()
    hex_log_two_99.close()


    hex_log_three_99 = open("hexadecimal_logs/inverted_again_color_code99.txt","w")
    hex_log_three_99.truncate()
    hex_log_three_99.close()


  if clear_files_option.lower() == "clear all":

    g2  = open("inverted_colors/inverted_cc.txt","w")
    g2.truncate()
    g2.close()

    f2 = open("logs/console_output.txt","w")
    f2.truncate()
    f2.close()

    fo2 = open("logs/console_output99.txt","w")
    fo2.truncate()
    fo2.close()

    go2 = open("inverted_colors/inverted_cc99.txt","w")
    go2.truncate()
    go2.close()

    color_code_deleter = open("color_code.txt","w")
    color_code_deleter.truncate()
    color_code_deleter.close()

    rgb_log_one = open("rgb_logs/orginal_cc.txt","w")
    rgb_log_one.truncate()
    rgb_log_one.close()

    rgb_log_one_99 = open("rgb_logs/orginal_cc99.txt","w")
    rgb_log_one_99.truncate()
    rgb_log_one_99.close()

    rgb_log_two = open("rgb_logs/inverted_cc.txt","w")
    rgb_log_two.truncate()
    rgb_log_two.close()

    rgb_log_two_99 = open("rgb_logs/inverted_cc99.txt","w")
    rgb_log_two_99.truncate()
    rgb_log_two_99.close()

    rgb_log_three = open("rgb_logs/inverted_back.txt","w")
    rgb_log_three.truncate()
    rgb_log_three.close()

    rgb_log_three_99 = open("rgb_logs/inverted_back99.txt","w")
    rgb_log_three_99.truncate()
    rgb_log_three_99.close()

    hex_log_one = open("hexadecimal_logs/orginal_color_code.txt","w")
    hex_log_one.truncate()
    hex_log_one.close()

    hex_log_two = open("hexadecimal_logs/inverted_color_code.txt","w")
    hex_log_two.truncate()
    hex_log_two.close()

    hex_log_three = open("hexadecimal_logs/inverted_again_color_code.txt","w")
    hex_log_three.truncate()
    hex_log_three.close()


    hex_log_one_99 = open("hexadecimal_logs/orginal_color_code99.txt","w")
    hex_log_one_99.truncate()
    hex_log_one_99.close()


    hex_log_two_99 = open("hexadecimal_logs/inverted_color_code99.txt","w")
    hex_log_two_99.truncate()
    hex_log_two_99.close()


    hex_log_three_99 = open("hexadecimal_logs/inverted_again_color_code99.txt","w")
    hex_log_three_99.truncate()
    hex_log_three_99.close()

  if clear_files_option.lower() == "delete all":

    for root, dirs, files in os.walk(os.getcwd()+"/logs"):
      for f in files:
          os.unlink(os.path.join(root, f))
      for d in dirs:
          shutil.rmtree(os.path.join(root, d))

    os.rmdir(os.getcwd()+"/logs")

    for root, dirs, files in os.walk(os.getcwd()+"/rgb_logs"):
      for f in files:
          os.unlink(os.path.join(root, f))
      for d in dirs:
          shutil.rmtree(os.path.join(root, d))

    os.rmdir(os.getcwd()+"/rgb_logs")

    for root, dirs, files in os.walk(os.getcwd()+"/inverted_colors"):
      for f in files:
        os.unlink(os.path.join(root, f))
      for d in dirs:
        shutil.rmtree(os.path.join(root, d))

    os.rmdir(os.getcwd()+"/inverted_colors")

    os.remove("color_code.txt")

    for root, dirs, files in os.walk(os.getcwd()+"/hexadecimal_logs"):
        for f in files:
          os.unlink(os.path.join(root, f))
        for d in dirs:
          shutil.rmtree(os.path.join(root, d))

    os.rmdir(os.getcwd()+"/hexadecimal_logs")

  if clear_files_option.lower() == "print":

    print("\nPrinting contents of Console....")

    print_content = 0

    string_to_use = ""

    while print_content < len(log.messages):

      string_to_use=string_to_use+(log.messages[print_content])

      print_content = print_content + 1

    print("\n")
    print(string_to_use)
