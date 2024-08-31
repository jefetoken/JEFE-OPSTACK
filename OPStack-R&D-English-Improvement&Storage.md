# Progress in Blockchain Development with Optimism's OP STACK: The Case of Knuckles

<img src="https://github.com/jefetoken/JEFE-OPSTACK/blob/main/Knuckles-Extra/opstack2.jpg">

## 1. Improvements in Storage and Development of the Knuckles OPCHAIN

### **1.1 Enhanced Development and Capabilities of the Knuckles Blockchain with Optimism**

"Knuckles" Development has significantly advanced its storage and operations capabilities on the Optimism Sepolia testnet. This progress has been recorded by implementing an optimism blockchain on testnet using the optimism.io op stack package <a href="https://github.com/ethereum-optimism/optimism">OP STACK</a> and an open source explorer that allows for a broader view of what is happening on the blockchain, such as block and transaction production, expanding the request processing capacity and improving how the development of the “Knuckles” blockchain created with the completely OPEN SOURCE OPTIMISM Op Stack is visualized.

## **Key Actions:**

- **Upgraded Virtual Private Server (VPS) Establishment:** Equipped with 8GB of RAM and 160GB of SSD storage, this server supports a blockchain explorer that makes it easier to inspect transactions and block confirmations.

- **API Connection Optimization:** We increased computational requests to the Alchemy API for better integration with the Sepolia network.

- **Critical File Reconfiguration:** Analyzed genesis and rollup files for blockchain synchronization.

- **Knuckles RPC Development:** We created and implemented an RPC endpoint to allow for blockchain monitoring.

- **Use of Open Source Tools:** We implemented Blackscout to improve blockchain transparency and tracking.

Now, with RPC up and running, it is possible to effectively monitor and store blockchain data, observing transactions and block confirmations in real-time.

## Synchronization Optimization

- **Relevance of Initial Setup:** Correct configuration of genesis and rollup files is vital for efficient blockchain deployment and synchronization.

- ## **1. Genesis Critical File and its Creation:**

- **Blockchain Foundation:** The genesis file is essential because it defines the initial state of the blockchain. It is the starting point that contains all the initial parameters and configurations. Its correct creation is crucial for:

- **Integrity and Security:** It guarantees that the blockchain starts with a secure base and free of errors that could compromise the network from its conception.

- **Compatibility and Continuity:** It ensures that any evolution or update of the network is compatible with the initial state, facilitating future integrations and scalability.

- **Customization and Optimization:** It allows the blockchain to be customized for specific needs, with the OpStack.

## **2. Sepolia Testing Faucets:**

- **Realistic Test Environment:** Using Sepolia, a testnet on Optimism, to obtain test tokens is vital for:

- **Transaction Gas:** It allows you to generate transactions and smart contracts in an environment that reflects the conditions of the mainnet.

- **Development and Debugging:** It facilitates the development and debugging of applications and contracts without the risk of losing real value, speeding up the development and testing cycle, but most importantly, it allows you to meticulously analyze in real time how each of the op Stack components works in operation, allowing you to measure and optimize.

- **Accessibility:** Faucets allow the developer to obtain resources to test an environment before deploying it on a mainnet.

## **3. Modifying Proposer and Batcher Time Intervals:**

- **Operational Efficiency:** Adjusting the time intervals for the proposer (the one that proposes blocks) and the batcher (the one that groups transactions into blocks) is critical for:

- **Network Optimization:** Improving the speed and efficiency with which transactions are processed and confirmed, directly affecting user experience and network capacity.

- **Latency Reduction:** Minimizing the time between block proposal and inclusion can reduce latency, a key factor in the usability of decentralized applications (dApps).

- **Adaptability:** Allows the blockchain to adapt to different workloads and network conditions, ensuring that the OpStack-powered blockchain can scale and respond to changing demands efficiently.

- ## **Limitations of the Critical Genesis File and its Creation:**

- **Configuration Complexity:** The creation of the genesis file requires a deep understanding of the blockchain configuration. An error in this file can lead to security vulnerabilities or faulty functionality from the start.

