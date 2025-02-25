# Blockchain Cryptocurrency Wallet

################################################################################
# This is a blockchain wallet Fintech Finder demonstration app in the form 
# of a Fintech client looking to hire professionals.
# 
# Ganache is used to establish a local ethereum blockchain network for the purpose of
# testing the application

################################################################################
# Imports
import streamlit as st
from hexbytes import HexBytes
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

from crypto_wallet import generate_account
from crypto_wallet import get_balance
from crypto_wallet import send_transaction

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xEf52D6342d04477d38113bafFf7fF7E54999C167", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0xd86eB4993D061742788a40ADE330f3c8cafB1440", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0xdeE1A999928935fa74f1de5305E78C318eF2f605", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x60d685f7B624E41B128780345380c259ADAa4b68", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s HD wallet and Ethereum account.

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Define a new `st.sidebar.write` function that will display the balance of the
# client’s account. Inside this function, call the `get_balance` function and
# pass it client's Ethereum `account.address`.

# Call `get_balance` function and pass it the client's account address
# Write the returned ether balance to the sidebar

# streamlit placeholder for balance variable
bal_p = st.sidebar.empty()    

balance = get_balance(w3, account.address)
# st.sidebar.write(balance)
bal_p.write(balance)

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Total Wage in Ether to the sidebar
st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Sign and Execute a Payment Transaction

# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
wage = hourly_rate * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

##########################################
# * Call the `send_transaction` function and pass it three parameters:
    # - Client's Ethereum `account` information
    # - The `candidate_address` 
    # - The `wage` value. 

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.

if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(HexBytes.hex(transaction_hash))

    # Update balance in client's account
    balance = get_balance(w3, account.address)
    bal_p.write(balance)

    # Show successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people(w3)


