## What does it mean port API?

Well if you are coding in this part, I assume you have some new features you would like to implement but let's wait and understand what does an SPI port means in this architecture

## SPI (Service Provider Interface)
**Definition:** An SPI is an interface that defines a contract for service providers to implement. It is oriented towards extension and implementation of internal services. This allows different modules or libraries to provide specific implementations of an interface without the client code knowing or depending on the concrete implementations.

**Usage in Hexagonal Architecture:** SPIs are part of the output ports side, defining how the application interacts with external services such as databases, messaging systems, or third-party services. SPIs enable the application to be decoupled by delegating the responsibility of implementing these services to other modules.

