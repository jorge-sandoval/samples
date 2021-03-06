# (c) 2018-2019 Ionic Security Inc.
# By using this code, I agree to the Terms & Conditions (https://dev.ionic.com/use.html)
# and the Privacy Policy (https://www.ionic.com/privacy-notice/).

from __future__ import print_function

import os
import sys
import ionicsdk

# read persistor password from environment variable
persistor_password = os.environ.get('IONIC_PERSISTOR_PASSWORD')
if (persistor_password == None):
    print("[!] Please provide the persistor password as env variable: IONIC_PERSISTOR_PASSWORD")
    sys.exit(1)

# initialize agent with password persistor
try:
    persistor_path = os.path.expanduser("~/.ionicsecurity/profiles.pw")
    persistor = ionicsdk.DeviceProfilePersistorPasswordFile(persistor_path, persistor_password)
    agent = ionicsdk.Agent(None, persistor)
except ionicsdk.exceptions.IonicException as e:
    print("Error initializing agent: {0}".format(e.message))
    sys.exit(1)

# check if there are profiles
if agent.hasanyprofiles():
    for profile in agent.getallprofiles():
        print ("Name: {}, Id: {}".format(
            profile.name,
            profile.deviceid))

    # Check if there is an active profile.
    if agent.hasactiveprofile():
        print ("\nActive profile, Name: {}, Id: {}".format(
            agent.getactiveprofile().name,
            agent.getactiveprofile().deviceid))
    else:
        print ("There is not an active device profile selected on this device.")
else:
    print ("There are no device profiles on this device.")
