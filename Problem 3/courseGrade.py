def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    filename = input()
    newfile = 'report.text'
    
    midterm_1 = 0
    midterm_2 = 0
    finalt = 0
      
      
    # TODO: Read a file name from the user and read the tsv file here.
    with open (filename, 'r') as file:
        data = file.readlines()
        
        for i in data:
            colums = data.split('\t')
            last_name = colums[0]
            first_name = colums[1]
            mt1 = int(colums[2])
            midterm_1 += mt1
            mt2 = int(colums[3])
            midterm_2 += mt2
            final = int(colums[4])
            finalt += final
           
        
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    avg = (mt1 +mt2 + final)/3
    if avg >= 90:
        letter = 'A'
    elif avg >= 80:
        letter = 'B'
    elif avg >= 70:
        letter = 'C'
    elif avg >= 60:
        letter = 'D'
    else:
        letter = 'F'
        print(last_name,first_name,mt1,mt2,final,letter)
     
    mid1_avg = midterm_1/len(file)
    mid2_avg = midterm_2/len(file)
    final_avg = finalt/len(file)
    print("Averages: midterm1 {:.2f}, midterm2 {:.2f}, final {:.2f}".format(mid1_avg,mid2_avg,final_avg))
    return

if __name__ == "__main__":
    courseGrade()
    
    