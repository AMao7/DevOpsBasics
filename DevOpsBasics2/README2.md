# N-Tier Architecture

### Docker is architecture, microservice can be part of docker - 
- Monolith = build everything in one, have to change everything to deploy everything to add features like payment methods
    - Alot more work to deploy things
    - Simple and easy to manage
    - No scalability (Vertical-give failure as its one big box/Horizontal- does not give failure as its got others) or failover (no backup)
    - Does not use resource efficiently (whole box in on at all times if it vertical scalability)
    
    
 -2 Tier Architecture = Client/Server Arch, App/db
    - Some scalability and failover
    - Some resource efficiency
    
- 3 Tier Archiecture = Presentation (front end) /Logical/Data tiers


- 3-Tier architecture  = app split into different sections e.g, e-commerce websites have different payment methods
    - Model - View - Controller
    - Pros: Clearer structure, Supports horizontal scaliability and portable
    - Cons: Additional interface, more complex to setup/depliy/maintain and develop and more resources
    - to change all you need to do is change one service without touching any other code (as application is designed to work together)

- N tier architecture = Web server/ Database / app / internet iter
    - Requires communication between tiers
    
- Microservice architecture = Different services to support different sub tiers
    - Linked by REST API
    
    
### IP 
Stands for Internet Protocol
- 4 Sets of numbers that run from 0-255 called octets
- 256 x 256 x 256 x 256
- A: 192.X.X.X = CLASS A is the first octet
- B: 192.168.X.X = CLASS B is the first two octet
- C: 192.168.10.X = CLASS C is the first three octet
- IP is a dot in the subnet (which is provided by e.g router) - probably class C