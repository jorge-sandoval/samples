/*
 * (c) 2019-2020 Ionic Security Inc.
 * By using this code, I agree to the Terms & Conditions (https://dev.ionic.com/use.html)
 * and the Privacy Policy (https://www.ionic.com/privacy-notice/).
 */

const appData = {
  appId: 'ionic-js-samples',
  userId: 'developer',
  userAuth: 'password123'
}

const main = async () => {
  const keyId1 = 'HVzG5uKl3yE'
  const keyId2 = 'HVzG3AJoHQU'
  const keyId3 = 'HVzG52Kj3to'

  // initialize agent
  const agent = new window.IonicSdk.ISAgent()
  await agent.loadUser(appData).catch((error) => {
    console.log('Error loading profile: ', error)
  })

  // Set the app metadata.
  let response = await agent.setMetadata({
    'ionic-application-name': 'JavaScript getMultipleKeys',
    'ionic-application-verison': '1.1.0',
  })

  // get multiple keys
  response = await agent.getKeys({
    keyIds: [keyId1, keyId2, keyId3]
  }).catch((error) => {
    console.log('Error Creating Key: ', error)
  })
  const keys = response.keys;

  // display fetched keys
  console.log('');
  keys.forEach((key) => {
    console.log('---');
    console.log('KeyId             : ', key.keyId);
    console.log('KeyBytes          : ', key.key);
    console.log('FixedAttributes   : ', JSON.stringify(key.attributes, null, 0));
    console.log('MutableAttributes : ', JSON.stringify(key.mutableAttributes, null, 0));
  })
}

main()
