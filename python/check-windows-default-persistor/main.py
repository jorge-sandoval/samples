"""
(c) 2018 Ionic Security Inc.

By using this code, I agree to the Terms & Conditions (https://dev.ionic.com/use.html) and the
Privacy Policy (https://www.ionic.com/privacy-notice/).

"""

import ionicsdk

try:
    agent = ionicsdk.Agent()

    # Check if there are profiles.
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

except ionicsdk.exceptions.IonicException as e:
    print ("Error initializing agent: {}".format(e.message))

input("\nPress Enter to continue...")
