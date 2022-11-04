import os
import csv
import json
import hashlib

# collect Input for csv and json files

csvinput = str(input('Enter csv file path : '))

def welcome():
    print('Welcome to Nft-Projects')
    # Check if file is a csv file

    with open(csvinput) as file:
        if file.read(1) in '{[':
            print('oops , seems like file isnt a csv file ,its likely JSON please try again')
        else:
            file.seek(0)
            reader = csv.reader(file)
            try:
                if len(next(reader)) == len(next(reader)) > 1:
                    print('This is a csvfile')
            except StopIteration:
                pass


# func split_attrib: to split the attributes in the csv file

def split_attrib(attr):
    i = 0
    attrs = []
    new_attr = attr.split(';')
    for val in new_attr:
        splited = val.split(':')
        attrs.append({'trait_type': splited[0], 'value': splited[0]})
    return attrs


# func(hashedkey): creates hash keys for each json file

def hashedkey(filename):
    hashvalue = hashlib.sha256(filename.encode())
    return hashvalue.hexdigest()


# func(make_record): create CH-0007 Json Format

def make_record(row):
    return {
        'format': 'CHIP-0007',
        'name': row['Name'],
        'description': row['Description'],
        'minting_tool': row['TEAM NAMES'],
        'sensitive_content': False,
        'series_number': int(row['Series Number']),
        'series_total': 420,
        'gender': row['Gender'],
        'attributes': [split_attrib(row['attributes'])],
        'collection': {'name': 'Zuri NFT Tickets for Free Lunch',
                       'id': 'b774f676-c1d5-422e-beed-00ef5510c64d',
                       'attributes': [{'type': 'description',
                       'value': 'Rewards for accomplishments during HNGi9.'
                       }]},
        }

    print('CH-007 format successfully created')

''' 
    /* This function does the following :-
    /* Create a folder 'jsonfiles' if file does not exist
    /* Read csv file collected as input 
    /* Create json files from each row in the csv
    /* Create a new csv file with jsonfile hashedkey added as a new column
        
'''

def run(inputfile, outputfile):
    if not os.path.exists('jsonfiles'):
        os.mkdir('jsonfiles')

    with open(inputfile, 'r') as csvfile:
        with open(outputfile, 'w') as write_csv:
            reader = csv.DictReader(csvfile)
            fields = reader.fieldnames + ['HASH_SHA256']
            csv_writer = csv.DictWriter(write_csv, fields)
            csv_writer.writeheader()
            lcount = 0

            for row in reader:
                dump = make_record(row)
                filename = 'jsonfiles/' + row['Filename'] + '.json'
                newline = hashedkey(filename)
                dump['Hash'] = newline
                out = json.dumps(dump, indent=4)
                jsonoutput = open(filename, 'w')
                jsonoutput.write(out)
                lcount += 1
                jsonoutput.close()
                row['HASH_SHA256'] = str(newline)
                csv_writer.writerow(row)

    print('Operation completed Succesfully')


if __name__ == '__main__':
    welcome()
    run(csvinput, csvinput.replace('.csv', '.output.csv'))
