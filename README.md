# Blockchain_Wallet

This is a blockchain wallet Fintech Finder demonstration app in the form 
of a Fintech client looking to hire professionals.

The application imports ethereum wallet functions (generate account, get balance, send transaction) from 'crypto_wallet.py'


<br/>

----

## Technologies

This application uses the following package:

* [Streamlit](https://streamlit.io)

This application uses Ganache as the 'local' Ethereum blockchain network for testing purpose.

* [Ganache](https://trufflesuite.com/ganache/)

<br/>

---

## Usage

In Windows GitBash or Mac Terminal app, run "streamlit run fintech_finder.py". This will launch the default browser showing the Fintech Finder application.

The mnemonic seed phrase (provided by Ganache) must be included in the .env text file in the following format:

        MNEMONIC = 'MNEMONIC SEED PHRASE HERE FROM GANACHE'


The application user interface in Streamlit. This screen showed a payment has been made by Client to Lane for an amount of 6 Ether.
![image1](transaction_images/image1.png)

<br/>

The client's and the Professionals wallets is shown under the ACCOUNTS tab in Ganache. 
![image2](transaction_images/image2.png)

<br/>

The transaction and the associated hash can be seen at the TRANSACTIONS tab in Ganache.
![image 3](transaction_images/image3.png)


<br/>

This image shows the details of the first transaction/payment.
![image 4](transaction_images/image4.png)


<br/>

---

## Contributors

This application is written by James Tan, with code snippets provided UBC Extension.

<br/>

---

## License

MIT.