# (c) 2018-2019 Ionic Security Inc.
# By using this code, I agree to the Terms & Conditions (https://dev.ionic.com/use.html)
# and the Privacy Policy (https://www.ionic.com/privacy-notice/).

from __future__ import print_function

import os
import sys
import ionicsdk

file_original = '../../sample-data/files/Message.docx'
file_ciphertext = './Message-Protected.docx'
file_plaintext = './Message.docx'
source_dir = 'github-samples/python/crypto-file-cipher-openxml'
this_dir = os.getcwd()

# run only from source directory
if not this_dir.endswith(source_dir): 
    print("[!] Please run this sample from inside " + source_dir)
    sys.exit(1)

# read persistor password from environment variable
persistorPassword = os.environ.get('IONIC_PERSISTOR_PASSWORD')
if (persistorPassword == None):
    print("[!] Please provide the persistor password as env variable: IONIC_PERSISTOR_PASSWORD")
    sys.exit(1)

# initialize agent with password persistor
try:
    persistorPath = os.path.expanduser("~/.ionicsecurity/profiles.pw")
    persistor = ionicsdk.DeviceProfilePersistorPasswordFile(persistorPath, persistorPassword)
    agent = ionicsdk.Agent(None, persistor)
except ionicsdk.exceptions.IonicException as e:
    print("Error initializing agent: {0}".format(e.message))
    sys.exit(-2)

# define attributes (optional)
mutable_attributes = {
    "classification": "Restricted"
}   

# initialize aes cipher object
cipher = ionicsdk.FileCipherOpenXml(agent)

# encrypt
print("Encrypting message and saving to Ciphertext File: {}".format(file_ciphertext))
cipher.encrypt(file_original, file_ciphertext, mutableAttributes=mutable_attributes)

# decrypt
print("Decrypting ciphertext and saving to Plaintext File: {}".format(file_plaintext))
cipher.decrypt(file_ciphertext, file_plaintext)
