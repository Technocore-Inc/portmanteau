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

- The user can select friends to be co-signers for the multi-sig address.
- For each friend, the wallet generates a public/private key pair. The public key is shared with the friend's Portmanteau wallet, while the private key remains with the user.
- The user sets the threshold for how many signatures are needed to authorize a transaction. For example, if the user selects 5 friends, they might set a threshold of 3 signatures to unlock the funds.

**3. Regular and Long-Term Compartments:**

- **Regular Compartment**: The user can transact normally using the private key stored on the device.
- **Long-Term Compartment**: To spend funds, the user sends a transaction request to the selected friends. This is a secure inquiry asking them to sign the multi-sig transaction.

**4. Transaction Authorization from Friends:**

- When a friend receives a transaction request, they can verify the identity of the user through a third-party channel (e.g., a phone call or video chat).
- Once the friend verifies the user's identity, they sign the transaction using their private key associated with the multi-sig address.
- After the required number of signatures is met (e.g., 3 out of 5 friends), the transaction is broadcasted to the network and funds are transferred from the long-term storage to the regular compartment or any other address.

**5. Backup & Recovery:**

- The user can backup the regular compartment's private key and the multi-sig configuration (not the private keys of the friends, for security reasons).
- In case of device loss or wallet deletion, the user can restore the regular compartment with the backed-up private key. For the multi-sig compartment, they would need to re-add friends and have them sign again.

**6. Features for Enhanced Security:**

- Two-factor authentication (2FA) for transaction approvals.
- Notifications for any activity on the long-term storage.
- Secure communication channel for transaction requests and approvals.

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