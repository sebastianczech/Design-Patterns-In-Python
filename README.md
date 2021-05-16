# Design patterns in Python

## Prerequsites

### Virtual environment

Create virtual environment:
```bash
python -m venv venv
```

Activate virtual environment:
```bash
source venv/bin/activate
```

### Depenendencies

Freeze currently installed packages:
```bash
pip freeze > requirements.txt
```

Install packages from file:
```bash
pip install -r requirements.txt
```

## Using repository

Start all tests:
```bash
pytest
```

Start all tests with coverage:
```bash
pytest --cov=patterns tests
```

## Design Patterns by examples

Examples of my code for selected design patterns 
described in [Source Making](https://sourcemaking.com/design_patterns) 
and [Refactoring Guru](https://refactoring.guru/design-patterns).

### Creational patterns

- [Abstract Factory](patterns/creational_pattern_abstract_factory.py) - Creates an instance of several families of classes
- [Builder](patterns/creational_pattern_builder.py) - Separates object construction from its representation
- [Factory Method](patterns/creational_pattern_factory_method.py) - Creates an instance of several derived classes
- Object Pool - Avoid expensive acquisition and release of resources by recycling objects that are no longer in use
- Prototype - A fully initialized instance to be copied or cloned
- [Singleton](patterns/creational_pattern_singleton.py) - A class of which only a single instance can exist

### Structural patterns

- [Adapter](patterns/structural_pattern_adapter.py) - Match interfaces of different classes
- Bridge - Separates an object's interface from its implementation
- Composite - A tree structure of simple and composite objects
- Decorator - Add responsibilities to objects dynamically
- Facade - A single class that represents an entire subsystem
- Flyweight - A fine-grained instance used for efficient sharing
- Private Class Data - Restricts accessor/mutator access
- Proxy - An object representing another object

### Behavioral patterns

- Chain of responsibility - A way of passing a request between a chain of objects
- Command - Encapsulate a command request as an object
- Interpreter - A way to include language elements in a program
- Iterator - Sequentially access the elements of a collection
- Mediator - Defines simplified communication between classes
- Memento - Capture and restore an object's internal state
- Null Object - Designed to act as a default value of an object
- Observer - A way of notifying change to a number of classes
- State - Alter an object's behavior when its state changes
- Strategy - Encapsulates an algorithm inside a class
- Template method - Defer the exact steps of an algorithm to a subclass
- Visitor - Defines a new operation to a class without change