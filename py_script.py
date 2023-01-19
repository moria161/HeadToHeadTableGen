import json

def print_h2h_table(fname):

    # open file
    f = open(fname)
    
    # load json
    data_as_dict = json.loads(f.read())

    # close file
    f.close()

    # get proper team order from json
    order = list(data_as_dict.keys())

    # print formatted top line
    top_line = "{:>5}"*(len(order)+1) # add one more format here for 'Tm'
    print(top_line.format('Tm',*order)) # print 'Tm' and order (in-line)

    i = 0
    for i in range(len(order)): # to grab each team's full data
        j = 0
        team_dict = data_as_dict[order[i]] # get team dict from data with title from order
        results = [order[i]] # declare results array with title at the start
        for j in range(len(order)): # to grab each team's head-to-head data
            if i == j:
                results.append('--') # if same team, insert '--'
                continue
            matchup_dict = team_dict[order[j]] # get matchup data (as dict)
            results.append(matchup_dict['W']) # add wins number to results array

        # for each team, print out results array 
        out = "{:>5}"*len(results) 
        print(out.format(*results))

    #print out formatted bottom line, same as above
    bottom_line = "{:>5}"*(len(order)+1)
    print(bottom_line.format('Tm',*order))
        
if __name__ == "__main__":
    f = 'example.json'
    print_h2h_table(f)
