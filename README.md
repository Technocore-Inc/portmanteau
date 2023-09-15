# portmanteau
p2p multisig wallet


"Well, 'slithy' means 'lithe and slimy'. 'Lithe' is the same as 'active'. You see it's like a portmanteau--there are two meanings packed up into one word." - Humpty Dumpty.

***Here's a high-level prototype for the "Portmanteau" multi-sig wallet:***

**1. Setup and Initialization:**

- User downloads and installs the Portmanteau wallet application.
- Upon initialization, the wallet will create:
  - A regular address (single-key) for day-to-day spending.
  - A multi-signature address for long-term storage.

**2. Multi-sig Configuration:**

- The user initiates the creation of a multi-sig address and invites selected friends to be co-signers.
Each invited friend, through their own Portmanteau wallet, generates and sends a public key to the user. This public key is essential for the multi-sig configuration but does not compromise the security of the friend's wallet.
- The private keys corresponding to these public keys remain securely on the friends' devices, ensuring they have full control of their signature authority.
- The user then sets the threshold for how many signatures are needed to authorize a transaction. For instance, if the user invites 5 friends, they might require at least 3 of their signatures to unlock the funds.

**3. Regular and Long-Term Compartments:**

- **Regular Compartment**: The user can transact normally using the private key stored on the device.
- **Long-Term Compartment**: To spend funds, the user sends a transaction request to the selected friends. This is a secure inquiry asking them to sign the multi-sig transaction.

**4. Transaction Authorization from Friends with Flexible Security Options:**

- **Initiation**:
  - The user initiates a transaction from their wallet. To authorize a transaction from the multisig compartment, signatures from a subset of their designated friends are required.

- **Flexible Data Generation**:
  - Upon initiating a transaction, the wallet software prompts the user with security options: "Would you like to share transaction details via QR Code, Steganographic Image, or both?" 
  - Depending on the user's choice, the wallet generates the required representation:
    1. QR Code
    2. Steganographic Image
    3. Hybrid (both QR code and steganographic image)
  
- **Steganographic Encapsulation** (if chosen):
  - The transaction details are seamlessly embedded within a chosen image using steganography, making it imperceptible to the naked eye.

- **QR Code Generation** (if chosen):
  - A QR code representing the transaction details is generated.

- **Sharing & Identity Verification**:
  - The user shares the chosen method(s) with their designated friends, either digitally or in person.
  - Upon receiving, friends then verify the user's identity through a third-party channel such as a phone call, video chat, or face-to-face interaction.

- **Decoding & Authorization**:
  - Depending on the method(s) the user chose:
    - For QR: Friends can scan the QR code to retrieve transaction details swiftly.
    - For Steganographic Image: Friends use a steganography tool or a compatible wallet feature to extract details from the image.
  
  - After retrieving and verifying the transaction details, each friend signs the transaction with their private key tied to the multisig address.
  
- **Signature Collection & Broadcasting**:
  - As the user collects the required number of signatures (e.g., 3 out of 5 friends), the wallet compiles them.
  - Once the threshold is met, the wallet broadcasts the transaction to the network, permitting the transfer of funds from the multisig compartment to the intended address.

*By providing the user with a choice between QR codes, steganographic images, or a hybrid method, this approach caters to different security preferences and use cases. Some users may prioritize discretion and opt for steganography, while others might lean towards the quick convenience of QR codes. The hybrid option offers a balanced mix of both security and ease.*

**5. Backup & Recovery:**

- **Regular Compartment**:
  - The user should backup the private key of the regular compartment. This ensures that in the event of a device malfunction, loss, or wallet deletion, they can restore the regular compartment using this backed-up private key.

