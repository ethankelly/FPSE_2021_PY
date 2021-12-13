# Steps for Implementing Adapter Design Pattern

## Create an Interface

__CONCEPT:__
- In OOP, you can think of an interface as a contract ensuring all objects that implement it have the required 
features and methods of an "X" - the general type of thing represented by the interface.
- I.e. an interface T might ensure that "for an object to be a T-like object, it must implement X, Y and Z."
- E.g. a "Shape" interface might ensure any objects that want to be a Shape-type thing (a square, circle, etc.) need to
have methods determining the area and perimeter of each instance of the instance classes (classes implementing the 
interface). 
- Common example in Java: implementing `Comparable<Comparator>` interface, so that we can order our custom objects in
a custom way, e.g. defining one car object "greater than" another car object if the first has more horse power than the 
other.

__BLACKJACK:__
- First, create an `Input` interface with methods that will be required by anything that will deal with input
- Define a `getInputString` method in `Input`
- Now, let's make the existing class `ConsoleInput` implement our `Input` interface - this is a step towards ensuring 
all input-type things have the required methods, as we will see
- Client side - what currently uses the `ConsoleInput` class directly? We need to replace these instance class
references with interface references, in case we want to replace `ConsoleInput` with some other instance class that
implements `Input` in the future (e.g. text file input).

_Testing:_
- First, create `TestInput` class, which implements Input interface
- In `TestInput`, create a list instance variable to contain some input strings to test the `getInputString` method
- Unit test: create a TestInput instance, set some values in the instance variable and test getting input

## Over to you!

Can you do the same with an `Output` interface, implemented by the `ConsoleOutput` class?

__Steps:__
1. Create an `Output` interface with a method for printing a message to the console
2. Make the existing `ConsoleOutput` class implement this interface
3. Amend the main BlackJack class to use `Output` interface instance classes, rather than specifically `ConsoleOutput`
(use your IDE searc function for this, CTRL/CMD + F should bring this up)
4. Create a `TestOutput` class containing an instance variable with some test outputs and a method for setting this 
variable
5. Unit test your refactored `ConsoleOutput` class - create an instance of `TestOutput`, add some strings to the 
instance variable, call the testing method and ensure that your expected and obtained outputs match.

## Extension

If you're comfortable with everything we did with the adapter pattern, now let's return to Singleton - can you make the 
Deck a singleton?

__Hints:__
- The Deck variable should be static and private field inside a Deck class
- The Deck variable should only be accessed through a very special getter called `getInstance` - this should first query
whether the Deck variable has anything in it. If it does, then return that - if it doesn't, create a Deck, assign it to
the Deck field and return that. This ensures we only ever create the Deck _once_ - the first time we ask for it - and
each subsequent call to `getInstance` results in us getting the same instance we created (plus some possible amendments,
e.g, drawing cards and so on, which should be done using the `getInstance` method too).