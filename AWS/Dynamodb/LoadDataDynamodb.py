#!/usr/bin/env python3

# Loads Json files to dynamoDB

import decimal
import json

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float=decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("adding movie:", year, title)

        table.put_item(
                Item={
                    'year': year,
                    'title': title,
                    'info':info,
                    }
                )