- **Multisig Compartment**:
  - The user doesn't need to backup the friends' private keys (and shouldn't for security reasons). However, they should document the multisig configuration, like the threshold for the number of signatures required and the public keys or xpubs of the participants.
  - In the event of a wallet recovery scenario, the user would need to re-setup the multisig compartment. They would have to re-invite or re-add friends and gather their public keys again for the multisig address generation. Afterward, the required number of friends must sign any pending transactions again.

- **Shamir's Secret Sharing**:
  - Instead of backing up the private key directly, the user can opt for Shamir's Secret Sharing (SSS) for added security. Here's how it works:
    1. The private key of the regular compartment (or the seed phrase) is split into multiple parts using Shamir's algorithm. 
    2. A threshold is set, determining how many parts are needed to reconstruct the original private key. For example, the key might be split into 5 parts, with any 3 required to reconstruct the full key.
    3. These parts or shares can be distributed to trusted entities or stored in different locations. They provide redundancy, so if one or more parts are lost, the private key can still be reconstructed as long as the threshold number of parts is available.
  - In a recovery scenario:
    1. The user would gather the necessary number of parts (e.g., 3 out of 5).
    2. Using the Shamir's algorithm, these parts would be combined to reconstruct the original private key, allowing for wallet restoration.

*By leveraging Shamir's Secret Sharing, the user can achieve a higher level of security for backups, protecting against both device loss and potential threats, as no single share provides insight into the actual private key.*

*Hierarchical Deterministic (HD) introduces a systematic structure and enhanced privacy.*

a. **HD Wallet Creation for Each Participant**:
   - Every participant (including the main user and their friends) generates their HD wallet. This involves the creation of a seed phrase, which leads to the derivation of a master private key and a corresponding master public key.
   
b. **Multisig Extended Public Key Sharing**:
   - Each participant derives an extended public key (xpub) from their HD wallet for the multisig compartment. They share only this xpub with the main user or the multisig coordinator.
   - Note: Sharing the extended public key allows the coordinator to generate multiple multisig addresses without further interaction with the participant. However, it doesn't compromise the security of any participant's wallet.

c. **Multisig Address Generation**:
   - The main user or coordinator uses the collected extended public keys from all participants to generate the multisig addresses. With HD, they can produce a virtually infinite number of addresses in a structured manner, enhancing privacy since each transaction can go to a new address.
   
d. **Transaction Authorization**:
   - When funds in a particular multisig address need to be spent, the transaction proposal is shared with the necessary number of participants (as per the threshold set, e.g., 3 of 5).
   - Each participant uses their HD wallet to derive the appropriate private key for the address in question and then signs the transaction.
   - Once the required number of signatures is collected, the transaction is broadcasted to the network.

e. **Gap Limit Consideration**:
   - HD wallets usually monitor a series of addresses for activity. If a certain number of consecutive addresses show no transaction history (often 20), the wallet stops checking further addresses. This is known as the "gap limit."
   - In the context of multisig with HD, ensure that the gap limit isn't reached without transaction activity. Otherwise, some addresses may be skipped, which can cause confusion or missed funds. Participants must be somewhat coordinated in their use of addresses to avoid hitting this gap.

f. **Backup and Recovery**:
   - The advantage of using HD in multisig is that the backup process becomes streamlined. Each participant only needs to back up their seed phrase. In the event of device loss, the seed can be used to restore the entire HD wallet, including all derived keys for the multisig compartment.
   - However, the multisig setup (like who the participants are, the required signatures, and the xpubs) should also be documented and stored securely. This information will be necessary to recover funds in case of device loss or other unforeseen circumstances.

*By using HD with multisig, users can combine the privacy and structured benefits of HD wallets with the security enhancements of multisig configurations.*

**6. Features for Enhanced Security:**

- Two-factor authentication (2FA) for transaction approvals.
- Notifications for any activity on the long-term storage.
- Secure communication channel for transaction requests and approvals.

**Enhanced Security Using Application Password in Seed Phrase Generation:**

*Incorporating an application-specific password into the seed phrase generation process adds another layer of security to the wallet. By combining user input (application password) with the randomly generated seed phrase, the derived key becomes unique to each user, even if two users are somehow given the same seed phrase.*

Here's how it can work:

1. **Initialization**:
    - When setting up the wallet for the first time, the user is prompted to provide an application password. This password should be robust, ideally consisting of alphanumeric characters and symbols.

2. **Password Hashing**:
    - To ensure that the user's password remains secure, it is hashed using a cryptographic hash function.

3. **Seed Phrase Generation**:
    - The wallet generates a standard seed phrase (typically 12 or 24 words) using a secure random number generator.

4. **Combining Seed & Password**:
    - The hashed version of the application password is combined with the seed phrase. This could be through a method like concatenation, salting, or another form of cryptographic mixing.

5. **Final Key Derivation**:
    - The combined data is then passed through a key derivation function to produce the final private key for the wallet. This private key is both a function of the seed and the user's application password.

6. **Transaction and Access Authentication**:
    - Every time the user wants to make a transaction or access certain secure sections of the wallet, they would need to provide their application password, ensuring an added layer of security.

7. **Backup & Recovery**:
    - Users should be informed that, for backup or recovery purposes, both the seed phrase and the application password are crucial. Losing either component would mean they cannot recover their funds.

8. **Warning**:
    - Emphasize the importance of never sharing the application password or writing it down with the seed phrase. These two components should be stored separately to ensure maximum security.

*By integrating the application password into the seed phrase generation process, not only is the derived key unique but also the security is substantially heightened. Even if a malicious actor gains access to the user's seed phrase, without the application password, they can't access the funds. However, this approach also increases the responsibility on the user's end – losing the application password would mean they can't recover their funds, even if they have the seed phrase.*

*To further protect user assets and information, the application can create two separate seeds: one associated with the user's actual password (real wallet) and the other tied to a duress password (decoy wallet). This approach ensures that even if the duress password is used, the intruder only gains access to the decoy wallet, which can be set up with limited or fake balances and addresses.*

*Given the transparent nature of blockchain transactions, we need to make sure the decoy wallet is convincing enough. We can't fabricate blockchain-based transactions, but we can ensure the decoy wallet is set up in a way that's plausible without exposing the real wallet. Here's a revised approach:*

**Dual Seed Creation with Real and Duress Passwords on a Transparent Blockchain:**

**Initial Setup:**

- Upon initial setup, the user generates a seed and corresponding password for their real wallet.
They're then prompted to set up a "duress" password. This password is used to generate a completely separate seed for the decoy wallet.
Decoy Wallet Initial Funding:

- To ensure the decoy wallet appears genuine, users should transfer a small, believable amount of cryptocurrency to it. This amount would be far less than the primary wallet but enough to seem like a typical everyday wallet.
Wallet Functionality Based on Password Entered:

- Real Password: Provides access to the user's main wallet with all their actual funds, addresses, and transactions.
Duress Password: Opens the decoy wallet, which has its real balances and transactions but is significantly less than the main wallet.
Actions Triggered by Duress Password:

- Alert Functionality: When the duress password is entered and the decoy wallet is accessed, the application discreetly sends an alert to a predefined contact or authority.

- Protection Against Unauthorized Fund Transfer:

- Transactions initiated from the decoy wallet could have a deliberate delay, giving the user a window to potentially block unauthorized transfers. Or, transactions can be automatically redirected to a secure vault address known only to the user.
Backup & Recovery with Duress Password:

- Restoring with the duress password only restores the decoy wallet, ensuring the primary wallet remains concealed and secure.
Education & User Awareness:

*Users need to be clearly informed about the difference between the two passwords and the separate wallets they control.
It's crucial to emphasize the importance of occasionally using the decoy wallet for small, genuine transactions to maintain its legitimacy.*

**Safety Precautions:**

*Ensure users know that while the decoy wallet provides an additional layer of protection, it isn't a foolproof safety measure in all coercive situations. The best protection is prevention, such as keeping the existence of a larger wallet entirely confidential.*

*This dual-seed approach, derived from two distinct passwords, enhances the security offerings of the wallet. While the real wallet contains the user's actual assets, the duress wallet serves as a protective layer, helping users maintain control over their assets even when faced with threats. Clear communication and user training are essential to the success of this strategy.*

*In this revised approach, the decoy wallet is not merely a dummy, but a genuine but smaller-scale wallet. This ensures that if an imposter or malicious actor checks the blockchain, they will see legitimate transactions, but will hopefully be deterred by the smaller balance, believing they have accessed all there is.*

**7. User Experience Enhancements:**

- A user-friendly interface showing both compartments' balances and transaction histories.
- Easy navigation to send transaction requests to friends.
- A dashboard for friends to view and sign pending transactions.

**Development Considerations:**

- Blockchain selection: Choose a blockchain that supports multi-sig natively, e.g., Bitcoin or Ethereum.
- Communication security: Ensure end-to-end encryption for transaction requests and approvals.
- Data privacy: Store sensitive data, such as private keys, securely and encrypted. Never expose private keys during communication.
- Backup & Recovery: Offer easy-to-use tools for users to backup and restore their wallets.

Building this wallet would require significant development effort across blockchain, security, and application development domains. Testing is crucial, especially considering the financial implications of any bugs or vulnerabilities.

***Incorporating an alert system for friends when suspicious or abnormal activities are detected is a great addition to the "Portmanteau" wallet. Let's detail how this can be integrated:***

**1. Enhanced Security with Alert Triggers:**

- **Incorrect Password/Fingerprint Inputs**: After a set number of consecutive incorrect attempts (e.g., 3 wrong passwords or fingerprint scans), the wallet triggers an alert to the selected friends.

- **Intentional Delays**: The user can set a "Check-in" period, say every month. If they don't sign a transaction with their key or "check-in" within this period, an alert is sent to friends. This feature can act as a dead man's switch.

- **Unusual Transaction Patterns**: If there's an attempt to move a larger-than-usual amount from the long-term compartment without the user's primary signature, an alert is dispatched.

**2. Configurable Alerts for Friends:**

- **Notification Preferences**: Friends can set preferences for what types of alerts they want to receive. They might want to be informed only for high-priority alerts, or they might opt-in for all notifications.

- **Verification Channel**: Upon receiving an alert, friends will have the option to contact the user directly through third-party communication channels to verify if the user initiated the action or if there's a genuine threat.

**3. User Control Over Alerts:**

- The wallet user can configure the sensitivity of the alert system. For instance, they can adjust how many incorrect attempts should trigger an alert or the amount threshold for unusual transaction patterns.

- They can also set "quiet times" where minor alerts are suppressed, to prevent unnecessary panic or disturbance, especially if they're aware of potential false positives.

**4. Emergency Response System:**

- In case of confirmed unauthorized access or threats, friends can initiate an "emergency lock," freezing the funds temporarily. To unfreeze, a consensus of a certain number of friends (or all) might be required.

- The user, upon verifying their identity, can also have the option to override this emergency lock, but with additional checks in place.

**5. Enhanced User Experience:**

- **User Dashboard**: Visual indicators for the last check-in, incorrect access attempts, and other security metrics. This way, the user can monitor their wallet's health at a glance.

- **Friends Interface**: Friends should have a dedicated section in their wallet app where they can view and manage all alerts and notifications, pending transaction signatures, and emergency responses.

**Development & Security Considerations:**

- **Privacy First**: Ensure that the alert system does not leak any sensitive information. Alerts should be vague, like "Suspicious activity detected on [Friend's Name] wallet."

- **Resilience against Misuse**: Consider potential misuse scenarios, such as a friend getting too many false alerts and ignoring a real one, or friends abusing the emergency lock feature.

- **Testing**: As always, rigorous testing should be conducted to ensure the alert system works as expected without false positives or negatives.

By implementing this enhanced alert system, the Portmanteau wallet would offer its users a combination of self-sovereign financial control and a social safety net, optimizing both security and usability.

***Adding a security level with public key exchange can fortify the alert system in the Portmanteau wallet by ensuring the alerts and system messages are end-to-end encrypted and can only be read by the designated friends. This level of security will prevent eavesdropping and unauthorized access to critical information. Here's how this can be seamlessly integrated into the concept:***

**1. Secure Key Exchange:**

- **Initial Setup**: When designating a friend within the Portmanteau wallet, a one-time secure key exchange process is initiated. The wallet generates a temporary public/private key pair, and only the public part is shared with the designated friend.

- **Encryption**: Alerts and system messages are encrypted using the friend's public key, ensuring that only the friend, with the matching private key, can decrypt and read the message.

- **Key Rotation**: For added security, consider rotating these keys at regular intervals or after a set number of exchanges. This ensures that even if a key is compromised, it can't be used indefinitely.

**2. Hierarchical Security Levels:**

- **Level 1 - Basic Alerts**: Information regarding failed password attempts, check-ins, etc. This is encrypted but contains general non-specific details.

- **Level 2 - Transaction Requests**: Messages requesting signatures for multisig transactions or indicating unusual transaction patterns. This requires higher encryption.

- **Level 3 - Emergency Notifications**: Alerts indicating a potential breach or the activation of the emergency response system. These alerts may have the highest level of encryption and may be accompanied by an urgency signal.

**3. Mutual Authentication:**

- To prevent impersonation, when the Portmanteau wallet sends an encrypted message to a friend, it should also include a digital signature created using the user's private key. This way, the friend can verify the authenticity of the message using the user's public key.

**4. Backup and Recovery:**

- If a friend loses their device or access to their private key, there should be a secure protocol to re-establish the connection and exchange new keys without compromising the security of the wallet or the encrypted communication.

**5. Enhanced Privacy Controls:**

- Allow users to set which alerts or messages are sent to which friends. For instance, a user might want only certain friends to be notified about large transactions, while all friends receive basic security alerts.

**6. Secure Key Storage:**

- All private keys, including the temporary ones used for encrypted communication, should be securely stored, preferably in hardware or secure enclaves if the application is on a smartphone.

**Development & Security Considerations:**

- **Avoiding Man-in-the-Middle Attacks**: Ensure the key exchange is secure, potentially by verifying keys through an out-of-band method or using trusted third-party solutions like QR code scanning.

- **Regular Audits**: Engage in regular security audits to ensure there are no vulnerabilities in the key exchange or encryption protocols.

By adding this layer of security, you ensure that not only are the funds secure within the Portmanteau wallet, but the communication between friends about the wallet's status is also safeguarded.

***Generating multisig addresses in a peer-to-peer (p2p) manner distributes the risk and bolsters security, especially in a scenario where trust is decentralized. Creating a multisig address collaboratively ensures that no single entity has complete control over the address creation process, reducing the chance of a centralized point of failure.***

Here's a step-by-step guide to adding this level of security:

**1. P2P Multisig Address Generation:**

- **Request for Public Keys**: When setting up a multisig address, the user's Portmanteau wallet sends a secure request to designated friends' wallets for their public keys.

- **Gathering Public Keys**: Each friend's wallet, upon user approval, sends back their public key to the requesting wallet. These keys are securely transmitted and encrypted.

- **Collaborative Address Creation**: The Portmanteau wallet then uses the gathered public keys, along with its own, to collaboratively generate the multisig address. This process ensures that the multisig address is a combination of keys from all parties involved.

**2. Threshold Signatures:**

- Determine a threshold for how many signatures are required to approve a transaction. For instance, if you've chosen five friends, you might decide that any three out of those five need to approve a transaction.

**3. Secure Communication Channel:**

- It's paramount that the channel of communication is encrypted and secure. This can be achieved using the earlier mentioned public key encryption process, where messages are encrypted using the recipient's public key.

**4. Address Verification:**

- Once the multisig address is generated, it would be a good security measure to allow each participant to verify the address independently. This can be achieved by sending a small test transaction to the newly created address. All participants should be able to validate this transaction.

**5. Backup & Recovery Protocols:**

- Since the multisig address relies on multiple parties, there should be a protocol in place in case a friend loses access to their key or if they are unreachable. This might mean having backup friends or other recovery methods.

**6. Enhanced Security Protocols:**

- Consider adding additional layers of security such as 2-factor authentication (2FA) for transaction approval requests and other critical actions.

- Anonymize the origin of the request. Even if it's a secure and encrypted request for a public key, it's a good practice to ensure that the source (i.e., the original user's Portmanteau wallet) remains anonymous, to protect the user's identity and intentions.

**Development & Security Considerations:**

- **Avoiding Sybil Attacks**: Ensure that the friends are genuine users and not multiple fake nodes set up by an adversary. This can be achieved by having some sort of trust verification or vouching system.

- **Rate Limiting**: Introduce rate-limiting mechanisms to prevent spamming of public key requests.

- **Regular Security Audits**: Regularly conduct audits to ensure the p2p key exchange and multisig address generation process is robust and free from vulnerabilities.

With this p2p approach, the Portmanteau wallet's multisig functionality becomes more robust and resilient against centralized threats, providing users with an extra layer of security and peace of mind.



***Adjusting the concept to use a blockchain-based system, particularly a "sharechain" for exchanging system messages, wallet states, keys, and other pertinent information is an intriguing idea. Here's how we can adapt the previous concept to incorporate these changes:***

**1. Sharechain Basics:**

- **Shares Instead of Blocks**: Instead of bundling transactions into blocks like traditional blockchains, we use "shares" to temporarily store system messages, wallet states, keys, and other information. Each share represents a set of messages or data updates.

- **Rolling Data Window**: As the sharechain grows, older shares are pruned to maintain a reasonable data size. This way, the storage and transmission overhead for each node remains manageable, ensuring the system is scalable.

**2. No Trusted Nodes Principle:**

- **Equal Rights for All Nodes**: Every node in the network has the same rights and capabilities. There's no central authority or trusted node. This ensures decentralization and diminishes single points of failure or control.

- **Dynamic Participation**: Nodes can join or leave the network freely without any repercussions. This dynamic topology ensures the system is resilient to node failures.

**3. Share Verification and Propagation:**

- **Proof of Stake (PoS) or Other Consensus Mechanism**: While we've ruled out Proof of Work, there's still a need for a consensus mechanism to validate shares. A lightweight version of PoS might be appropriate, where nodes validate shares based on the number of Portmanteau wallets or user endorsements they can attest to. This would prevent spam or malicious nodes from flooding the network with invalid shares.

- **Gossip Protocol**: Use a gossip protocol to propagate shares among nodes efficiently. This way, when a node receives or creates a new share, it notifies a subset of its peers, who then notify their peers, leading to rapid data propagation.

**4. Secure Communication:**

- **End-to-End Encryption**: All messages, keys, and other data exchanged between Portmanteau wallets over the sharechain should be encrypted using public key encryption. This ensures that only the intended recipient can decrypt and read the message.

**5. Data Lifecycle on Sharechain:**

- **Temporary Storage**: Data in shares, especially sensitive information like keys, should have a limited lifespan. Once they've served their purpose (e.g., a key has been exchanged and acknowledged), they should be marked for pruning during the next rolling data window update.

- **Immutable History for Relevant Data**: Some data, like system alerts or wallet state changes, might be valuable for maintaining a history. In such cases, the sharechain can provide an immutable record (up to the point of the rolling window) to trace back any discrepancies.

**6. Resilience and Scalability:**

- **Sharding**: As the network grows, consider splitting the sharechain into shards, where each shard handles a subset of the total messages. This can help in scaling the system efficiently.

- **Peer Discovery**: Use a decentralized peer discovery mechanism, ensuring nodes can find and connect to each other without relying on central directories.

In essence, the adjusted Portmanteau wallet system will be a decentralized, peer-to-peer, and blockchain-based communication system tailored specifically for secure data exchange among users. With the proposed sharechain approach, users can enjoy the benefits of blockchain technology while ensuring data integrity, privacy, and scalability.



***Given the unique requirements of the "sharechain" concept for the Portmanteau wallet system, we'd need a consensus mechanism that caters to:***

1. Absence of open sensitive data inside shares.
2. The short online durations of nodes.
3. No accumulated trust over time.
4. The possible absence of neutral peers, leaving only friend nodes.

Considering these constraints, a hybrid consensus mechanism might be fitting. Here's a proposal:

**1. Direct Trust-Based Signing (DTBS):**

- Each user has a circle of "direct trust" friends. When they want to publish a share to the sharechain, they can obtain signatures from a subset of these trusted friends. 
- A share can be considered valid if it contains signatures from a predefined number of such direct trust friends.
- This method is beneficial for instances when only friends are online or the network has very few active participants.

**2. Lightweight PoS with Weighted Randomness:**

- Given the short duration nodes are online, traditional PoS might not work well. Instead, nodes could lock a symbolic amount of tokens (or any other form of commitment) to show their intention of participating in the consensus for a given timeframe.
- During their active periods, these nodes become temporary validators. The chances of being chosen as a validator for a particular share depend on the amount of token locked multiplied by a random factor. This randomness ensures no predictability, making it harder to game.
- This method helps when more nodes are online, providing a quicker consensus.

**3. Proof of Availability (PoA):**

- Given the short online times of nodes, nodes that are online and can prove they possess certain shares or data could get priority in consensus decisions.
- This is based on the idea that availability and willingness to participate are valuable for the network's health, especially in a system with short online durations.

**4. Share Validation and Propagation:**

- Before being propagated, shares are briefly validated for structure and integrity. This can be a straightforward deterministic process.
- After basic validation, shares are propagated in the network, where the consensus mechanism then further validates them.
- If a node propagates an invalid share, a penalty can be applied. This could be a timeout or a symbolic fine.

**5. Dispute Resolution:**

- If there's a dispute, e.g., two conflicting shares, the one with more direct trust signatures (from the friends) or validator approvals (from the lightweight PoS) gets preference.
- If disputes can't be resolved in this manner, a time-bound fallback mechanism could kick in. For instance, waiting for more friend nodes to come online to provide their direct trust signatures.

**Conclusion:**

Such a hybrid consensus mechanism combines the benefits of direct trust, lightweight staking, and data availability. It provides flexibility, ensuring that the system remains operational even when only a few nodes (or just friend nodes) are online, while still benefiting from the broader network when more nodes are active. The system is designed to be resilient, ensuring that even in the face of potential thefts or malicious actors, the integrity of the sharechain is maintained.



***When many nodes are typically offline and only occasionally online, maintaining a shared storage system that's both accessible and reliable can be a challenge. Here's a solution using fragmented distributed storage:***

### Fragmented Distributed Storage with Redundancy:

**1. Data Fragmentation:**

- When a Portmanteau wallet user generates data (like a message, system update, or key exchange), this data is fragmented into multiple smaller chunks.
  
**2. Redundancy with Erasure Coding:**

- Apply [Erasure Coding](https://en.wikipedia.org/wiki/Erasure_code) to each fragmented piece of data. This technique divides data into fragments that are expanded and encoded with redundant pieces of data. For instance, you can split a piece of data into 10 fragments but then expand it to 16 fragments. Any 10 out of those 16 are enough to reconstruct the original data. This means you can lose up to 6 fragments, and the data is still recoverable.
  
**3. Fragment Distribution:**

- Each fragment, post-erasure coding, is distributed to a different Portmanteau wallet user's storage. The system will ensure that fragments are distributed such that there's a higher probability that at least some fragments will be available at any given time.
  
**4. Directory Nodes (D-Nodes):**

- While most nodes are offline most of the time, there can be special nodes called Directory Nodes (D-Nodes). These D-Nodes are light nodes that don't store data but keep track of which node has which fragment. They can be run on devices that are online more often (like home PCs or dedicated servers). These D-Nodes help in quickly locating the fragments needed.
  
**5. Data Retrieval:**

- When a node wants to access specific data, it will query the D-Nodes. The D-Nodes will provide a list of nodes that should have the fragments.
- The requesting node then attempts to retrieve the fragments from the nodes in the list. Due to erasure coding, even if some of those nodes are offline, the data can still be reconstructed if enough fragments are accessed.
  
**6. Periodic Rebalancing:**

- As nodes join or leave the network or as the likelihood of certain nodes being online changes, the system can rebalance where fragments are stored. This rebalancing is done to ensure high data availability and to cope with the dynamic nature of the network.

**7. Incentive for Storage:**

- Given the voluntary nature of the network, an incentive mechanism might be required to encourage users to offer storage. This could be in the form of improved service, acknowledgments, or even a symbolic reward system. For instance, those who share storage might get priority in data retrieval or other services.

**Benefits:**

- **Redundancy**: Erasure coding ensures data is available even if many nodes are offline.
  
- **Flexibility**: The system can cope with a large percentage of nodes being offline simultaneously.
  
- **Scalability**: As more users join the Portmanteau wallet, the storage system scales naturally, with each user contributing a small amount of storage.

In conclusion, fragmented distributed storage with redundancy, guided by directory nodes, allows the Portmanteau wallet system to maintain a shared storage system even when most nodes are typically offline.



***To manage a sharechain in a decentralized manner with Portmanteau wallet users, particularly when nodes (users) are often offline, a shared storage solution needs to prioritize redundancy and accessibility. Here's a proposal that might work:***

**1. Distributed Hash Table (DHT) with Erasure Coding:**

- **Distributed Hash Table (DHT)**: DHTs are a class of decentralized distributed systems that allow nodes to self-organize and distribute data. Data can be retrieved by a key, and the data corresponding to a key is stored on the node to which the key maps. BitTorrent uses DHT for its peer-to-peer file-sharing system.

- **Erasure Coding**: Given the intermittent availability of nodes, erasure coding can ensure that even if only a portion of the nodes are online, the full data can still be reconstructed. This process splits data into fragments that are expanded and encoded with redundant data pieces. If some fragments go missing, they can be reconstructed from the remaining ones. 

**2. Scheduled Synchronization:**

- Given that nodes will be offline most of the time, there could be a feature where nodes schedule 'sync sessions' where they come online to update and synchronize their version of the sharechain with others. This ensures that even if nodes are often offline, they periodically get updated.

**3. Data Pinning Agreements:**

- When online, nodes can enter short-term pinning agreements. Here, they promise to keep certain shares of data available for a particular duration. These agreements can be made based on the expected online time or can be randomized.

- When two nodes are online simultaneously, they can agree to pin complementary data. This ensures that even if one node goes offline, the network doesn't lose access to the data it was pinning because the other node has it.

**4. Data Prioritization:**

- Given the rolling data window where older shares are discarded, nodes can prioritize keeping the newest shares available. Older shares that are nearing their discard time can be deprioritized, saving storage space and bandwidth.

**5. Local Caching and Checkpoints:**

- Nodes can maintain local caches of frequently accessed or critical data.
  
- Periodic checkpoints can be established in the sharechain. These checkpoints are a condensed representation of the state at a particular time. Nodes can download these checkpoints when they come online, ensuring they have a relatively recent state of the sharechain without downloading everything.

**6. Lightweight Bootstrap Nodes:**

- While the idea is to avoid special directory nodes, having a few voluntarily run bootstrap nodes can be beneficial. They're not trusted nodes but can help new nodes or nodes coming online after a long gap to quickly discover peers and synchronize faster.

**7. Proactive Data Requesting:**

- Before going offline, nodes can broadcast a 'going offline' message, prompting other nodes to request any data they might need from this node in the near future.

**8. Gossip Protocol:**

- Nodes can use a gossip protocol to propagate data. This ensures that information (like new shares or updates) quickly spreads across the network, even if only a few nodes are online.

**Conclusion:**

The proposed system leverages the redundancy of DHTs and erasure coding to ensure data availability even with the intermittent online behavior of nodes. Scheduled syncs, data pinning, and proactive requests further enhance the accessibility and freshness of the data. This approach respects the constraints presented and ensures a robust shared storage system for the Portmanteau wallet users.



***Given the constraints provided, let's adjust the communication concept:***

### Adjusted Communication Concept for Portmanteau Wallet Peer Nodes

1. **Mobile-Optimized Protocol**: Recognizing that all nodes run on mobile devices, the protocol should be lightweight, ensuring minimal battery and data consumption. 

2. **Short Online Times**: Given the sporadic nature of node availability due to short online times, a more dynamic approach to node discovery and management is required.

3. **Dynamic Supernode Selection**:
    - During the small windows when users are active on their Portmanteau wallets, a fraction of them can temporarily serve as supernodes based on network needs, their device capabilities, and connectivity.
    - Users who permit the app to run periodically in the background could have a higher priority for supernode selection, as they'd provide more consistent availability.
    - Incentives could be provided (maybe in the form of reduced fees, cashback, or other perks) to users who allow the app to periodically wake up and contribute to the network.

4. **Localized Communication Strategy**: Since the nodes are mobile and geographically scattered, using location data (if permitted) can optimize communication. Peers close to each other can form temporary clusters to communicate more efficiently and quickly.

5. **Caching and Data Retention**: 
    - Nodes, when online, can cache critical network data and messages. 
    - Cached data can be utilized for quicker synchronization the next time they're online.
    - Background processes can periodically update this cache to ensure data freshness.

6. **Push Notifications**: Use mobile push notifications as an alert mechanism:
    - Notify friends about required signatures for multisig transactions.
    - Warn of any suspicious activities on their Portmanteau wallet.
    - Remind users to come online if there's a pressing need for their node to contribute to network stability.

7. **Scheduled Synchronization**: Given that friends are usually warned before a multisig transaction:
    - Allow scheduling of synchronization times. Friends can indicate when they will be online, ensuring that there's an overlap of online times for necessary operations.
    - This ensures that the necessary peers are online at the same time for critical operations, improving efficiency.

8. **Intelligent Peer Selection**: 
    - When a node needs to relay a message or transaction, intelligently select online peers based on their recent activity, ensuring quicker message propagation.
    - Factor in geographic proximity, historical uptime, and recent contributions to network stability.

9. **Background Network Maintenance**:
    - Nodes with permission to run in the background, even if for short periods, can perform routine network maintenance tasks, like data verification, message forwarding, and temporary data storage.
    - They can also play a role in establishing the necessary connections for nodes that are currently online and using the app.

10. **Security**:
    - Continuously ensure end-to-end encryption, especially since most communications will be via unpredictable mobile networks.
    - Use multi-factor authentication to confirm transaction requests, especially if there's a deviation from typical user behavior.

By adjusting the communication concept around these constraints, the Portmanteau wallet peer nodes can maintain a robust, efficient, and secure network while recognizing the mobile-centric and sporadic online behavior of its users.



***Maintaining friend anonymity within a system while ensuring they get notifications requires a strategy that separates the identity of the friend from the actual push mechanism. Here's a method to achieve this:***

### Token-Based Anonymous Notification System

1. **Token Generation**:
   - When setting up the multisig wallet, each friend (participant) in the multisig group generates a unique, one-time-use token.
   
2. **Token Registration with Notification Service**:
   - Each friend registers their unique token with a decentralized notification service, without linking it to their actual wallet address or identity. This service is solely responsible for handling push notifications.
   - For an added layer of security, the registration process can be done over Tor or a similar anonymizing network.

3. **Storing Tokens in Wallet**:
   - The user's wallet stores these one-time-use tokens, but has no knowledge about which token is linked to which friend. 

4. **Notification Initiation**:
   - When the user wants to initiate a multisig transaction, their wallet sends a notification request to the decentralized notification service using these tokens.
   - The service then pushes notifications to devices linked with these tokens without revealing or knowing the identity behind each token.

5. **Token Rotation for Enhanced Anonymity**:
   - Once a token has been used to receive a notification, it gets flagged or discarded. The friend's wallet will automatically generate a new token, register it with the notification service, and then securely communicate this new token to the user's wallet.
   - This ensures that even if an external actor collects these tokens over time, they cannot establish a consistent pattern or link them to specific individuals.

6. **Decentralized Notification Service**:
   - To prevent centralization and potential data collection by a single entity, the notification service itself can be built on a decentralized platform or framework, similar to how dApps operate on platforms like Ethereum. This ensures that there's no single point of control or failure.

7. **End-to-End Encryption**:
   - All communications between the user's wallet, the friend's wallet, and the notification service should be end-to-end encrypted, ensuring that even if data transmission is intercepted, the content remains confidential.

Through this token-based system, friends remain anonymous to the wallet itself, while still receiving necessary notifications. The continuous rotation of tokens and use of a decentralized notification platform ensures high levels of privacy and security.



### Emergency Transfer to Long-Term Storage

1. **Emergency Trigger**:
   - Implement a specific gesture, passphrase, or pattern within the wallet app that signifies an emergency. This can be a unique swipe pattern, a series of taps, a voice command, or even a hidden button.
   - For additional security, allow the user to customize this trigger during the setup process, so it's unique to each user and harder for outsiders to guess.

2. **Instant Fund Transfer**:
   - Upon recognizing the emergency trigger, the wallet immediately initiates a transaction to move all available funds to the multisig long-term storage address.
   - This process should be made as seamless and quick as possible, without the need for extra confirmations, to ensure timely execution during emergencies.

3. **Stealth Mode**:
   - Optionally, after the emergency transfer is initiated, the wallet can enter a "stealth mode". In this mode, the wallet might hide its balance, transactions, or even appear as if it's been reset to its default state. This can deter a potential thief or attacker who accesses the mobile device, making them believe that the wallet is empty or unused.

4. **Notification to Friends**:
   - Using the previously discussed token-based anonymous notification system, the wallet can also send a discreet alert to the friends' list, notifying them of the emergency transaction. This helps keep them informed and ready to validate any further multisig transactions if required.

5. **Recovery Process**:
   - After the emergency has been dealt with, the user can begin the process of accessing the funds in the multisig storage. They can communicate with their friends and get the required signatures to move the funds back to the regular compartment or to a new wallet, depending on the circumstances.

6. **Rate Limiting & Anti-Fraud**:
   - To prevent misuse or accidental triggers, implement rate limiting on how often the emergency function can be used. For example, if triggered, it might be disabled for a certain time period.
   - Additionally, any suspicious or repetitive use can be flagged for review, and the user can be prompted for additional verification.

7. **Regular Reminders**:
   - Periodically remind users about this feature, its purpose, and its trigger mechanism. This ensures they remember it during actual emergencies.

This emergency function adds a robust protective layer to the Portmanteau wallet, allowing users to swiftly act in dire situations and safeguard their assets.




***Absolutely! Here's an enhancement to the Portmanteau Wallet concept, catering specifically to the use cases mentioned:***

## **Portmanteau Wallet: Special Use Cases**

### **1. Children's Wallet**:

This configuration is crafted for parents wishing to give their children the independence of a wallet, but with some built-in oversight.

**Features**:

- **Dual Access Control**:
  - **Child's Spending Compartment**: Contains a limited amount of funds for daily use. The child has access to this compartment with set daily or weekly spending limits.
  
  - **Parental Control Compartment**: A multisig storage that parents have control over. When the child requires more funds or for special expenses, they can request a transfer from this compartment.

- **Multisig Transaction Process**:
  - When a child requests more funds, parents receive a secure inquiry to their wallets. They can approve or decline the request, and in the case of approval, the specified amount moves to the child's spending compartment.
  
- **Notifications**:
  - Parents can receive notifications for transactions exceeding a certain amount or for when the child's spending compartment balance runs low.
  
- **Educational Component**:
  - The wallet can have features that educate the child about saving, budgeting, and cryptocurrency in a child-friendly manner.

### **2. Collective Funds Wallet**:

This configuration is designed for groups (like clubs, associations, or teams) pooling funds collectively, ensuring consensus-based spending.

**Features**:

- **Multi-User Access Control**:
  - **Individual Spending Compartments**: Each member can have an individual compartment for personal use or allocated funds.
  
  - **Consensus Control Compartment**: The main compartment where collective funds are stored. Transactions from this compartment require multisig approval from designated members or a majority.

- **Multisig Transaction Process**:
  - When a fund allocation request arises, all designated members receive a secure inquiry. A set majority (e.g., 2/3) must approve for the funds to be released.
  
- **Transparent Ledger**:
  - All members can view transactions and approvals for accountability. However, personal compartments can be set to private.
  
- **Notifications & Voting**:
  - Members receive notifications for fund requests, allowing them to cast their vote (approve/deny) within a stipulated timeframe.

- **Role-Based Permissions**:
  - Depending on the organization's structure, roles like Treasurer or President might have special permissions or responsibilities within the wallet.

### **Benefits**:

- **Control & Oversight**: Both configurations ensure a balance between autonomy and oversight, ensuring funds are used appropriately.
  
- **Flexibility**: The system can cater to various needs – from parental control to collective decision-making in groups.
  
- **Transparency**: All transactions can be viewed by designated members, ensuring trust and accountability in collective setups.

- **Education**: In the children's wallet setup, youngsters are introduced to financial responsibility and the world of digital currencies.

These use cases exemplify how the Portmanteau Wallet concept can adapt to various real-world scenarios, bringing the power of decentralized finance to diverse user groups while maintaining controls and checks.



***Absolutely. Let's extend the Portmanteau Wallet concept to accommodate these specific scenarios:***

## **Portmanteau Wallet: Extended Use Cases**

### **1. Owner's Death**:
An unfortunate event where the wallet owner passes away and the funds need to be accessed by a designated heir or family member.

**Features**:
- **Dead Man's Switch**: A system where if the owner doesn't interact with their wallet for a specified period, a notification is sent to a trusted individual or group. 
- **Heir Access**: In the case of confirmed death, a multisig process can be initiated by designated heirs (like children or spouse) to access the funds.
- **Proof of Death**: The system may require a legal proof of death to initiate this process.

### **2. Lost Wallet**:
The wallet owner misplaces their mobile device or forgets their credentials.

**Features**:
- **Remote Freeze**: An option to remotely freeze the wallet to prevent unauthorized access. This can be initiated through another authenticated device or a web portal.
- **Friend Recovery**: Use the multisig process with trusted friends to recover the funds and move them to a new address.
- **Backup Recovery Phrase**: Traditional method where a phrase generated during wallet setup can be used to recover the wallet on a new device.

### **3. Physical Ambush or Robbery**:
The wallet owner is physically threatened to transfer their funds to a robber.

**Features**:
- **Duress Pin**: A special PIN which, when entered, sends a silent alert to a designated contact or authority, and can optionally trigger the emergency function to move funds to the long-term storage.
- **Timed Withdrawals**: Even if the robber forces a transfer, the funds can be programmed to only move after a certain time, giving law enforcement a window to act.

### **4. Forced Actions by Third Parties**:
Situations like lawsuits, debts, or governmental actions where funds might be seized.

**Features**:
- **Legal Hold Feature**: Allows the owner to put funds in a state where they can't be accessed for a specified period, ensuring they can't be moved under duress.
- **Friend Notify**: Trusted contacts are informed when a legal hold or forced transaction is made, ensuring transparency and possibly providing a way for them to intervene or advise.

### **Benefits**:

- **Safety**: Provides various safeguards against external threats and personal accidents, ensuring that the funds remain safe and can be recovered in emergencies.
  
- **Flexibility**: Each scenario has tools tailored to the situation, be it notifying trusted contacts, involving law enforcement, or locking down the funds.
  
- **Transparency**: Ensures that in high-pressure scenarios, the owner's wishes and security protocols are followed.

These extended use cases further solidify the utility of the Portmanteau Wallet in real-life situations. The combination of innovative blockchain solutions and traditional security measures makes it resilient to a wide array of challenges.

### ***Multitouch Wallet Unlock feature***:
- Brings an enhanced level of security and personalization to the Portmanteau app. Every time a user attempts to unlock their wallet, a distinct set of fingerprint marks will be randomly distributed across the screen. Despite the random distribution, the owner would be able to recognize the correct pattern or sequence necessary to unlock the wallet.

This innovation ensures that even if someone observes the unlock process multiple times, they would not be able to memorize or recreate the correct sequence due to its dynamic nature. This unique identification method, customizable by the user, relies on the user's deep familiarity with their chosen pattern, safeguarding the wallet against unauthorized access and offering a robust yet user-friendly security solution.
