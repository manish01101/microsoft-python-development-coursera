"""

Integration Testing Strategies

1. Top-Down Integration Testing
 Approach: Test from the highest-level modules (UI) down to lower-level components usingstub. Advantages:

 Early validation of overall design and navigation.
 Working system skeleton helps visualize final product. Disadvantages:

 Lower-level modules may get less attention.
 Creating realistic stubs can be tricky. Best Use: When high-level functionality (UI or core workflow) is critical or lower modules are frequently changing.

2. Bottom-Up Integration Testing
 Approach: Test lower-level modules first usingdriver, then integrate upward. Advantages:

 Thorough testing of fundamental components.
 Easier to isolate and fix errors. Disadvantages:

 Complete system not visible until the end. Best Use: When lower-level modules are stable and well-defined; suitable for object-oriented systems.

3. Sandwich (Hybrid) Integration Testing
 Approach: Combine top-down and bottom-up simultaneously; focus on a middle “target layer” where high-level and low-level modules meet. Advantages:

 Comprehensive testing of both high-level and low-level modules.
 Faster testing due to concurrent efforts. Disadvantages:

 More complex to coordinate stubs, drivers, and teams. Best Use: Large, complex projects with multiple critical modules at different layers (e.g., e-commerce platforms, OS development).

Real-world Examples:
 E-commerce website: Sandwich (UI + payment modules tested concurrently). Mobile banking app: Bottom-up (core banking modules first). Social media platform: Top-down (UI and new features first).

Key Idea: Integration testing ensures that all modules interact correctly, delivering a seamless and reliable user experience.



Test Doubles: Mocks, Stubs, and Fakes
Definition:
Test doubles are stand-ins for real objects in your code, used to isolate units of functionality and test them in a controlled environment. They help ensure reliable, fast, and independent testing without relying on actual external systems.
1. Mocks

Purpose: Verify interactions with dependencies and the order of operations.
Behavior: Programmed with expectations; test fails if interactions don’t match.
Example: Mock a payment processor to check if charge_card() is called after validate_address().
Use When: You need to ensure correct calls, parameters, or sequence of operations.
2. Stubs
Purpose: Provide predefined responses to method calls.
Behavior: Simple, predictable; ignores how or when called.
Example: Stub a weather service to always return “Partly cloudy, 18°C”.
Use When: You just need test data for the code to run, without checking interactions.
3. Fakes
Purpose: Lightweight, simplified implementation of real systems.
Behavior: Mimics real behavior but in a controlled, efficient way.
Example: Fake database storing data in memory instead of on disk.
Use When: You want realistic behavior without the complexity of real systems.
Choosing the Right Test Double:
Mocks: For testing interactions and sequence of operations.
Stubs: For providing canned responses and predictable data.
Fakes: For simulating complex systems in a lightweight, controlled manner.
Key Idea: Test doubles isolate dependencies, improve test reliability, and speed up testing, making them essential tools for robust software development.


"""
