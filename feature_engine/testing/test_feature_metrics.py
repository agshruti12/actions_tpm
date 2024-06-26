import pytest
import pandas as pd
import numpy as np
from numpy import nan
import logging

test_chat_df =  pd.read_csv("../output/chat/reddit_test_chat_level.csv")
test_conv_df =  pd.read_csv("../output/conv/test_turn_taking_conversation_level.csv")

with open('test.log', 'w'):
    pass

@pytest.mark.parametrize("row", test_chat_df.iterrows())
def test_chat_unit_equality(row):
    actual = row[1][row[1]['expected_column']]
    expected = row[1]['expected_value']
    
    try:
        assert actual == expected
    except AssertionError:

        with open('test.log', 'a') as file:
            file.write("\n")
            file.write("------TEST FAILED------\n")
            file.write(f"Testing {row[1]['expected_column']} for message: {row[1]['message_original']}\n")
            file.write(f"Expected value: {expected}\n")
            file.write(f"Actual value: {actual}\n")

        raise  # Re-raise the AssertionError to mark the test as failed


@pytest.mark.parametrize("conversation_num, conversation_rows", test_conv_df.groupby('conversation_num'))
def test_conv_unit_equality(conversation_num, conversation_rows):
    test_failed = False
    expected_out = ""
    actual_out = ""

    for _, row in conversation_rows.iterrows():
        actual = row[row['expected_column']]
        expected = row['expected_value']
    
    try:
        assert actual == expected
    except AssertionError:
        expected_out = expected
        actual_out = actual
        test_failed = True

    if test_failed:
        with open('test.log', 'a') as file:
            file.write("\n")
            file.write("------TEST FAILED------\n")
            file.write(f"Testing {row['expected_column']} for conversation_num: {conversation_num}\n")
            file.write(f"Expected value: {expected_out}\n")
            file.write(f"Actual value: {actual_out}\n")

        raise
