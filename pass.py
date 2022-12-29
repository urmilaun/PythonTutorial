def seq():
    sequence = {"Python", "Pass", "Statement", "Placeholder"}  
    for value in sequence:  
        if value == "Pass":  
            pass # leaving an empty if block using the pass keyword  
        else:  
            print("Not reached pass keyword: ", value)  
seq()