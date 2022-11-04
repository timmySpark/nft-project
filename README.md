##  Nft-Project

A program that converts csv files into generated CH-007 compatible json format ,  it also calculates the SHA256 of all json files created and the results are added as a column in a new csv file 


##   Steps on How to Use This Script


i . Make sure you have python installed on your system
    
ii. Clone this github repo 

     git clone https://github.com/timmySpark/nft-project.git
    
iii. Navigate to the folder already cloned

     cd nft-project
     
iv.  Run the Script 

     python pyscripts.py
    
v. A folder `jsonfiles` is created in the `nft-project folder` where all the json files created are stored

vi. A new csvfile is created `filename.output.csv`(filename is the name of the csv file collected) where all rows are writted with an extra column containing the SHA256 of the generated json files
    


