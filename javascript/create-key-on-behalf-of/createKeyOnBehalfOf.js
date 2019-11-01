/*
 * (c) 2019-2020 Ionic Security Inc.
 * By using this code, I agree to the Terms & Conditions (https://dev.ionic.com/use.html)
 * and the Privacy Policy (https://www.ionic.com/privacy-notice/).
 */

// AppData for all Javascript samples.
const appData = {
    appId: 'ionic-js-samples',
    userId: 'developer',
    userAuth: 'password123'
}

const main = async () => {

    const delegatedUserEmail = 'test@ionic.com'

    // initialize agent
    const agent = new window.IonicSdk.ISAgent();
    await agent.loadUser(appData).catch((error) => {
        console.log('Error loading profile: ', error)
        return
    })

    // define on-behalf-of as request metadata
    const requestMetadata = {
        'ionic-delegated-email': delegatedUserEmail
    }

    // create key
    const response = await agent.createKeys({
        quantity: 1,
        metadata: requestMetadata
    }).catch((error) => {
        console.log('Error Creating Key: ', error)
        return
    })
    const key = response.keys[0]

    // display created key
    console.log('')
    console.log('KeyId             : ', key.keyId)
    console.log('KeyBytes          : ', key.key)
    console.log('FixedAttributes   : ', JSON.stringify(key.attributes,null,0))
    console.log('MutableAttributes : ', JSON.stringify(key.mutableAttributes,null,0))
}

main();
