# Head-to-Head Chart Python Solution
 ## Top Level
 The following solution to the interview question contains one main function, print_h2h_table, which
 prints a head-to-head table of wins from a JSON file. The function is comprised of two loops moving 
 through dictionaries of data generated by the Python JSON parsing from the json module.
 ## Process
 The function, print_h2h_table, first opens a json file, parses it, and prints the data in a table
 to the console using formatted strings. The format strings, demonstrated first on line 18, are used 
 to create a dynamically sized table based on the number of teams from the JSON data. The strings are 
 also right justified to the size of five spaces to make the table readable. The main printing element 
 of the function is comprised of two loops with the outer loop indexed by i and the inner loop indexed 
 by j. The outer loop initializes a list of results (named results) which holds each piece of win data
 for the team currently being read from, along with the three letter team code for the beginning of each
 row in the table. The inner loop then checks if the indicies are equal (to input the '--') and then
 grabs the win data for each team, appending the results to the results array. Finally, for each outer 
 loop iteration, a row is printed to the console.
 ## Constraints
 The function does not check if the JSON file is either valid JSON, nor if the file has proper team data.
 The inputted data is assumed to be reflective of the example data. 
 ## Example
 Here is an example of the outputted data with the training data.
 ![Example table, rendered in IDLE](https://github.com/moria161/HeadToHeadTableGen/blob/main/example_table.png?raw=true)
