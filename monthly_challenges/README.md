flowchart TD
    subgraph BodhiTree_FrontEnd
        A[User Clicks Export Data Button]
    end
    
    subgraph BodhiTree_Backend
        B[Backend Validates and Collects Data]
    end
    
    subgraph TA_Buddy_Server
        C[Receive Data & Store]
        C1[Return 200 Response]
        C2[Check if Entries > 5000]
        C3[Kafka Producer Extracts Data]
        C4[Train/Test Split on Temp Location]
        C5[Enqueue Path in Queue]
        C6[Kafka Consumer Sleeps]
        C7[Load Model on GPU]
        C8[Consumer Wakes Up]
        C9[Consume Pending Tasks]
        C10[Free GPU and Sleep]
    end

    A --> B
    B --> C
    C --> C1
    C1 --> C2
    C2 --> |No| C6
    C2 --> |Yes| C3
    C3 --> C4
    C4 --> C5
    C5 --> C7
    C7 --> C8
    C8 --> C9
    C9 --> C10
