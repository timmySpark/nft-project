#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import json
import hashlib

# collect Input for csv and json files

csvinput = str(input('Enter csv file : '))
jsoninput = csvinput.replace('.csv', '_output.json')


# func split_attrib: to split the attributes in the csv file

def split_attrib(attr):
    i = 0
    new_attr = attr.split(';')
    for val in new_attr:
        splited = val.split(':')
        return{
            "trait_type":splited[0],
            "value":splited[1]
        }
    '''

    for (i, val) in enumerate(new_attr):
        if i > 7:
            break
        else:
            splited = val.split(':')

            # print (i, ",",splited , ',' , splited[0],',',splited[1])

            print ('trait_type', splited[0], ',', 'value', splited[1])
            i += 1
    '''

# func(make_record): create CH-0007 Json Format

def make_record(row):

    # print(row['attributes'])

    return {  # i want to get the length of all rows in the csv
              # Attributes is in object but it's to
        'format': 'CHIP-0007',
        'name': row['Name'],
        'description': row['Description'],
        'minting_tool': row['TEAM NAMES'],
        'sensitive_content': False,
        'series_number': int(row['Series Number']),
        'series_total': len(row),
        'gender': row['Gender'],
        'attributes': [split_attrib(row['attributes']),
                       {'trait_type': '', 'value': ''}],
        'collection': {'name': '', 'id': '', 'attributes': [{'type': ''
                       ,
                       'value': 'Rewards for accomplishments during HNGi9.'
                       }]},
        }


# func(hashedkey): creates hash keys for json files

def hashedkey(filename):
    hashvalue = hashlib.sha256(filename.encode())
    return hashvalue.hexdigest()


# func(add_column_in_csv): with inputs from the fuction below ,
# read csv collected as input and write in a new csv file
# with Hash as an extra column

def add_column_in_csv(inputfile, outputfile):
    with open(inputfile, 'r') as read_csv:
        with open(outputfile, 'w', newline='') as write_csv:

            # Create a csv.reader object from the input file object

            csv_reader = csv.reader(read_csv)

            # Create a csv.writer object from the output file object

            csv_writer = csv.writer(write_csv)

            count = 0
            i = 0
            for row in csv_reader:
                if count == 0:
                    row.append('Hash')
                # else:
                    # while i < len(hashes):
                    #     row.append(hashes[i])

                    # row.append(newcolumn)
                csv_writer.writerow(row)
                count += 1


# Read csv file collected as input ,
# create json files from each row in the csv

with open(csvinput, 'r') as csvfile:

    reader = csv.DictReader(csvfile)

    lcount = 0

    for row in reader:

        dump=make_record(row)
        filename = row['Filename'] + '.json'
        newline = hashedkey(filename)
        dump['Hash'] = newline
        out = json.dumps(dump, indent=4)
        jsonoutput = open(filename, 'w')
        jsonoutput.write(out)


        lcount += 1

        # print(newline)

    add_column_in_csv(csvinput, 'output.csv')

    jsonoutput.close()
