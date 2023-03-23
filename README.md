# Object Relations Code Challenge - JackPot

For this challenge, we'll be working with a JackPot domain.

We have three models: `Bid`, `Gambler`, and `Dealer`.

A `Gambler` has many `Bids`s. A `Dealer` has many `Bids`s. A `Bid` belongs to a `Gambler` and belongs to a `Dealer`.

`Gambler` - `Dealer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`. You'll need to create your own sample instances so that you can try out your code on your own. Make sure your relationships and methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it, run `python tools/debug.py` from the command line. This will start a `ipdb` session with your classes defined. You can test out the methods that you write here. You can add code to the `tools/debug.py` file to define variables and create sample instances of your objects.

Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

### Initializers, Readers, and Writers

#### Gambler

- `Gambler __init__(self, name)`
  - `Gambler` is initialized with a name (string)
- `Gambler get_name()`
  - returns the `Gambler`'s name

#### Dealer

- `Dealer __init__(self, name)`
  - `Dealer` is initialized with a name (string)
- `Dealer get_name()`
  - returns the Dealer's name

#### Bid

- `Bid __init__(self, gambler, dealer, amount)`
  - `Bid` is initialized with a `Gambler` instance, a `Dealer` instance, and an amount (float)
- `Bid get_amount()`
  - returns the amount for the `Bid` instance

### Object Relationship Methods

#### Bid

- `Bid get_gambler()`
  - returns the `Gambler` instance associated with the `Bid` instance
- `Bid get_dealer()`
  - returns the `Dealer` instance associated with the `Bid` instance

#### Gambler

- `Gambler get_bids()`
  - returns a list of `Bid` instances associated with the `Gambler` instance.
- `Gambler get_dealers()`
  - returns a list of `Dealer` instances who made a bid with the `Gambler` instance.
  - HINT: you can get the dealers by iterating through the list of bids

#### Dealer

- `Dealer get_bids()`
  - returns a list of all the `Bid` instances for the `Dealer`.
- `Dealer get_gamblers()`
  - returns a list of all of the `Gambler` instances that made a bid with the `Dealer`.
  - HINT: you can get the gamblers by iterating through the list of bids

### Aggregate and Association Methods

#### Gambler

- `Gambler has_bidded(dealer)`
  - returns `True` if the `Gambler` has made a bid with this `Dealer` (if there is a `Bid` instance for this `Gambler` that exists  with the `Dealer`), returns `False` otherwise
- `Gambler make_bid(dealer, amount)`
  - a `Dealer` instance and an amount (float) are passed in as arguments
  - this method should create a new `Bid` instance and attach it to both the `Gambler` instance and the `Dealer` instance

- `Gambler average_bid_amount()`
  - returns the average of all bid amounts for the `Gambler` instance
  - to average bid amounts, add all bid amounts together and divide by the total number of bids.
- `Gambler highest_bid()` 
  - returns the `Bid` instance with the highest bid amount for the gambler.

  ***BONUS***
  - `Gambler highest_average_gambler()`
    - returns the gambler with the highest average bids.




# practice-relationships-jackpot
