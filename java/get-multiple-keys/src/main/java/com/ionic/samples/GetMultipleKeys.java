/*
 * (c) 2018 Ionic Security Inc.
 * By using this code, I agree to the Terms & Conditions (https://dev.ionic.com/use.html)
 * and the Privacy Policy (https://www.ionic.com/privacy-notice/).
 * 
 * Developed with Ionic Java SDK 2.1.0
 */

package com.ionic.samples;

import com.ionic.sdk.device.profile.persistor.DeviceProfilePersistorPassword;
import com.ionic.sdk.agent.Agent;
import com.ionic.sdk.agent.request.getkey.GetKeysRequest;
import com.ionic.sdk.agent.request.getkey.GetKeysResponse;
import com.ionic.sdk.error.IonicException;
import java.util.List;
import javax.xml.bind.DatatypeConverter;

public class GetMultipleKeys
{
    public static void main(String[] args)
    {
        // initialize agent
        Agent agent = new Agent();
        try {
            String persistorPath = System.getProperty("user.home") + "/.ionicsecurity/profiles.pw";
            String persistorPassword = System.getenv("IONIC_PERSISTOR_PASSWORD");

            DeviceProfilePersistorPassword persistor = new DeviceProfilePersistorPassword(persistorPath);
            persistor.setPassword(persistorPassword);

            agent.initialize(persistor);
        } catch(IonicException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
        
        String keyId1 = "HVzG3oKSL7A";
        String keyId2 = "HVzG4fqePwk";

        // get multiple keys
        GetKeysRequest request = new GetKeysRequest();
        request.add(keyId1);
        request.add(keyId2);
        List<GetKeysResponse.Key> keys = null;
        try {
            keys = agent.getKeys(request).getKeys();
        } catch(IonicException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }

        // display fetched keys
        for (GetKeysResponse.Key key : keys) {
            System.out.println("---");
            System.out.println("KeyId        : " + key.getId());
            System.out.println("KeyBytes     : " + DatatypeConverter.printHexBinary(key.getKey()));
            System.out.println("FixedAttrs   : " + key.getAttributesMap());
            System.out.println("MutableAttrs : " + key.getMutableAttributes());
        }
    }
}