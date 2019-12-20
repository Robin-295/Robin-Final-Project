# Robin-Final-Project
 Robin Gardner's Programming Final

Welcome to Crypto-Source!

Getting started/running Crypto-Source-
	Running Crypto-Source to access the application is done through a command line interface. To get it started you need to first open your command line interface and activate virtual environment. You can do this by running the command source venv/bin/activate.
Once virtual environment is running, navigate to the directory where the app.py file is located, which is named "Crypto-Source". Once you've navigated to that directory you can run the application with the command "flask run". Once the application is running you can open it in your internet browser by typing http://127.0.0.1:5000/ into your browser's address bar. Once you've gotten to the Crypto-Source application you can use it. 

Key Generation-
	The first page Crypto-Source will open to is the page for key generation. Because Crypto-Source is a public-private key cipher, keys are in pairs of a public and private key. To generate a key pair all Crypto-Source needs as a user input are two unique prime numbers. You can enter the prime numbers you've chosen into each of the text boxes marked "First Prime Number" and "Second Prime Number". Once you've done that, all you need to do is click the "submit" button below these text boxes. Crypto-Source will then return your key pair. To use your key pair, first write down the values for both public and private keys, then navigate to the encryption page using the navigation bar at the top of the page. 

Encryption- 
	To encrypt a message Crypto-Source requires two inputs. The first is the public key that you've generated using Crypto-Source. The second is some plaintext to encrypt. To encrypt enter the public key pair into the corresponding text boxes in the encryption page. The public key is made up of two numbers. Type the first number in the box marked "E". Type the second number in the box marked "N". Once you've done that, type your plaintext that you would like to encrypt into the text box marked "Message to Encrypt". Finally click the submit button. Crypto-Source will then return your encrypted message. 

Decryption-
	To decrypt a message Crypto-Source still requires two inputs. This time it needs the private key you've generated. Enter the private key by typing the first number into the box marked "D". Then enter the second number into the box marked "N". Then enter the cipher text you would like to decrypt into the text box marked "Message to Decrypt". Then click the submit button and Crypto-Source will return your decrypted message. 