- **Initial Immutability:** Once the genesis file is configured and the blockchain is launched, it is preferable not to alter or change fundamental aspects defined in this file.

- **Future Compatibility:** By defining the initial state, the genesis file should anticipate future upgrades and scalability.

- **Interoperability:** If the new blockchain is planned to interact with other networks or systems, the genesis file should be designed with these interactions in mind.

These limitations underscore the importance of meticulous planning and precise execution in creating the genesis file, as this document not only defines the beginning of the blockchain but also lays the foundation for its long-term evolution and success.

## **2. Sepolia Balances in Testing Faucets:**

- **Access to Faucets:** Faucets such as QuickNode or Superchain Faucet provide test tokens for the Optimism Sepolia network. These faucets are designed to distribute test ETH at no cost, with only a waiting period for every 24 hours.

- **Wallet Configuration:** It is always important to verify in every deployment that the use of wallets (such as MetaMask) are super well configured to interact with the Optimism Sepolia network. This implies adding the Sepolia network to your wallet with the correct chain parameters (Chain ID, RPC URL, etc.). Ensure the initial configuration of environment variables always takes into account the ERC-20 addresses of Admin, Proposer, Batcher, Sequencer, constant balance monitoring is important.

- **Token Request:** A simple request from your wallet to the chosen faucet and that's how easy it is to request tokens and continue with the blockchain deployment.

## **3. Modification of Time Intervals in Proposer and Batcher:**

The modification in synchronization components has been extensive and important to achieve the goal of having a good synchronization, this has involved generating test environments with altered variables in the configuration of:

- **Proposer:** The proposer is responsible for proposing new blocks. To adjust the intervals:
- **Node Configuration:** Through this you access the configuration of the Optimism node. This is generally done through configuration files. Our goal is to propose a new parameter such as `--proposeInterval` that defines how long a proposer waits before proposing a new block more adapted to the needs of Knuckles and its use case integration. Which may vary from who deploys it.

- **Batcher:** Through the crucial operation the batcher will continue batching transactions

- **Batching Interval:** Similar to proposer, another very interesting parameter was experimented with, the `--batchSubmitInterval` in the node configuration of the OPTIMISM OpStack source code
. This interval determines how often the batcher sends batches of transactions to the main network.

- **Efficiency Optimization:** Adjusting this interval can optimize gas cost in L1 versus transaction latency in L2. It is an active experiment so a longer interval could reduce costs by sending more transactions per batch, but would increase latency for L2 users.

Both processes require direct access to the blockchain software configuration or the source code if it is open source, as is the case with Optimism. Modifying these intervals should be done carefully, considering the balance between efficiency, cost, and user experience on the network.


Knuckels RPC BLOCKCHAIN
KNUCKLES OPCHAIN TESTNET RPC : http://51.195.202.219:8545 <br>
idchain: 42069 <br>
Blockchain inspector-explorer: https://explorer.jefetoken.com || http://217.182.72.132:3001/ <br>
https://github.com/jefetoken/JEFE-OPSTACK
<br>
<br>
In summary, these aspects are fundamental to creating an effective and efficient blockchain using Optimism's OpStack. Each plays a vital role in ensuring that the blockchain not only works correctly from the start but is also able to adapt and optimize for future needs and challenges.

## **Conclusion:**

The Knuckles project, using Optimism's technology specifically the OpStack, has proven to be fertile ground for blockchain applications and its use case as an educational implementation, facilitating analysis and study especially in terms of storage and network efficiency. However, the challenges in synchronization underscore the importance of continuous optimization and the need for fine-tuning of the blockchain configuration for optimal performance. Despite the challenges presented, particularly in synchronization and initial configuration, this project illustrates the potential of second layer solutions to overcome the limitations of the Ethereum blockchain. The experience gained with Knuckles not only paves the way for future improvements to its own network but also provides valuable lessons for the blockchain community , SUPERCHAIN all the way and for everone.

