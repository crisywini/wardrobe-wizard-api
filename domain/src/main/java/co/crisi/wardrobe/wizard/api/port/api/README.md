## What does it mean port API?

Well if you are coding in this part, I assume you have some new features you would like to implement but let's wait and understand what does an API port means in this architecture

## API (Application Programming Interface)
**Definition:** An API is an interface that defines how software components interact with each other. In the context of the hexagonal architecture, APIs are typically on the input ports side, meaning they define how external consumers (e.g., web clients or external services) interact with the application.

**Usage in Hexagonal Architecture:** APIs are exposed to users and define the operations available to them. For example, in a Java application using Spring, APIs might be represented by REST controllers (e.g., using @RestController) that expose functionality to external clients.