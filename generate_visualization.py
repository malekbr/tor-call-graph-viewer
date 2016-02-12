#!/usr/bin/env python
'''Generates graphical visualization data of callgraph.'''
import json
import sys

def filter_callgraph(callgraph):
    '''Filters the callgraph such that only defined methods are present.'''
    return {caller:
            [callee for callee in callgraph[caller] if callee in callgraph]
            for caller in callgraph}

def format_for_json(callgraph):
    '''Formats the data to be exported to JSON.'''
    return [{
        'name': caller,
        'calls': callgraph[caller]
    } for caller in callgraph]

def main():
    pickle_path = 'callgraph_full.txt'
    if len(sys.argv) == 2:
        pickle_path = sys.argv[1]
    elif len(sys.argv) > 2:
        print >> sys.stderr, ("Only accept at most one argument, specifying "
            "the path for the pickle file to load.")
    with open(pickle_path, 'r') as pickle_file:
        data = eval(pickle_file.read())
    print 'Filtering the data...'
    filtered_data = filter_callgraph(data['callgraph'])
    print 'Formatting data...'
    formatted_data = format_for_json(filtered_data)
    with open('callgrah_data.json', 'w+') as output_file:
        json.dump(formatted_data, output_file)

if __name__ == '__main__':
    main()
