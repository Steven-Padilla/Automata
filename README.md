#What is this automata for
This automata takes a folder with files (activities made by students from the universidad Politécnica de Chiapas), these files should be named with the followings rules:
 ***ID_lastname1_lastname2.C(number 1-3).A(number 1-9).pdf***
 1. First 6 symbols (id), are the id from the universidad politecnica de chiapas -id's from 2018 to 2022- plus divider ("_"," ")
 2. Now, we have last names (two), separated with the dividers : (" ","_")  *LAST NAMES HAVE TO BE UPPERCASE*
 *Last names need to have at least 3 letters*
 3. Next to the second last name, we got a divider (same as the previos step, or  ".")
 4. Now,"C" or "c" that repesents in wich section of the four-month period was made the file, followed by a number from 1 to 3
 5. A divirder ("_",".") and an "A" or "a", followed by a number from 1-9 that represents the number of the activity.
 6. At last, it has to end with the extention ".pdf"
 
 Examples:
 203426 STEVEN_PADILLA.c3.a7.pdf 
 181900_RAMOS HERRERA_C1.A5.pdf
 222023_PEREZ_SAINS.C2_a9.pdf
 
# How to use it
1. Clone this repository
2. Install openpyxl
  $ pip install openpyxl 
3. Place the folder in the same folder where you have the program (file: prueba02.py)
4. Run the program
    $ python3 prueba02.py
    *try without the 3 in "python3" for linux and mac*
5. Congrats!! now you have a file .xlsx with the data 